"""
Milestone: Writing Conditional Statements for Data Logic
This script demonstrates:
- Basic if statements
- if-else branching
- if-elif-else for multiple conditions
- Logical operators (and, or, not)
"""

# 1. Writing Basic if Statements
num = 10
if num > 5:
    print(f"Basic if: {num} is greater than 5")

if num < 5:
    print(f"Basic if: {num} is less than 5")  # Will not print

# 2. Using if–else for Decision Branching
name = "HealthyAir"
if name == "HealthyAir":
    print("if-else: Name matches HealthyAir")
else:
    print("if-else: Name does not match HealthyAir")

# 3. Handling Multiple Conditions with elif
score = 85
if score >= 90:
    print("if-elif-else: Grade is A")
elif score >= 80:
    print("if-elif-else: Grade is B")
elif score >= 70:
    print("if-elif-else: Grade is C")
else:
    print("if-elif-else: Grade is D or below")

# 4. Using Logical Operators
age = 25
has_id = True
if age >= 18 and has_id:
    print("Logical operators: Allowed entry (age >= 18 and has ID)")

is_member = False
if age < 18 or is_member:
    print("Logical operators: Special access (age < 18 or is member)")
else:
    print("Logical operators: No special access")

if not is_member:
    print("Logical operators: Not a member")

# 5. Edge Case Example
value = ""
if not value:
    print("Edge case: Value is empty or False")

# End of milestone script
