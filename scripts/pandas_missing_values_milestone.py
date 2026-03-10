"""
Milestone: Handling Missing Values Using Drop and Fill Strategies
Dataset: Air Quality readings across major Indian cities
"""

import pandas as pd
import numpy as np

# ─────────────────────────────────────────────────────────────────
# STEP 1 — Load Dataset
# ─────────────────────────────────────────────────────────────────
file_path = '../data/raw/air_quality_missing.csv'
df = pd.read_csv(file_path)

print("=" * 60)
print("STEP 1 — Dataset Loaded")
print("=" * 60)
print(f"Shape: {df.shape}  →  {df.shape[0]} rows × {df.shape[1]} columns")
print(df.head())

# ─────────────────────────────────────────────────────────────────
# STEP 2 — Detect Missing Values
# ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 2 — Detect Missing Values")
print("=" * 60)

missing_count = df.isnull().sum()
missing_pct   = (df.isnull().sum() / len(df) * 100).round(2)

missing_summary = pd.DataFrame({
    'Missing Count': missing_count,
    'Missing %'    : missing_pct
})
print(missing_summary[missing_summary['Missing Count'] > 0])

total_missing = df.isnull().sum().sum()
print(f"\nTotal missing cells: {total_missing}")
print(f"Rows with any NaN: {df.isnull().any(axis=1).sum()}")

# ─────────────────────────────────────────────────────────────────
# STEP 3 — Drop Strategies
# ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 3 — Drop Strategies")
print("=" * 60)

# (a) Drop rows with any missing value
df_drop_any = df.dropna()
print(f"dropna() any   → shape before: {df.shape}  after: {df_drop_any.shape}  lost: {df.shape[0] - df_drop_any.shape[0]} rows")

# (b) Drop rows missing in critical column (aqi)
df_drop_aqi = df.dropna(subset=['aqi'])
print(f"dropna(subset=['aqi']) → shape: {df_drop_aqi.shape}  lost: {df.shape[0] - df_drop_aqi.shape[0]} rows")

# (c) Drop all-NaN rows
df_drop_all = df.dropna(how='all')
print(f"dropna(how='all')      → shape: {df_drop_all.shape}  lost: {df.shape[0] - df_drop_all.shape[0]} rows")

# (d) Drop columns with < 80% non-null values
threshold = int(0.80 * len(df))
df_drop_cols = df.dropna(axis=1, thresh=threshold)
dropped_cols = set(df.columns) - set(df_drop_cols.columns)
print(f"dropna(axis=1, thresh=80%) → columns dropped: {dropped_cols if dropped_cols else 'None'}")

# ─────────────────────────────────────────────────────────────────
# STEP 4 — Fill Strategies
# ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 4 — Fill Strategies")
print("=" * 60)

numeric_cols = ['pm25', 'pm10', 'no2', 'co', 'aqi', 'temperature', 'humidity']

# (a) Fill with constant
df_fill_const = df.copy()
df_fill_const['co'] = df_fill_const['co'].fillna(0)
print(f"Constant fill (co → 0): missing after = {df_fill_const['co'].isnull().sum()}")

# (b) Fill with mean
df_fill_mean = df.copy()
pm25_mean = df_fill_mean['pm25'].mean().round(2)
df_fill_mean['pm25'] = df_fill_mean['pm25'].fillna(pm25_mean)
print(f"Mean fill (pm25 → {pm25_mean}): missing after = {df_fill_mean['pm25'].isnull().sum()}")

# (c) Fill with median
df_fill_median = df.copy()
aqi_median = df_fill_median['aqi'].median()
df_fill_median['aqi'] = df_fill_median['aqi'].fillna(aqi_median)
print(f"Median fill (aqi → {aqi_median}): missing after = {df_fill_median['aqi'].isnull().sum()}")

# (d) Fill with mode (categorical)
df_fill_mode = df.copy()
station_mode = df_fill_mode['station'].mode()[0]
df_fill_mode['station'] = df_fill_mode['station'].fillna(station_mode)
print(f"Mode fill (station → '{station_mode}'): missing after = {df_fill_mode['station'].isnull().sum()}")

