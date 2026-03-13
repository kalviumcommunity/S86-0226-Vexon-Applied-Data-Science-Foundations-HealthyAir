import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset (assumes cleaned data is available)
df = pd.read_csv('data/processed/cleaned_data.csv')

# 2. Select numeric columns
df_numeric = df.select_dtypes(include='number')
print('Numeric columns:', df_numeric.columns.tolist())

# 3. Create a boxplot for each numeric column
for col in df_numeric.columns:
    plt.figure(figsize=(5, 6))
    plt.boxplot(df_numeric[col].dropna(), vert=True, patch_artist=True)
    plt.title(f'Boxplot of {col}')
    plt.ylabel(col)
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.show()
    # For video: explain median, quartiles, whiskers, and outliers here

# 4. (Optional) Compare boxplots across all numeric columns side by side
if len(df_numeric.columns) > 1:
    plt.figure(figsize=(8, 6))
    plt.boxplot([df_numeric[c].dropna() for c in df_numeric.columns], labels=df_numeric.columns, patch_artist=True)
    plt.title('Boxplots of All Numeric Columns')
    plt.ylabel('Value')
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.show()
    # For video: compare medians, spread, and outliers across columns
