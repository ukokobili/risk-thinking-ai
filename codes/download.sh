#!/bin/bash

# Set your Kaggle API credentials
export KAGGLE_USERNAME=$(jq -r '.username' ~/.kaggle/kaggle.json)
export KAGGLE_KEY=$(jq -r '.key' ~/.kaggle/kaggle.json)

# Create local folder for store the raw datasets
mkdir -p ./raw_data

# Download the dataset using Kaggle API
kaggle datasets download -d jacksoncrow/stock-market-dataset --unzip

# Copy the unzipped directories to the raw_data folder
cp -r stocks ./raw_data
cp -r etfs ./raw_data


