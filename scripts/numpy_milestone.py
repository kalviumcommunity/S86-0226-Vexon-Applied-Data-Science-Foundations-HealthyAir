"""
Milestone: Creating NumPy Arrays from Python Lists

This script demonstrates the fundamentals of NumPy arrays:
1. Understanding NumPy Arrays vs Python Lists
2. Creating NumPy Arrays from Lists (1D and 2D)
3. Inspecting Array Properties (shape, dtype, ndim)
4. Basic Operations on Arrays (element-wise math)
"""

# Importing NumPy correctly
import numpy as np

def main():
    print("==================================================")
    print("1. Understanding NumPy Arrays vs Python Lists")
    print("==================================================")
    python_list = [1, 2, 3, 4]
    
    # Python lists repeat elements when multiplied
    print(f"Python List: {python_list}")
    print(f"Python List multiplied by 2: {python_list * 2}")
    print("Notice how the list just repeated itself instead of doing math.\n")


    print("==================================================")
    print("2. Creating NumPy Arrays from Lists")
    print("==================================================")
    # Creating a 1D array from a list
    list_1d = [10, 20, 30, 40]
    array_1d = np.array(list_1d)
    print(f"1D NumPy Array created from list:\n{array_1d}\n")

    # Creating a 2D (multi-dimensional) array from a nested list
    list_2d = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    array_2d = np.array(list_2d)
    print(f"2D NumPy Array created from nested lists:\n{array_2d}\n")


    print("==================================================")
    print("3. Inspecting Array Properties")
    print("==================================================")
    # Inspecting structure of the 2D array
    print("Let's inspect the properties of our 2D array:")
    print(f"- Shape (rows, columns): {array_2d.shape}")
    print(f"- Data Type (dtype): {array_2d.dtype}")
    print(f"- Dimensionality (ndim): {array_2d.ndim}")
    print(f"- Total elements (size): {array_2d.size}\n")


    print("==================================================")
    print("4. Basic Operations on Arrays")
    print("==================================================")
    base_array = np.array([5, 10, 15, 20])
    print(f"Base Array: {base_array}")

    # NumPy performs element-wise operations
    added_array = base_array + 100
    print(f"Array + 100 (Element-wise addition): {added_array}")

    multiplied_array = base_array * 2
    print(f"Array * 2 (Element-wise multiplication): {multiplied_array}")

    # Operations between two arrays
    array_b = np.array([1, 2, 3, 4])
    sum_arrays = base_array + array_b
    print(f"Array + Array (Element-wise addition of two arrays): {sum_arrays}\n")
    print("Notice how NumPy did the math for every single element instantly!")


if __name__ == "__main__":
    main()
