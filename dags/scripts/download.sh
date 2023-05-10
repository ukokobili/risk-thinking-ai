#!/bin/bash

# Install Kaggle CLI
pip install kaggle

# Set your Kaggle API credentials
export KAGGLE_USERNAME="jacobukokobili" #$(jq -r '.username' ~/.kaggle/kaggle.json)
export KAGGLE_KEY="61b5f532a19d8c9f03d309e9b75a02ff" #$(jq -r '.key' ~/.kaggle/kaggle.json)

# Download the dataset using Kaggle API and unzip into the /opt/airflow/etl directory
kaggle datasets download -d jacksoncrow/stock-market-dataset --unzip -p /opt/airflow/load
