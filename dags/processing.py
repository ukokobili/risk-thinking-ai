import os
import pandas as pd
import pyarrow.parquet as pq

# read symbols_valid_meta.csv into a pandas DataFrame
# read symbols_valid_meta.csv into a pandas DataFrame with the desired datatypes

def data_tranformation():
    symbols_df = pd.read_csv('/opt/airflow/load/symbols_valid_meta.csv')

    # define the path to the directory containing the files
    directories = ['/opt/airflow/load/stocks/', '/opt/airflow/load/etfs/']

    # loop over the directories
    for directory in directories:
        # loop over the files in the directory
        for filename in os.listdir(directory):
            if filename.endswith('.csv') and filename != 'symbols_valid_meta.csv':
                # read the file into a pandas DataFrame
                file_df = pd.read_csv(os.path.join(directory, filename), dtype={'Open': float, 'High': float, 'Low': float, 'Close': float, 'Adj Close': float, 'Volume': float})

                # extract the symbol from the file name
                symbol = os.path.splitext(os.path.basename(filename))[0]

                # find the row in symbols_df that matches the extracted symbol
                match = symbols_df[symbols_df['Symbol'] == symbol]

                # if a match is found, add the Symbol and Security Name columns to file_df
                if len(match) > 0:
                    file_df.insert(0, 'Symbol', match['Symbol'].iloc[0])
                    file_df.insert(1, 'Security Name', match['Security Name'].iloc[0])

                # convert the Date column to the desired datatype
                file_df['Date'] = pd.to_datetime(file_df['Date'], format='%Y-%m-%d').dt.date.astype(str)

                # write the updated file_df to a new CSV file with 'symbols' suffix
                output_filename = os.path.join(directory, symbol + '.csv')
                file_df.to_csv(output_filename, index=False)

###########################################################################################################

def stock_csv_to_parquet():
    csv_dir_list = ['/opt/airflow/load/stocks/']
    output_dir = '/opt/airflow/load/parquet_stock/'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for csv_dir in csv_dir_list:
        for file in os.listdir(csv_dir):
            if file.endswith('.csv'):
                csv_file_path = os.path.join(csv_dir, file)
                parquet_file_path = os.path.join(output_dir, os.path.splitext(file)[0] + '.parquet')
                table = pd.read_csv(csv_file_path).to_parquet(parquet_file_path)


############################################################################################################

def etfs_csv_to_parquet():
    csv_dir_list = ['/opt/airflow/load/etfs/']
    output_dir = '/opt/airflow/load/parquet_etfs/'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for csv_dir in csv_dir_list:
        for file in os.listdir(csv_dir):
            if file.endswith('.csv'):
                csv_file_path = os.path.join(csv_dir, file)
                parquet_file_path = os.path.join(output_dir, os.path.splitext(file)[0] + '.parquet')
                table = pd.read_csv(csv_file_path).to_parquet(parquet_file_path)