from census_api import fetch_census_data
from data_processing import clean_data

def generate_quality_report():
    # Fetch and process the data
    df = fetch_census_data()
    df = clean_data(df)

    # Basic stats
    total_records = len(df)
    total_variables = len(df.columns)
    total_data_points = total_records * total_variables

    # Missing values
    missing_counts = df.isna().sum()
    total_missing = missing_counts.sum()
    completeness = 1 - (total_missing / total_data_points)

    # Build report
    report = {
        "Total records": total_records,
        "Total variables": total_variables,
        "Total data points": total_data_points,
        "Total missing values": int(total_missing),
        "Completeness (%)": round(completeness * 100, 2)
    }

    print("\n=== QUALITY REPORT ===")
    for k, v in report.items():
        print(f"{k}: {v}")

    print("\nMissing values by column:")
    print(missing_counts)

    return report

if __name__ == "__main__":
    generate_quality_report()

