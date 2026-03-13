"""
Milestone: Vectorized Operations Instead of Python Loops

This script demonstrates the difference between loop-based and vectorized operations in NumPy.
It covers:
1. Loop-based vs vectorized arithmetic
2. Vectorized comparisons
3. Common pitfalls

Run this script to see output and explanations.
"""

import numpy as np

print("--- 1. Loop-Based vs Vectorized Arithmetic ---")
# Loop-based approach
arr = np.array([1, 2, 3, 4, 5])
result_loop = []
for x in arr:
    result_loop.append(x * 2)
print("Loop-based result:", result_loop)

# Vectorized approach
result_vec = arr * 2
print("Vectorized result:", result_vec)

print("\n--- 2. Vectorized Arithmetic Operations ---")
arr2 = np.array([10, 20, 30, 40, 50])
# Add two arrays (vectorized)
sum_vec = arr + arr2
print("Sum of arrays (vectorized):", sum_vec)

# Subtract, multiply, divide
print("Element-wise subtraction:", arr2 - arr)
print("Element-wise multiplication:", arr * arr2)
print("Element-wise division:", arr2 / arr)

print("\n--- 3. Vectorized Comparisons and Conditions ---")
# Comparison (vectorized)
comp = arr > 2
print("arr > 2:", comp)

# Use boolean array to filter
filtered = arr[arr > 2]
print("Filtered (arr > 2):", filtered)

print("\n--- 4. Common Vectorization Pitfalls ---")
# Shape mismatch example
try:
    arr3 = np.array([1, 2])
    print(arr + arr3)  # This will raise an error if shapes are incompatible
except ValueError as e:
    print("Shape mismatch error:", e)

# Broadcasting works if shapes are compatible
arr4 = np.array([1])
print("Broadcasting with arr4:", arr + arr4)

print("\n--- 5. Summary ---")
print("Vectorized operations are concise, readable, and fast. Avoid loops for simple array math!")
