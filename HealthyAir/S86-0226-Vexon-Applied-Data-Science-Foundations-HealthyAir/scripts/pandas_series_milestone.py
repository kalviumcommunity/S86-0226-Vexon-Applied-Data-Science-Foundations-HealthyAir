import pandas as pd
import numpy as np

def main():
    print("--- 1. Understanding Pandas Series ---")
    print("A Pandas Series is a 1D labeled data structure.\n")

    print("--- 2. Creating a Series from Python Lists ---")
    my_list = [10, 20, 30, 40, 50]
    series_from_list = pd.Series(my_list)
    print("Series from List:")
    print(series_from_list)
    print("\n")

    print("--- 3. Creating a Series from NumPy Arrays ---")
    my_array = np.array([1.5, 2.5, 3.5, 4.5])
    series_from_array = pd.Series(my_array)
    print("Series from NumPy Array:")
    print(series_from_array)
    print("\n")

    print("--- 4. Understanding Index and Values ---")
    print("Values:", series_from_list.values)
    print("Index (RangeIndex):", series_from_list.index)
    
    # Adding meaningful custom labels
    custom_labels = ['A', 'B', 'C', 'D']
    labeled_series = pd.Series(my_array, index=custom_labels)
    print("\nLabeled Series:")
    print(labeled_series)
    
    print("\nAccess by label ('B'):", labeled_series['B'])
    print("Access by positional index (1):", labeled_series.iloc[1])


if __name__ == "__main__":
    main()
