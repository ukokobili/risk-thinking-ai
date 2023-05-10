# Import libraries
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pickle


# Define the path to the directory containing the files
dir_path = '/home/nerd/RiskThinking/stage/etfs'

# Get a list of all file paths in the directory
file_paths = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith('.csv')]

# Initialize an empty list to hold the dataframes
dfs = []

# Loop through each file path and read the CSV file into a dataframe
for file_path in file_paths:
    # Use pandas' read_csv() function to read the CSV file into a dataframe
    df = pd.read_csv(file_path)
    # Append the dataframe to the dfs list
    dfs.append(df)

# Concatenate all the dataframes together into a single dataframe
df = pd.concat(dfs, ignore_index=True)

# Convert the 'date' column to a datetime object and set it as the index
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Remove rows with NaN values
df.dropna(inplace=True)

# Select features and target
features = ['vol_moving_avg', 'adj_close_rolling_med']
target = 'volume'

X = df[features]
y = np.log1p(df[target])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a RandomForestRegressor model
model = RandomForestRegressor(n_estimators=200, min_samples_split=50, random_state=1)

# Train the model
model.fit(X_train, y_train)

# Make predictions on test data
y_pred = model.predict(X_test)

# Calculate the Mean Absolute Error and Mean Squared Error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Print the Mean Squared Error and Mean Absolute Error
print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)

# Save the model as a pickle file
pickle.dump(model, open('model.pkl','wb'))

