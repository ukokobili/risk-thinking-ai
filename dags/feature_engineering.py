import os
import pandas as pd

def stocks_cal():
    # define the paths of the folders containing the CSV files
    stocks_path = '/opt/airflow/load/stocks'

    # define the path of the output folder
    output_folder = '/opt/airflow/stage/'

    # create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # process the files in folder 1
    for filename in os.listdir(stocks_path):
        if filename.endswith('.csv'):
            # load the data into a DataFrame
            df = pd.read_csv(os.path.join(stocks_path, filename))

            # change fields name to small letters and replace white spaces with underscore
            df.columns = df.columns.str.lower().str.replace(' ','_')

            # Convert the 'Date' column to a datetime object
            df['date'] = pd.to_datetime(df['date'])

            # Check if 'symbol' is in the DataFrame columns
            if 'symbol' not in df.columns:
                print(f"'symbol' column not found in {filename}. Skipping this file.")
                continue

            # Group the DataFrame by symbol and calculate the rolling 30-day moving average of the trading volume
            df['vol_moving_avg'] = df.groupby('symbol')['volume'].rolling(window=30).mean().reset_index(0, drop=True)

            # Calculate the rolling median with a window size of 30
            df['adj_close_rolling_med'] = df['adj_close'].rolling(window=30).median()

            # save the updated DataFrame to a new CSV file in the output folder
            output_path = os.path.join(output_folder, 'stocks', filename)
            if not os.path.exists(os.path.dirname(output_path)):
                os.makedirs(os.path.dirname(output_path))
            df.to_csv(output_path, index=False)


#######################################################################################################################

def etfs_cal():

    # define the paths of the folders containing the CSV files
    etfs_path = '/opt/airflow/load/etfs'

    # define the path of the output folder
    output_folder = '/opt/airflow/stage/'

    # create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # process the files in folder 1
    for filename in os.listdir(etfs_path):
        if filename.endswith('.csv'):
            # load the data into a DataFrame
            df = pd.read_csv(os.path.join(etfs_path, filename))

            # change fields name to small letters and replace white spaces with underscore
            df.columns = df.columns.str.lower().str.replace(' ','_')

            # Convert the 'Date' column to a datetime object
            df['date'] = pd.to_datetime(df['date'])

            # Check if 'symbol' is in the DataFrame columns
            if 'symbol' not in df.columns:
                print(f"'symbol' column not found in {filename}. Skipping this file.")
                continue

            # Group the DataFrame by symbol and calculate the rolling 30-day moving average of the trading volume
            df['vol_moving_avg'] = df.groupby('symbol')['volume'].rolling(window=30).mean().reset_index(0, drop=True)

            # Calculate the rolling median with a window size of 30
            df['adj_close_rolling_med'] = df['adj_close'].rolling(window=30).median()

            # save the updated DataFrame to a new CSV file in the output folder
            output_path = os.path.join(output_folder, 'etfs', filename)
            if not os.path.exists(os.path.dirname(output_path)):
                os.makedirs(os.path.dirname(output_path))
            df.to_csv(output_path, index=False)

########################################################################################################################

def stock_csv_to_parquet():
    csv_dir_list = ['/opt/airflow/stage/stocks/']
    output_dir = '/opt/airflow/stage/parquet_stock/'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for csv_dir in csv_dir_list:
        for file in os.listdir(csv_dir):
            if file.endswith('.csv'):
                csv_file_path = os.path.join(csv_dir, file)
                parquet_file_path = os.path.join(output_dir, os.path.splitext(file)[0] + '.parquet')
                table = pd.read_csv(csv_file_path).to_parquet(parquet_file_path)


######################################################################################################################

def etfs_csv_to_parquet():
    csv_dir_list = ['/opt/airflow/stage/etfs/']
    output_dir = '/opt/airflow/stage/parquet_etfs/'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for csv_dir in csv_dir_list:
        for file in os.listdir(csv_dir):
            if file.endswith('.csv'):
                csv_file_path = os.path.join(csv_dir, file)
                parquet_file_path = os.path.join(output_dir, os.path.splitext(file)[0] + '.parquet')
                table = pd.read_csv(csv_file_path).to_parquet(parquet_file_path)
