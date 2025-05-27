# Dockerfile for a simple Python application

# Start with an official Python runtime as a parent image
# Using a slim version to keep the image size smaller
FROM python:3.9-slim

# Set the working directory in the container
# All subsequent commands (COPY, RUN, CMD) will be relative to this path
WORKDIR /app

# Copy the contents of the ./app directory from your host
# into the /app directory in the container
COPY ./app /app

# If your Python application has dependencies listed in a requirements.txt,
# you would uncomment the following lines:
# COPY ./app/requirements.txt /app/requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
# This is the port your application *inside* the container will listen on.
# You'll map this to a host port when you run the container.
EXPOSE 8000

# Define an environment variable. This is just an example, have fun with it :)
ENV APP_NAME="My Awesome Python App"
ENV GREETING_MESSAGE="Hello from Docker!"

# Command to run your application.
# This example assumes you have an app.py file that starts a simple web server.
# For a simple script, it might just be: CMD ["python", "app.py"]
# If your app.py uses Flask and runs on 0.0.0.0:8000, this would be appropriate:
CMD ["python", "app.py"]
