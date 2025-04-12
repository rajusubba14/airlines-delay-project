import pandas as pd

# S3 path to your CSV file
s3_path = 's3://mlprojects-raju/airlinesdelay/Airlines.csv'

# Read the CSV file from S3 into a DataFrame.
# By default, pd.read_csv will use s3fs if the path starts with "s3://"
df = pd.read_csv(s3_path)

# Display the first few rows to verify the data
print(df.head())