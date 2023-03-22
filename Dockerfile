# Use the official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the project code into the container at /app
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME BypassDM

# Run the Django development server when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
