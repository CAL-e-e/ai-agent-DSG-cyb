from census_api import fetch_census_data
from data_processing import clean_data

def main():
    print("Fetching census data...")
    df = fetch_census_data()
    df = clean_data(df)
    print(df.head())

if __name__ == "__main__":
    main()
