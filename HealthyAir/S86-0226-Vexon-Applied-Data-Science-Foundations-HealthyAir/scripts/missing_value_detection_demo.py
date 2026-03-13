"""
Missing Value Detection Milestone
This script demonstrates how to detect, count, and inspect missing values in a Pandas DataFrame.
No cleaning or imputation is performed.
"""

import pandas as pd

# Example DataFrame with missing values
example_data = {
    'city': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', None],
    'pm25': [35.2, None, 22.5, 18.1, 40.0],
    'aqi': [120, 110, None, 90, 130],
    'station': ['A', 'B', None, 'D', 'E'],
    'co': [0.7, 0.8, None, 0.6, None]
}
df = pd.DataFrame(example_data)

print("STEP 1 — Data Preview")
print("=" * 60)
print(df)

print("\nSTEP 2 — Detect Missing Values")
print("=" * 60)
missing_count = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df) * 100).round(2)
missing_summary = pd.DataFrame({
    'Missing Count': missing_count,
    'Missing %': missing_pct
})
print(missing_summary[missing_summary['Missing Count'] > 0])

total_missing = df.isnull().sum().sum()
print(f"\nTotal missing cells: {total_missing}")
print(f"Rows with any NaN: {df.isnull().any(axis=1).sum()}")
print(f"Rows that are completely clean: {df.notnull().all(axis=1).sum()}")

print("\nSTEP 3 — Inspect Rows with Missing Data")
print("=" * 60)
rows_with_missing = df[df.isnull().any(axis=1)]
print(rows_with_missing)

print("\nSTEP 4 — Interpretation")
print("=" * 60)
print("Missing values indicate incomplete data. Always check for missing values before analysis or cleaning.")
