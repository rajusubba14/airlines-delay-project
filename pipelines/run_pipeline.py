import sagemaker
from sagemaker.inputs import TrainingInput
from sagemaker.estimator import Estimator

# Manually specify your SageMaker execution role ARN.
# Ensure this role has all the required permissions (SageMaker, S3, CloudWatch, and ECR read/pull permissions).
role = "arn:aws:iam::225989361602:role/service-role/AmazonSageMaker-ExecutionRole-20250406T095913"

# Update S3 paths with your actual data and output locations.
s3_data = 's3://mlprojects-raju/airlinesdelay/processed_airlines.csv'
output_path = 's3://mlprojects-raju/airlinesdelay/model-artifacts/'

# Specify the full image URI (note that the URL doesn't include a "https://" prefix)
image_uri = "225989361602.dkr.ecr.us-east-1.amazonaws.com/my-custom-training-image:latest"

# Create the SageMaker Estimator.
# If you're running a custom training script located in the 'scripts/train.py' file, update the entry_point accordingly.
estimator = Estimator(
    image_uri=image_uri,       # This is your custom image from ECR.
    entry_point='scripts/train.py',  # Path to your training script.
    role=role,
    instance_count=1,
    instance_type='ml.m5.xlarge',
    output_path=output_path,
    py_version='py3'
)

# Define the training data input channel.
train_input = TrainingInput(s3_data=s3_data, content_type='text/csv')

# Launch the training job.
print("Starting the training job...")
estimator.fit({'train': train_input})
print("Training job completed!")