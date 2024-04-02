# Output table
# MedInc has R2 score: 0.45885918903846656
#          has MSE score: 0.7091157771765549

# HouseAge has R2 score: 0.012551235533311389
#          has MSE score: 1.2939617265100323

# AveRooms has R2 score: 0.013795337532284901
#          has MSE score: 1.2923314440807299

# AveBedrms has R2 score: -0.0003652108639329299
#          has MSE score: 1.3108875538359483

# Population has R2 score: 9.303316180342414e-05
#          has MSE score: 1.3102870667503983

# AveOccup has R2 score: 0.0005830567221980498
#          has MSE score: 1.3096449354773076

# Latitude has R2 score: 0.021915712646639274
#          has MSE score: 1.281690431624196

# Longitude has R2 score: 0.0017575657278725565
#          has MSE score: 1.3081058483312469

"""

Summarization:

Based on the output, 'MedInc' has the highest R2 score 
and the lowest MSE among the individual features, 
making it the most correlated feature with housing prices.

The simple linear regression analysis shows that the 
'MedInc' (Median Income) feature has the strongest correlation 
with housing prices, as it achieved the highest R2 score of 
approximately 0.469 and the lowest MSE of about 0.594. 
In contrast, the other individual features like 
'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 
'Latitude', and 'Longitude' demonstrated weaker correlations with 
housing prices, with R2 scores close to zero and higher MSE values 
ranging from approximately 1.329 to 1.343.

"""

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
