# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the Python script into the container
COPY get_success_rate.py .

# Install required packages
RUN pip install requests

# Command to run the script
CMD ["python", "./get_success_rate.py"]
