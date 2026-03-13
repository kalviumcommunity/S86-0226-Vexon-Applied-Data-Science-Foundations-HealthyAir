import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset (assumes cleaned data is available)
df = pd.read_csv('data/processed/cleaned_data.csv')

# 2. Select numeric columns
numeric_cols = df.select_dtypes(include='number').columns.tolist()
print('Numeric columns:', numeric_cols)

# 3. Create a scatter plot for the first two numeric columns (if available)
if len(numeric_cols) >= 2:
    x_col, y_col = numeric_cols[0], numeric_cols[1]
    plt.figure(figsize=(7, 5))
    plt.scatter(df[x_col], df[y_col], alpha=0.7, edgecolor='k')
    plt.title(f'Scatter Plot: {x_col} vs {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    # For video: explain observed relationship, clusters, trends, or outliers
else:
    print('Not enough numeric columns for a scatter plot.')

# 4. (Optional) Create scatter plots for other pairs if needed
# for i in range(len(numeric_cols)):
#     for j in range(i+1, len(numeric_cols)):
#         plt.figure(figsize=(7, 5))
#         plt.scatter(df[numeric_cols[i]], df[numeric_cols[j]], alpha=0.7, edgecolor='k')
#         plt.title(f'Scatter Plot: {numeric_cols[i]} vs {numeric_cols[j]}')
#         plt.xlabel(numeric_cols[i])
#         plt.ylabel(numeric_cols[j])
#         plt.grid(True, alpha=0.3)
#         plt.tight_layout()
#         plt.show()
