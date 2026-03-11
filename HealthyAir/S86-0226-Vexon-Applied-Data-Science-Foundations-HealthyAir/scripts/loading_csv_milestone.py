import pandas as pd
import os

def main():
    print("--- 1. Understanding CSV Files ---")
    print("CSV files store tabular data as plain text. Pandas reads these seamlessly.\n")

    print("--- 2. Loading CSV Files into Pandas ---")
    clean_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'clean_data.csv')
    df = pd.read_csv(clean_path)
    print("Clean CSV loaded!\n")

    print("--- 3. Inspecting Loaded Data ---")
    print("First 3 rows:")
    print(df.head(3))
    
    print("\nColumn Names:")
    print(df.columns.tolist())
    
    print(f"\nRow count: {len(df)}")
    print(f"Column count: {len(df.columns)}\n")
    
    print("Structure info:")
    df.info()
    print("\n")

    print("--- 4. Recognizing Common Loading Issues ---")
    messy_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'messy_data.csv')
    print("Attempting to load a problematic CSV file (messy_data.csv).")
    try:
        df_messy = pd.read_csv(messy_path)
        print("Loaded, but data is completely distorted due to unexpected rows and commas:")
        print(df_messy.head())
        print("\nNotice the incorrect headers ('Report Generated Automatically').")
        print("This proves why inspection immediately after loading is mandatory.")
    except Exception as e:
        print("Error caught during reading:\n", e)

if __name__ == "__main__":
    main()