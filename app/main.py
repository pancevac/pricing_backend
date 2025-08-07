from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.routes.books import router as books_router
from app.routes.health import router as health_router
from app.events import lifespan
from app.config import settings
from app.exceptions import NotFoundException, IntegrityException

app = FastAPI(title="Pricing Backend API", lifespan=lifespan, debug=settings.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books_router)
app.include_router(health_router)


@app.exception_handler(NotFoundException)
async def not_found_exception_handler(_request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": exc.detail},
    )

@app.exception_handler(IntegrityException)
async def sqlalchemy_integrity_error_handler(_request: Request, exc: IntegrityException):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": exc.detail},
    )
