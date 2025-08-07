FROM python:3.12-slim

# Install system deps
RUN apt-get update && apt-get install -y curl

# Install Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Set working directory
WORKDIR /app

# Set working dir
WORKDIR /app

# Copy project files
COPY pyproject.toml poetry.lock* /app/

# Configure Poetry to not create virtualenvs (we want system-wide)
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi

# Copy the rest of the code
COPY . /app

# Expose port and start app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
