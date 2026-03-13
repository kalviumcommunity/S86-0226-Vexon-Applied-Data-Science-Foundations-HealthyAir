import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset (assumes cleaned data is available)
df = pd.read_csv('data/processed/cleaned_data.csv')

# 2. Select numeric columns
numeric_cols = df.select_dtypes(include='number').columns.tolist()
print('Numeric columns:', numeric_cols)

# 3. Visual inspection using boxplots for each numeric column
for col in numeric_cols:
    plt.figure(figsize=(5, 6))
    plt.boxplot(df[col].dropna(), vert=True, patch_artist=True)
    plt.title(f'Boxplot of {col}')
    plt.ylabel(col)
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.show()
    # For video: visually inspect for outliers beyond whiskers

# 4. Detecting outliers using the IQR rule for each numeric column
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
    print(f'\nOutliers in {col} using IQR rule:')
    print(outliers.values)
    print(f'Number of outliers in {col}:', len(outliers))
    # For video: explain why these points are flagged

# 5. (Optional) Visual inspection using scatter plots for pairs of numeric columns
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
    # For video: look for isolated or extreme points
