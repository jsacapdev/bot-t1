# Use an official Python runtime as a parent image
FROM python:3.13-slim-bookworm

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container
# Assuming requirements.txt is in the root of your repo
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the 'src/app' directory from your host into the 'app' directory in the container
COPY src/app/ .

# Set the command to run the application's main entry point
# Now main.py is directly under /app
CMD ["python", "main.py"]