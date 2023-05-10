#!/bin/bash

# Install Kaggle CLI
pip install kaggle

# Set your Kaggle API credentials
export KAGGLE_USERNAME=" " 
export KAGGLE_KEY=" " 

# Download the dataset using Kaggle API and unzip into the /opt/airflow/etl directory
kaggle datasets download -d jacksoncrow/stock-market-dataset --unzip -p /opt/airflow/load
