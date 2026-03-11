import pandas as pd
import os

def main():
    print("--- 1. Understanding Pandas DataFrames ---")
    print("A DataFrame acts like a spreadsheet in Python with rows and columns.\n")

    print("--- 2. Creating DataFrames from Dictionaries ---")
    data_dict = {
        'Product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor'],
        'Price': [1200, 400, 800, 300],
        'Stock': [50, 100, 150, 75]
    }
    df_from_dict = pd.DataFrame(data_dict)
    print("DataFrame from Dictionary:")
    print(df_from_dict)
    print("\n")

    print("--- 3. Creating DataFrames from Files ---")
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'sample_data.csv')
    try:
        df_from_file = pd.read_csv(file_path)
        print("Successfully loaded DataFrame from CSV File:")
        print(df_from_file)
        print("\n")

        print("--- 4. Inspecting DataFrame Structure ---")
        print("First 3 Rows (head):")
        print(df_from_file.head(3))
        
        print("\nColumn Names:")
        print(df_from_file.columns.tolist())
        
        print("\nShape (Rows, Columns):")
        print(df_from_file.shape)
        
        print("\nData Types:")
        print(df_from_file.dtypes)
        
    except FileNotFoundError:
        print(f"Error: Could not find the file at {file_path}")

if __name__ == "__main__":
    main()