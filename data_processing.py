import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Use the new column names
    df = df.dropna(subset=[
        "Median_Household_Income",
        "Total_Population",
        "Population_Below_Poverty_Line"
    ])
    # Add any other cleaning steps here, using the new column names
    return df