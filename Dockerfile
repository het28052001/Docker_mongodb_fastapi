# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables for MongoDB URI
ENV MONGODB_URI="mongodb+srv://het28082001:dhruvi19121998@cluster0.5csscov.mongodb.net/"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Run uvicorn to start the FastAPI application
CMD ["uvicorn", "mongo:app", "--host", "0.0.0.0", "--port", "8000"]
