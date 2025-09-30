import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from census_api import fetch_census_data
from data_processing import clean_data
import json

def prepare_data_for_ml(df: pd.DataFrame) -> pd.DataFrame:
    # Create features
    df['poverty_rate'] = df['Population_Below_Poverty_Line'].astype(float) / df['Total_Population'].astype(float)
    df['Median_Household_Income'] = df['Median_Household_Income'].astype(float)

    # Convert poverty rate to percentage
    df['poverty_rate_pct'] = df['poverty_rate'] * 100

    # Define food desert based on poverty rate and income
    df['is_food_desert'] = ((df['poverty_rate'] > df['poverty_rate'].median()) &
                           (df['Median_Household_Income'] < df['Median_Household_Income'].median())).astype(int)

    return df

def train_food_desert_model():
    # Fetch and prepare data
    df = fetch_census_data()
    df = clean_data(df)
    df = prepare_data_for_ml(df)

    # Create and save poverty rates table
    county_poverty = df[['county', 'state', 'poverty_rate_pct']].sort_values(by='poverty_rate_pct', ascending=False)

    # Convert to dict for JSON storage
    poverty_data = county_poverty.to_dict(orient='records')

    # Save to JSON file
    with open('county_poverty_rates.json', 'w') as f:
        json.dump(poverty_data, f, indent=2)

    print("\nPoverty Rates saved to 'county_poverty_rates.json'")
    print("\nPoverty Rates by County:")
    print("------------------------")
    print(county_poverty.to_string(float_format=lambda x: '{:.2f}'.format(x)))

    # Rest of model training
    X = df[['poverty_rate', 'Median_Household_Income']]
    y = df['is_food_desert']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(random_state=42)
    model.fit(X_train_scaled, y_train)

    train_score = model.score(X_train_scaled, y_train)
    test_score = model.score(X_test_scaled, y_test)

    print(f"\nModel Performance:")
    print(f"Training accuracy: {train_score:.2f}")
    print(f"Testing accuracy: {test_score:.2f}")

    return model, scaler

if __name__ == "__main__":
    train_food_desert_model()