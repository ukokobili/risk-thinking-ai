## problem 1
1. Setup Airflow 

* Create `mkdir -p ./dags ./logs ./plugins ./load ./stage ./model echo -e "AIRFLOW_UID=$(id -u)" > .env` working directory.

* Create `Dockerfile` and `docker-compose.yaml` with the necessary dependencies

* Run the following `docker build .` to build the docker image, `docker-compose up airflow-init` to initiate Airflow,
`docker-compose up -d` to run `Airflow` in the `Docker` container. Enter `localhost:8080` in the browser and enter `Airflow` default username and password.

2. Download Dataset
* Create an API key in Kaggle 

* Enter the API credentials in the bash script created `download.sh`

* Create a dag `data_processing_dag.py` file and trigger the dag to commence download, transform and convert the data to parquet format from the `processing.py` file. 

## Problem 2
* Create a dag `feature_engineering_dag.py` file and trigger the dag to compute the moving average of the trading volume (Volume) and rolling median of 30 days per each stock and ETF, and the newly added column `vol_moving_avg` and `adj_close_rolling_med` respectively and convert the data to parquet format from the `feature_engineering.py` file. 

## Problem 3
* Create a dag `machine_learning_dag.py` file to the prediction model and a model is save as a pickle file from the `prediction_model.py` file. 

* The `pipeline_dags` triggers and run `data_processing_dag.py`, `feature_engineering_dag.py` and `machine_learning_dag.py` in sequential order.

## Problem
* The Dockerfile contains all dependencies for deploying the prediction app.

* The `app.py` is the Flask prediction app script

* The `result.py` is a python script to send request to the API server which can be run locally.

* The app is dockerized and deployed to the cloud via fly.io


Mean Squared Error: 1.9700897898059626
Mean Absolute Error: 0.86404038901568


