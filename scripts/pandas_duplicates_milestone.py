"""
Milestone: Identifying and Removing Duplicate Records
Dataset: Air Quality readings across major Indian cities
"""

import pandas as pd
import numpy as np

# ─────────────────────────────────────────────────────────────────
# STEP 1 — Load Dataset and Inject Duplicates
# ─────────────────────────────────────────────────────────────────
print("=" * 60)
print("STEP 1 — Load Dataset and Inject Duplicates")
print("=" * 60)

file_path = '../data/raw/air_quality_missing.csv'
df_base = pd.read_csv(file_path)

print(f"Base dataset shape: {df_base.shape}  →  {df_base.shape[0]} rows × {df_base.shape[1]} columns")
print(df_base.head())

# Inject exact duplicates (first 10 rows repeated)
exact_dupes = df_base.head(10).copy()

# Inject partial duplicates (same city+date, slightly different values)
partial_dupes = df_base.head(5).copy()
partial_dupes['pm25'] = partial_dupes['pm25'] + 0.1

# Create working dataset
df = pd.concat([df_base, exact_dupes, partial_dupes], ignore_index=True)

print(f"\nDataset WITH duplicates: {df.shape}  →  {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Exact duplicate rows injected  : {len(exact_dupes)}")
print(f"Partial duplicate rows injected: {len(partial_dupes)}")

# ─────────────────────────────────────────────────────────────────
# STEP 2 — Detecting Duplicate Rows
# ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 2 — Detecting Duplicate Rows")
print("=" * 60)

# (a) Basic detection — exact duplicates
dup_mask = df.duplicated()
print(f"Total rows            : {len(df)}")
print(f"Exact duplicates found: {dup_mask.sum()}")
print(f"Duplicate percentage  : {dup_mask.sum() / len(df) * 100:.2f}%")
print(f"Unique rows           : {len(df) - dup_mask.sum()}")

# (b) Inspect the duplicate rows
print("\nSample duplicate rows (using keep=False — shows all occurrences):")
duplicate_rows = df[df.duplicated(keep=False)]
print(duplicate_rows.sort_values(['city', 'date']).head(20).to_string())

# (c) Partial duplicates — same city + date
partial_dup_mask = df.duplicated(subset=['city', 'date'])
print(f"\nPartial duplicate rows (same city+date): {partial_dup_mask.sum()}")

# (d) Duplicate counts per city
dup_rows = df[df.duplicated(keep=False)]
if len(dup_rows) > 0:
    dup_by_city = (dup_rows
                   .groupby('city')
                   .size()
                   .reset_index(name='duplicate_count')
                   .sort_values('duplicate_count', ascending=False))
    print("\nDuplicate row counts by city:")
    print(dup_by_city.to_string(index=False))

# (e) Detection summary table
print("\nDuplicate Detection Summary:")
print(f"{'Detection Method':<40} {'Duplicates Found':>16}")
print("-" * 58)
print(f"{'All columns (keep=first)':<40} {df.duplicated(keep='first').sum():>16}")
print(f"{'All columns (keep=last)':<40} {df.duplicated(keep='last').sum():>16}")
print(f"{'All columns (keep=False)':<40} {df.duplicated(keep=False).sum():>16}")
print(f"{'Subset: city + date':<40} {df.duplicated(subset=['city','date']).sum():>16}")

# ─────────────────────────────────────────────────────────────────
# STEP 3 — Removing Duplicate Records
# ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 3 — Removing Duplicate Records")
print("=" * 60)

# (a) Keep first occurrence (default)
df_dedup_first = df.drop_duplicates(keep='first')
print(f"drop_duplicates(keep='first') → before: {df.shape}  after: {df_dedup_first.shape}  removed: {df.shape[0] - df_dedup_first.shape[0]}")

# (b) Keep last occurrence
df_dedup_last = df.drop_duplicates(keep='last')
print(f"drop_duplicates(keep='last')  → before: {df.shape}  after: {df_dedup_last.shape}  removed: {df.shape[0] - df_dedup_last.shape[0]}")

# (c) Drop ALL rows involved in duplication
df_dedup_none = df.drop_duplicates(keep=False)
print(f"drop_duplicates(keep=False)   → before: {df.shape}  after: {df_dedup_none.shape}  removed: {df.shape[0] - df_dedup_none.shape[0]}")

