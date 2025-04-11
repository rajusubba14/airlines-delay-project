import pandas as pd

# Replace 'data/airlines.csv' with your file path or S3 path if using s3fs.
df = pd.read_csv('s3://mlprojects-raju/airlinesdelay/Airlines.csv')

# writing data to s3

# Assume df_processed is your preprocessed DataFrame


# Write directly to S3 (ensure s3fs is installed: pip install s3fs)
s3_output_path = 's3://mlprojects-raju/airlinesdelay/processed_airlines.csv'
df.to_csv(s3_output_path, index=False)
print(f"Data written to {s3_output_path}")
