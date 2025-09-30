import requests
import pandas as pd

API_KEY = "c8926fa8d5fd044b5b828d2b3588e03d9f005485"

BASE_URL = "https://api.census.gov/data/2021/acs/acs5"

# Example variables:
# B19013_001E = Median household income
# B01003_001E = Total population
# B17001_002E = Population below poverty line
VARIABLES = ["B19013_001E", "B01003_001E", "B17001_002E"]


def fetch_census_data():
    params = {
        "get": ",".join(VARIABLES),
        "for": "county:*",
        "key": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    # First row is headers
    df = pd.DataFrame(data[1:], columns=data[0])
    return df


if __name__ == "__main__":
    df = fetch_census_data()
    print(df.head())
# Rename columns for better analysis
COLUMN_RENAME_MAP = {
    "B19013_001E": "Median_Household_Income",
    "B01003_001E": "Total_Population",
    "B17001_002E": "Population_Below_Poverty_Line"
}

def fetch_census_data():
    params = {
        "get": ",".join(VARIABLES),
        "for": "county:*",
        "key": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data[1:], columns=data[0])
    df = df.rename(columns=COLUMN_RENAME_MAP)
    return df