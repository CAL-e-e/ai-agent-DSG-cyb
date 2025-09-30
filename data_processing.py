import pandas as pd
from logger import logger

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting data cleaning process")
    try:
        # Check if DataFrame is empty or None
        if df is None or df.empty:
            logger.error("Received empty or None DataFrame")
            raise ValueError("DataFrame is empty or None")

        logger.info(f"Initial DataFrame shape: {df.shape}")

        # Drop rows with missing values in required columns
        required_columns = [
            "Median_Household_Income",
            "Total_Population",
            "Population_Below_Poverty_Line"
        ]

        # Verify all required columns exist
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            logger.error(f"Missing required columns: {missing_cols}")
            raise ValueError(f"Missing required columns: {missing_cols}")

        df = df.dropna(subset=required_columns)
        logger.info(f"Final DataFrame shape after cleaning: {df.shape}")

        logger.info("Data cleaning completed successfully")
        return df

    except Exception as e:
        logger.error(f"Error during data cleaning: {str(e)}")
        raise