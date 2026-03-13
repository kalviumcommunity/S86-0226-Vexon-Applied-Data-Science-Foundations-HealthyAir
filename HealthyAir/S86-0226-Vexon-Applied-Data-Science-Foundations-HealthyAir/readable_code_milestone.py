"""
Milestone: Writing Readable Variable Names and Comments (PEP8 Basics)
This script demonstrates:
- Descriptive variable names
- PEP 8 naming conventions
- Useful comments
- Readability best practices
"""

# 1. Writing Readable Variable Names
# Poor example:
x = 10
tmp = 5
val = x + tmp

# Good example:
item_count = 10
item_price = 5
total_cost = item_count + item_price

# 2. Following PEP 8 Naming Conventions
# Use snake_case for variables
user_name = "HealthyAirUser"
max_score = 100

# 3. Writing Useful Comments
# Calculate the average score for a user
user_score = 85
average_score = (user_score + max_score) / 2  # Average of user's score and max

# Explain why a check is needed (not what it does)
# Ensure the user has a valid score before proceeding
if user_score > 0:
    print(f"User score is valid: {user_score}")
else:
    print("User score is not valid.")

# 4. Avoiding Common Readability Mistakes
# Avoid commented-out code and redundant comments
# BAD: # Add 1 to the score
# user_score = user_score + 1

# BAD: # This is a variable
# score = 10

# GOOD: Only comment when intent is not obvious
# If the user is an admin, grant access
is_admin = True
if is_admin:
    print("Access granted.")

# End of milestone script
