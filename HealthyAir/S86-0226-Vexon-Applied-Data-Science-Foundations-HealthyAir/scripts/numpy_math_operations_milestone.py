"""
Milestone: Performing Basic Mathematical Operations on NumPy Arrays

This script demonstrates core NumPy computations:
1. Element-Wise Array Operations (Addition, Subtraction, Multiplication, Division)
2. Scalar Operations on Arrays (Adding/Multiplying by a single number)
3. Comparing NumPy Arrays and Python Lists
4. Avoiding Common Mistakes (Shape mismatch demonstration conceptualized)
"""

import numpy as np

def main():
    # Setup arrays
    array_a = np.array([10, 20, 30, 40])
    array_b = np.array([2, 4, 6, 8])

    print("==================================================")
    print("1. Element-Wise Array Operations")
    print("==================================================")
    print(f"Array A: {array_a}")
    print(f"Array B: {array_b}\n")
    
    print(f"Addition (A + B):      {array_a + array_b}")
    print(f"Subtraction (A - B):   {array_a - array_b}")
    print(f"Multiplication (A * B):{array_a * array_b}")
    print(f"Division (A / B):      {array_a / array_b}\n")
    print("Notice that math applies exactly to the corresponding elements at each position.\n")


    print("==================================================")
    print("2. Scalar Operations on Arrays")
    print("==================================================")
    print("A scalar is just a single number applied to the whole array.")
    print(f"Original Array A: {array_a}")
    print(f"Add 5 to Array A: {array_a + 5}")
    print(f"Multiply Array A by 3: {array_a * 3}\n")


    print("==================================================")
    print("3. Comparing NumPy Arrays and Python Lists")
    print("==================================================")
    python_list_1 = [1, 2, 3]
    python_list_2 = [4, 5, 6]
    
    np_array_1 = np.array([1, 2, 3])
    np_array_2 = np.array([4, 5, 6])
    
    print(f"Python List Addition (`list_1 + list_2`):")
    print(f"Result: {python_list_1 + python_list_2}")
    print("-> The lists just attached (concatenated) end-to-end.\n")

    print(f"NumPy Array Addition (`np_array_1 + np_array_2`):")
    print(f"Result: {np_array_1 + np_array_2}")
    print("-> The arrays performed mathematically structured element-wise addition!\n")


    print("==================================================")
    print("4. Avoiding Common Mistakes")
    print("==================================================")
    print("Always ensure array shapes match when performing operations.\n")
    
    array_3_elements = np.array([1, 2, 3])
    array_4_elements = np.array([1, 2, 3, 4])
    
    print(f"Shape of Array 1: {array_3_elements.shape}")
    print(f"Shape of Array 2: {array_4_elements.shape}")
    print("If you try to add these directly: `array_3_elements + array_4_elements`")
    print("NumPy will raise a ValueError: 'operands could not be broadcast together with shapes'.")
    print("This is why checking .shape before math computation is essential.")


if __name__ == "__main__":
    main()
