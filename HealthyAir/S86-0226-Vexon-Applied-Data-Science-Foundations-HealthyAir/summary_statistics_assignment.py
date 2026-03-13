import pandas as pd

# 1. Load a DataFrame (replace with your actual file if needed)
df = pd.read_csv('data/processed/cleaned_data.csv')
print('Columns:', df.columns.tolist())

# 2. Select individual numeric columns (example: 'amount')
if 'amount' in df.columns:
    col = 'amount'
    print(f'\nSummary statistics for column: {col}')
    print('Count:', df[col].count())
    print('Mean:', df[col].mean())
    print('Median:', df[col].median())
    print('Min:', df[col].min())
    print('Max:', df[col].max())
    print('Standard Deviation:', df[col].std())
    print('Variance:', df[col].var())

# 3. Compare with another numeric column if available (example: 'value')
if 'value' in df.columns:
    col2 = 'value'
    print(f'\nSummary statistics for column: {col2}')
    print('Count:', df[col2].count())
    print('Mean:', df[col2].mean())
    print('Median:', df[col2].median())
    print('Min:', df[col2].min())
    print('Max:', df[col2].max())
    print('Standard Deviation:', df[col2].std())
    print('Variance:', df[col2].var())

# 4. General summary for all numeric columns
print('\nGeneral summary for all numeric columns:')
print(df.describe())
