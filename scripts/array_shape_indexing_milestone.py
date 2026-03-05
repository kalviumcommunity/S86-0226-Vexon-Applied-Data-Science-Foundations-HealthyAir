"""
Milestone: Understanding Array Shape, Dimensions, and Index Positions

This script demonstrates basic NumPy fundamentals:
1. Understanding Array Shape (rows and columns)
2. Understanding Dimensions (ndim)
3. Accessing Elements Using Index Positions
4. Visualizing Array Layout
"""

import numpy as np

def main():
    print("==================================================")
    print("1 & 2. Understanding Array Shape and Dimensions")
    print("==================================================")
    
    # 1D Array
    array_1d = np.array([10, 20, 30, 40, 50])
    print(f"1D Array: {array_1d}")
    print(f"Shape: {array_1d.shape}  --> (5 elements,)")
    print(f"Dimensions (ndim): {array_1d.ndim}\n")

    # 2D Array
    array_2d = np.array([
        [100, 200, 300],
        [400, 500, 600],
        [700, 800, 900]
    ])
    print("2D Array (Visualized as a grid/table):")
    print(array_2d)
    print(f"Shape: {array_2d.shape} --> (3 rows, 3 columns)")
    print(f"Dimensions (ndim): {array_2d.ndim}\n")


    print("==================================================")
    print("3. Accessing Elements Using Index Positions")
    print("==================================================")
    print("Remember: Indexing in Python completely starts at 0!\n")

    # Accessing 1D array elements
    print("--- 1D Array Indexing ---")
    print(f"First element (index 0): {array_1d[0]}")
    print(f"Third element (index 2): {array_1d[2]}")
    print(f"Last element (index -1): {array_1d[-1]}\n")

    # Accessing 2D array elements (row, column)
    print("--- 2D Array Indexing ---")
    print("Format is grid[row_index, column_index]")
    print(f"Element at Row 0, Col 0 (Top-left): {array_2d[0, 0]}")
    print(f"Element at Row 1, Col 2 (Middle row, Right col): {array_2d[1, 2]}")
    print(f"Element at Row 2, Col 1 (Bottom row, Middle col): {array_2d[2, 1]}\n")
    
    # Accessing an entire row or column
    print(f"Entire First Row (index 0): {array_2d[0, :]}")
    print(f"Entire Last Column (index 2): {array_2d[:, 2]}\n")


    print("==================================================")
    print("4. Visualizing Array Layout")
    print("==================================================")
    print("Rows run horizontally (axis=0), Columns run vertically (axis=1).")
    print("Row 0:  [100, 200, 300]   <-- indices (0,0), (0,1), (0,2)")
    print("Row 1:  [400, 500, 600]   <-- indices (1,0), (1,1), (1,2)")
    print("Row 2:  [700, 800, 900]   <-- indices (2,0), (2,1), (2,2)")


if __name__ == "__main__":
    main()
