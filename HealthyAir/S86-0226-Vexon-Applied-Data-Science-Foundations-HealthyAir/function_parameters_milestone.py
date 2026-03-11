"""
Milestone: Passing Data into Functions and Returning Results
This script demonstrates:
- Defining functions with parameters
- Passing arguments to functions
- Returning values from functions
- Using returned results in further computation
- Avoiding common function mistakes
"""

# 1. Understanding Parameters and Arguments
def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

# 2. Returning Values from Functions
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

# 3. Using Returned Results
def square(x):
    """Return the square of a number."""
    return x * x

# 4. Avoiding Common Function Mistakes
def safe_divide(numerator, denominator):
    """Return the result of division, or None if denominator is zero."""
    if denominator == 0:
        return None
    return numerator / denominator

# --- Demonstration ---

# Using greet function
message = greet("HealthyAir")
print(message)  # Output: Hello, HealthyAir!

# Using add function
result = add(10, 5)
print(f"10 + 5 = {result}")

# Using square function with returned value from add
squared = square(result)
print(f"({result})^2 = {squared}")

# Using safe_divide function
quotient = safe_divide(20, 4)
print(f"20 / 4 = {quotient}")

# Handling division by zero
zero_div = safe_divide(10, 0)
if zero_div is None:
    print("Cannot divide by zero.")
else:
    print(f"10 / 0 = {zero_div}")

# End of milestone script
