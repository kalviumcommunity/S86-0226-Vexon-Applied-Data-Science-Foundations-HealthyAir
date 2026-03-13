import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset (assumes cleaned data is available)
df = pd.read_csv('data/processed/cleaned_data.csv')

# 2. Select numeric columns
df_numeric = df.select_dtypes(include='number')
print('Numeric columns:', df_numeric.columns.tolist())

# 3. Create histograms for each numeric column
for col in df_numeric.columns:
    plt.figure(figsize=(7, 4))
    plt.hist(df_numeric[col].dropna(), bins=10, edgecolor='black')
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.show()
    # For video: explain bins, frequencies, and distribution shape here

# 4. (Optional) Compare two columns side by side
if len(df_numeric.columns) >= 2:
    col1, col2 = df_numeric.columns[:2]
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.hist(df_numeric[col1].dropna(), bins=10, edgecolor='black')
    plt.title(f'Histogram of {col1}')
    plt.xlabel(col1)
    plt.ylabel('Frequency')
    plt.subplot(1, 2, 2)
    plt.hist(df_numeric[col2].dropna(), bins=10, edgecolor='black')
    plt.title(f'Histogram of {col2}')
    plt.xlabel(col2)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    # For video: compare spread and skew visually
