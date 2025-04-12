FROM python:3.8-slim

# Set the working directory to the location SageMaker expects your code
WORKDIR /opt/ml/code

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container.
# Make sure your folder structure inside your project matches what you reference here.
COPY . .

# Set the command to run your training script.
# Make sure 'scripts/train.py' is relative to /opt/ml/code.
CMD ["python", "scripts/train.py"]  # Corrected CMD