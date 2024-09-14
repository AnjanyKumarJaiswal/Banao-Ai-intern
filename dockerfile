# Use official Python image from DockerHub
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file from the src directory
COPY src/requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code to /app, excluding the virtual environment
COPY src/ /app/

# Run the main script when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
