import pandas as pd

# 1. Load a DataFrame (replace with your actual file if needed)
df = pd.read_csv('data/raw/example_raw_data.txt')
print('Original columns:', df.columns.tolist())

# 2. Standardize column names: lowercase, replace spaces with underscores, remove special characters
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace(r'[^\w_]', '', regex=True)
)
print('Standardized columns:', df.columns.tolist())

# 3. Standardize text data (example: 'category' column)
if 'category' in df.columns:
    df['category'] = df['category'].str.strip().str.lower()
    print('Standardized category values:', df['category'].unique())

# 4. Standardize numeric and date formats (example: 'amount' and 'date' columns)
if 'amount' in df.columns:
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    print('Amount column type:', df['amount'].dtype)

if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    print('Date column type:', df['date'].dtype)

# 5. Inspect results
print(df.head())
print(df.dtypes)

# 6. Save cleaned data (optional)
df.to_csv('data/processed/cleaned_data.csv', index=False)
