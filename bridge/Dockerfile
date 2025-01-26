# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the bridge client script
COPY bridge_client.py .

# Run the bridge client script
CMD ["python", "bridge_client.py"]