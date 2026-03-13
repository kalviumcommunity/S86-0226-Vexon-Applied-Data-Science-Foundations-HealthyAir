import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset (assumes cleaned data is available)
df = pd.read_csv('data/processed/cleaned_data.csv')

# 2. Identify time or date columns
time_cols = [col for col in df.columns if 'date' in col or 'time' in col]
print('Time-based columns:', time_cols)

# 3. Ensure the time column is in datetime format and sort by time
if time_cols:
    time_col = time_cols[0]
    df[time_col] = pd.to_datetime(df[time_col], errors='coerce')
    df = df.sort_values(by=time_col)
    # 4. Select a numeric column to plot
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 0:
        y_col = numeric_cols[0]
        plt.figure(figsize=(10, 5))
        plt.plot(df[time_col], df[y_col], marker='o', linestyle='-')
        plt.title(f'Trend of {y_col} over time')
        plt.xlabel(time_col)
        plt.ylabel(y_col)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        # For video: explain trend, notable changes, and why line plots are used
    else:
        print('No numeric columns found for plotting.')
else:
    print('No time-based column found in the dataset.')

# 5. (Optional) Plot additional numeric columns if available
if time_cols and len(numeric_cols) > 1:
    for y_col in numeric_cols[1:]:
        plt.figure(figsize=(10, 5))
        plt.plot(df[time_col], df[y_col], marker='o', linestyle='-')
        plt.title(f'Trend of {y_col} over time')
        plt.xlabel(time_col)
        plt.ylabel(y_col)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        # For video: compare trends across columns
