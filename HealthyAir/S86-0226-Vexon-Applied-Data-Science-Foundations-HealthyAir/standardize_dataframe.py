"""
standardize_dataframe.py

This script demonstrates how to standardize column names and data formats in a Pandas DataFrame, as required by the milestone assignment.
"""

import pandas as pd
import re

# Example raw data (simulating a messy CSV import)
data = {
    'First Name ': [' Alice ', 'BOB', 'Charlie'],
    'Last-Name': ['Smith', ' jones ', 'O\'Reilly'],
    'Date of Birth': ['2000/01/01', '1999-12-31', '01-02-2001'],
    'SCORE (%)': ['85 ', ' 90', '88'],
    'Category ': ['Student', 'student ', 'STUDENT']
}
df = pd.DataFrame(data)

print('--- BEFORE STANDARDIZATION ---')
print(df)
print('\nColumns:', df.columns.tolist())

# 1. Standardize column names
def clean_column(col):
    col = col.strip().lower()  # Lowercase and strip
    col = re.sub(r'[^a-z0-9_]', '_', col)  # Replace non-alphanumeric with _
    col = re.sub(r'_+', '_', col)  # Collapse multiple underscores
    col = col.strip('_')  # Remove leading/trailing underscores
    return col

df.columns = [clean_column(c) for c in df.columns]

# 2. Standardize text data (strip, lower, consistent categories)
df['first_name'] = df['first_name'].str.strip().str.lower()
df['last_name'] = df['last_name'].str.strip().str.title()
df['category'] = df['category'].str.strip().str.lower()

# 3. Standardize numeric data
df['score'] = pd.to_numeric(df['score'], errors='coerce')

# 4. Standardize date formats
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce', dayfirst=False)

print('\n--- AFTER STANDARDIZATION ---')
print(df)
print('\nColumns:', df.columns.tolist())

# 5. Show before/after for video walkthrough (print statements)
print('\nStandardization complete. Column names and data formats are now consistent.')
