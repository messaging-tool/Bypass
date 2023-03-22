# # Use the official Python runtime as a parent image
# FROM python:3.10-slim

# # Set the working directory to /app
# WORKDIR /app

# # Copy the requirements file into the container at /app
# COPY requirements.txt /app/

# # Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# # Copy the project code into the container at /app
# COPY . /app/

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Define environment variable
# ENV NAME BypassDM

# # Run the Django development server when the container launches
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



# Use Python 3.10 as the base image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install any dependencies required by the Django project
RUN pip install -r requirements.txt

# Copy the entire Django project to the working directory
COPY . .

# Set the environment variable for Django to know it's running in production mode
ENV NAME BypassDM

# Expose port 8000 for the Django app to run on
EXPOSE 8000

# Run the Django app using gunicorn as the server
CMD ["gunicorn", "BypassDM.wsgi:application", "--bind", "0.0.0.0:8000"]
