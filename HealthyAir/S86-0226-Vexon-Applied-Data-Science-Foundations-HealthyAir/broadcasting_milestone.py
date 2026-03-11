"""
Milestone: Understanding NumPy Broadcasting with Simple Examples

This script demonstrates NumPy broadcasting with clear, small examples.
It covers:
1. Scalar-to-array broadcasting
2. 1D-to-1D broadcasting
3. 2D-to-1D broadcasting
4. Conceptual broadcasting rules

Run this script to see output and explanations.
"""

import numpy as np

print("--- 1. Broadcasting with Scalars ---")
arr = np.array([1, 2, 3])
scalar = 5
print("Array:", arr)
print("Scalar:", scalar)
print("Shape before:", arr.shape, "and scalar is a single value")
result_scalar = arr + scalar
print("Result (arr + scalar):", result_scalar)
print("Shape after:", result_scalar.shape)

print("\n--- 2. Broadcasting Between 1D Arrays ---")
arr1 = np.array([10, 20, 30])
arr2 = np.array([1])
print("Array 1:", arr1, "Shape:", arr1.shape)
print("Array 2:", arr2, "Shape:", arr2.shape)
result_1d = arr1 + arr2
print("Result (arr1 + arr2):", result_1d)
print("Shape after:", result_1d.shape)

# Example of incompatible shapes
try:
    arr3 = np.array([1, 2])
    print("Trying arr1 + arr3:")
    print(arr1 + arr3)
except ValueError as e:
    print("Shape mismatch error:", e)

print("\n--- 3. Broadcasting Between 2D and 1D Arrays ---")
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr1d = np.array([10, 20, 30])
print("2D Array:", arr2d, "Shape:", arr2d.shape)
print("1D Array:", arr1d, "Shape:", arr1d.shape)
result_2d_1d = arr2d + arr1d
print("Result (2D + 1D):", result_2d_1d)
print("Shape after:", result_2d_1d.shape)

# Broadcasting along columns
arr1d_col = np.array([[100], [200]])
print("2D Array:", arr2d, "Shape:", arr2d.shape)
print("1D column Array:", arr1d_col, "Shape:", arr1d_col.shape)
result_col = arr2d + arr1d_col
print("Result (2D + column):", result_col)
print("Shape after:", result_col.shape)

print("\n--- 4. Conceptual Broadcasting Rules ---")
print("Shapes are compared from the right. Size 1 dimensions are expandable. Incompatible shapes cause errors.")
print("Broadcasting lets you write concise, readable code without explicit loops!")
