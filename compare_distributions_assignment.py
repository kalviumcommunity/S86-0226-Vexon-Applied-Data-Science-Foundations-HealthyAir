import pandas as pd

# 1. Load a DataFrame with multiple numeric columns
# (Assumes you have already cleaned your data)
df = pd.read_csv('data/processed/cleaned_data.csv')
print('Numeric columns:', df.select_dtypes(include='number').columns.tolist())

# 2. Compute summary statistics for each numeric column
summary = df.describe()
print('\nSummary statistics for all numeric columns:')
print(summary)

# 3. Compare central tendency (mean, median) and spread (std, range) across columns
numeric_cols = df.select_dtypes(include='number').columns
print('\nCentral tendency and spread comparison:')
for col in numeric_cols:
    mean = df[col].mean()
    median = df[col].median()
    std = df[col].std()
    col_min = df[col].min()
    col_max = df[col].max()
    col_range = col_max - col_min
    print(f"\nColumn: {col}")
    print(f"  Mean: {mean}")
    print(f"  Median: {median}")
    print(f"  Min: {col_min}")
    print(f"  Max: {col_max}")
    print(f"  Range: {col_range}")
    print(f"  Standard Deviation: {std}")

# 4. Identify columns with highest and lowest variability
variability = df[numeric_cols].std().sort_values(ascending=False)
print('\nColumns sorted by variability (standard deviation):')
print(variability)

# 5. Interpretation (add your own observations in your video or report)
# Example: Which columns are most/least variable? Which have similar or different means/medians?
