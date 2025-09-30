from census_api import fetch_census_data
from data_processing import clean_data
from logger import *  # Add this import

def main():
    log_data_loading("census API")
    print("Fetching census data...")
    df = fetch_census_data()

    logger.info("Cleaning data...")
    df = clean_data(df)

    logger.info("Data processing complete. Displaying results:")
    print(df.head())

if __name__ == "__main__":
    main()