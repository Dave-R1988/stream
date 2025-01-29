# Use an official Python runtime as a parent image
FROM python:3.10-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install fastapi, psutil, pydantic with specific versions
RUN pip install --no-cache-dir fastapi==0.115.7 psutil==6.1.1 pydantic==2.10.6 fastapi-cli==0.0.7

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Command to run the FastAPI app using fastapi-cli
CMD ["fastapi", "run", "src/service.py", "--host", "0.0.0.0", "--port", "8000"]
