#!/usr/bin/env python

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Load data from S3 or local file
s3_path = 's3://mlprojects-raju/airlinesdelay/Airlines.csv'
data = pd.read_csv(s3_path)

# List of columns that are categorical but stored as object
categorical_cols = ['Airline', 'AirportFrom', 'AirportTo', 'filght_time']

# Convert each column to a categorical type and then map to numeric codes
for col in categorical_cols:
    data[col] = data[col].astype('category').cat.codes

# Now separate features and target (assuming 'Delay' is the target column)
X = data.drop('Delay', axis=1)
y = data['Delay']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = xgb.XGBRegressor(max_depth=5, eta=0.2, objective='reg:squarederror')
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("MSE:", mse)

# Save the model artifact
joblib.dump(model, 'model.joblib')