# (d) Deduplicate on subset — keep highest AQI reading for each city+date
df_sorted = df.sort_values('aqi', ascending=False)
df_dedup_subset = df_sorted.drop_duplicates(subset=['city', 'date'], keep='first')
df_dedup_subset = df_dedup_subset.sort_values(['city', 'date']).reset_index(drop=True)
print(f"drop_duplicates(subset=[city,date]) → before: {df.shape}  after: {df_dedup_subset.shape}  removed: {df.shape[0] - df_dedup_subset.shape[0]}")

# (e) Final clean DataFrame (keep first + reset index)
df_clean = df.drop_duplicates(keep='first').reset_index(drop=True)
print(f"\nFinal df_clean shape: {df_clean.shape}")

# ─────────────────────────────────────────────────────────────────
# STEP 4 — Verifying Deduplication Results
# ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 4 — Verifying Deduplication Results")
print("=" * 60)

# (a) Shape comparison
print("Shape Comparison:")
print(f"  BEFORE: {df.shape}  ({df.shape[0]} rows)")
print(f"  AFTER : {df_clean.shape}  ({df_clean.shape[0]} rows)")
print(f"  Rows removed  : {df.shape[0] - df_clean.shape[0]}")
print(f"  Data retained : {df_clean.shape[0] / df.shape[0] * 100:.1f}%")

# (b) Recheck for remaining duplicates
remaining_exact   = df_clean.duplicated().sum()
remaining_partial = df_clean.duplicated(subset=['city', 'date']).sum()
print(f"\nRemaining exact duplicates    : {remaining_exact}")
print(f"Remaining city+date duplicates: {remaining_partial}")
print("✓  Deduplication successful!" if remaining_exact == 0 else "✗  Duplicates still detected!")

# (c) Statistics comparison
numeric_cols = ['pm25', 'pm10', 'no2', 'co', 'aqi', 'temperature', 'humidity']
print("\nStatistic Comparison (Before vs After):")
print(f"{'Metric':<15} {'PM2.5 Before':>14} {'PM2.5 After':>13} {'AQI Before':>12} {'AQI After':>11}")
print("-" * 67)
print(f"{'count':<15} {df['pm25'].count():>14.0f} {df_clean['pm25'].count():>13.0f} {df['aqi'].count():>12.0f} {df_clean['aqi'].count():>11.0f}")
print(f"{'mean':<15} {df['pm25'].mean():>14.2f} {df_clean['pm25'].mean():>13.2f} {df['aqi'].mean():>12.2f} {df_clean['aqi'].mean():>11.2f}")
print(f"{'median':<15} {df['pm25'].median():>14.2f} {df_clean['pm25'].median():>13.2f} {df['aqi'].median():>12.2f} {df_clean['aqi'].median():>11.2f}")

# (d) Full summary table
print("\nDeduplication Strategy Comparison:")
print(f"{'Strategy':<45} {'Rows':>6} {'Removed':>8} {'Dupes After':>12}")
print("-" * 73)
strategies = [
    ('Original (with dupes)',                     df,            df.duplicated().sum()),
    ('drop_duplicates(keep="first")',              df_dedup_first, 0),
    ('drop_duplicates(keep="last")',               df_dedup_last,  0),
    ('drop_duplicates(keep=False)',                df_dedup_none,  0),
    ('drop_duplicates(subset=[city,date])',        df_dedup_subset,
     df_dedup_subset.duplicated(subset=['city','date']).sum()),
]
for name, dframe, dupes_after in strategies:
    removed = df.shape[0] - dframe.shape[0]
    print(f"{name:<45} {dframe.shape[0]:>6} {removed:>8} {dupes_after:>12}")

# (e) Final clean info
print("\n" + "=" * 60)
print("Final Clean DataFrame")
print("=" * 60)
print(f"Shape   : {df_clean.shape}")
print(f"Duplicates: {df_clean.duplicated().sum()}")
print(f"Cities  : {df_clean['city'].nunique()} unique")
print(f"Dates   : {df_clean['date'].nunique()} unique")
print(df_clean.dtypes)