# (e) Forward fill (time-series)
df_ffill = df.sort_values(['city', 'date']).copy().reset_index(drop=True)
df_ffill[numeric_cols] = df_ffill[numeric_cols].ffill()
print(f"ffill: missing numeric after = {df_ffill[numeric_cols].isnull().sum().sum()}")

# (f) Backward fill
df_bfill = df.sort_values(['city', 'date']).copy().reset_index(drop=True)
df_bfill[numeric_cols] = df_bfill[numeric_cols].bfill()
print(f"bfill: missing numeric after = {df_bfill[numeric_cols].isnull().sum().sum()}")

# ─────────────────────────────────────────────────────────────────
# STEP 5 — Combined Cleaning Pipeline
# ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 5 — Combined Pipeline (all columns)")
print("=" * 60)

df_clean = df.copy()

for col in numeric_cols:
    median_val = df_clean[col].median()
    df_clean[col] = df_clean[col].fillna(median_val)
    print(f"  Filled '{col}' with median = {median_val:.2f}")

station_mode = df_clean['station'].mode()[0]
df_clean['station'] = df_clean['station'].fillna(station_mode)
print(f"  Filled 'station' with mode = '{station_mode}'")

remaining_missing = df_clean.isnull().sum().sum()
print(f"\nMissing values after full pipeline: {remaining_missing}")
print(f"Clean shape: {df_clean.shape}")

# ─────────────────────────────────────────────────────────────────
# STEP 6 — Drop vs Fill Comparison
# ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 6 — Drop vs Fill Comparison")
print("=" * 60)

df_drop = df.dropna()
# df_clean already built above

print(f"{'Metric':<20} {'Original':>10} {'Drop':>10} {'Fill (Med)':>12}")
print("-" * 56)
print(f"{'Rows':<20} {df.shape[0]:>10} {df_drop.shape[0]:>10} {df_clean.shape[0]:>12}")
print(f"{'Missing values':<20} {df.isnull().sum().sum():>10} {0:>10} {0:>12}")
print(f"{'PM2.5 Mean':<20} {df['pm25'].mean():>10.2f} {df_drop['pm25'].mean():>10.2f} {df_clean['pm25'].mean():>12.2f}")
print(f"{'PM2.5 Median':<20} {df['pm25'].median():>10.2f} {df_drop['pm25'].median():>10.2f} {df_clean['pm25'].median():>12.2f}")
print(f"{'AQI Mean':<20} {df['aqi'].mean():>10.2f} {df_drop['aqi'].mean():>10.2f} {df_clean['aqi'].mean():>12.2f}")

# ─────────────────────────────────────────────────────────────────
# STEP 7 — Decision Guide (auto-recommendation)
# ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 7 — Decision Guide")
print("=" * 60)

for col in df.columns:
    pct_missing = df[col].isnull().mean() * 100
    dtype = df[col].dtype

    is_numeric = pd.api.types.is_numeric_dtype(df[col])
    if pct_missing == 0:
        recommendation = "No action needed"
    elif pct_missing > 50:
        recommendation = "DROP the column (too sparse)"
    elif not is_numeric:
        recommendation = f"FILL with mode = '{df[col].mode()[0]}'"
    else:
        skew = abs(df[col].skew())
        if skew > 1.0:
            recommendation = f"FILL with median = {df[col].median():.2f} (skewed)"
        else:
            recommendation = f"FILL with mean = {df[col].mean():.2f} (symmetric)"

    print(f"  {col:12s} | {pct_missing:5.1f}% missing | {recommendation}")

# ─────────────────────────────────────────────────────────────────
# STEP 8 — Save Cleaned Data
# ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 8 — Save Cleaned Data")
print("=" * 60)

output_path = '../data/processed/air_quality_cleaned.csv'
df_clean.to_csv(output_path, index=False)

saved_df = pd.read_csv(output_path)
print(f"Saved to: {output_path}")
print(f"Shape: {saved_df.shape}")
print(f"Missing values in saved file: {saved_df.isnull().sum().sum()}")

print("\n" + "=" * 60)
print("All steps complete. Missing values handled successfully.")
print("=" * 60)
