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

## Problem 4
* The Dockerfile contains all dependencies for deploying the prediction app.

* The `app.py` is the Flask prediction app script

* The `result.py` is a python script to send request to the API server which can be run locally.

* The app is dockerized and deployed to the cloud via fly.io


## Workflow Image
Dockerized workflow imagefor Problems 1-3 with dependencies and build/execution configurations...Workflow image: docker pull jkop100/riskai

## Model Training
The dataset was too large to work with, so I had to use only 10% of the ETFs dataset. I shuffled the data and split it into a smaller sample to enable me to perform training on the dataset.

For training the model, I used Random Forest Regressor with the following parameters: `n_estimators=200`, `min_samples_split=50`, and `random_state=1`. The model produced the following results while evaluating its performance:
Mean Squared Error: 1.97
Mean Absolute Error: 0.86

However, I was unable to fine-tune the model or perform hyperparameter tuning due to the constant crashing of the notebook kernel.

## Model Deploy
The model was successfully deployed to the cloud via Fly.io. Unfortunately, tha model `ai-app` application hosted on Fly.io crashed because it ran out of memory. I provided a python script `result.py`  to send request to the API server which can be run locally and it's located in the `model` folder.

## Technologies
* Airflow
* Docker
* Flask
* Python
* Flask
* Fly.io
* Scikit-learn
* Gunicorn

## Directories
* `load` contains raw data
* `stage` contains transformed data with aggregation
* `model` contains prediction app, model, Dockerfile for building Docker image, fly.toml config for deploy to Fly.io

## Resources
* https://github.com/DataTalksClub/data-engineering-zoomcamp
* https://www.marketvolume.com/analysis/volume_ma.asp
* https://stackoverflow.com/questions/20906474/
* https://stackoverflow.com/questions/20906474/
* https://www.youtube.com/watch?v=Q4kKShL2muA&list=PLGZpjgRdXegnAephEInJwYmscGtPgLbBs&index=17
* https://stackoverflow.com/questions/66699394/airflow-how-to-get-pip-packages-installed-via-their-docker-compose-yml
* https://www.youtube.com/watch?v=Gs15V79cauo
* https://www.youtube.com/watch?v=ZS1ivzlymPQ
* https://fly.io/docs/apps/launch/#customize-the-configuration-file
* https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe#21232849

## Additional Resources
ChatGPT:
* Question: How can I insert Symbol	and Security Name with it's values from symbols_valid_meta.csv	into A.csv	where the Symbol matches with the "A" from the A.csv without the extention. Below are the sample datasets:

* Answer:
    ```
    import pandas as pd
    import os

    # read symbols_valid_meta.csv into a pandas DataFrame
    symbols_df = pd.read_csv('symbols_valid_meta.csv')

    # read A.csv into a pandas DataFrame
    a_df = pd.read_csv('A.csv')

    # extract the symbol from the file name
    symbol = os.path.splitext(os.path.basename('A.csv'))[0]

    # find the row in symbols_df that matches the extracted symbol
    match = symbols_df[symbols_df['Symbol'] == symbol]

    # if a match is found, add the Symbol and Security Name columns to a_df
    if len(match) > 0:
        a_df.insert(0, 'Symbol', match['Symbol'].iloc[0])
        a_df.insert(1, 'Security Name', match['Security Name'].iloc[0])

    # write the updated a_df to a new CSV file
    a_df.to_csv('A_with_symbols.csv', index=False)

    ```

    * Question: 
    How do I fix this error: Canceled future for execute_request message before replies were done. The Kernel crashed while executing code in the the current cell or a previous cell. Please review the code in the cell(s) to identify a possible cause of the failure.

    * Answer:
    This error message typically occurs in Jupyter notebooks or JupyterLab when the kernel of the notebook has crashed or disconnected while executing a code cell.

    To fix this error, you can try the following steps:

    Restart the kernel: Click on the "Kernel" menu in the Jupyter notebook interface and select "Restart". This will restart the kernel and clear any previously executed code.

    Run the code again: Once the kernel has been restarted, try running the code cell again. If the error persists, try running the code cell in a new notebook.

    Check for syntax errors: Review the code in the cell to see if there are any syntax errors that could be causing the kernel to crash. If you find any syntax errors, fix them and try running the code cell again.

    Check for memory issues: If you are working with large datasets, it is possible that the kernel is running out of memory. Try clearing the workspace or freeing up memory before running the code cell again.

    Update Jupyter: If you are using an older version of Jupyter, it is possible that there are known bugs that are causing the kernel to crash. Updating to the latest version may help to fix the issue.

    If none of these steps help, it may be necessary to seek further assistance or debug the code with additional tools or techniques.


