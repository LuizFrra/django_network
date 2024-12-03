# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.6.1

# Install system dependencies and Poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean

# Add Poetry to the PATH
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy only the Poetry files to install dependencies first
COPY poetry.lock pyproject.toml /app/

# Install project dependencies
RUN poetry install

# Copy the application code into the container
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Default command
CMD ["poetry", "run", "manage.py", "runserver", "0.0.0.0:8000"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
