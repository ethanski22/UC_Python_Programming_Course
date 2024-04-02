# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load California Housing dataset
cali = fetch_california_housing()

# Convert dataset to DataFrame
cali_df = pd.DataFrame(cali.data, columns=cali.feature_names)
cali_df['Target'] = cali.target

# Initialize lists to store R2 and MSE scores
r2_scores = []
mse_scores = []

# Perform simple linear regression for each feature
for feature in cali.feature_names:
    # Extract single feature
    X = cali_df[[feature]]
    y = cali_df['Target']
    
    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate R2 score and MSE
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    # Append scores to lists
    r2_scores.append(r2)
    mse_scores.append(mse)
    
    # Print results
    print(f"{feature} has R2 score: {r2}")
    print(f"         has MSE score: {mse}\n")

# Perform multiple linear regression using all features
X = cali_df.drop('Target', axis=1)
y = cali_df['Target']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate R2 score and MSE for multiple linear regression
r2_multiple = r2_score(y_test, y_pred)
mse_multiple = mean_squared_error(y_test, y_pred)

# Print results for multiple linear regression
print("Multiple Linear Regression using All features")
print(f"R2 score: {r2_multiple}")
print(f"MSE score: {mse_multiple}\n")

# Create a table to determine which feature produced the best results
results_df = pd.DataFrame({
    'Feature': cali.feature_names,
    'R2 Score': r2_scores,
    'MSE Score': mse_scores
})

print(results_df)
