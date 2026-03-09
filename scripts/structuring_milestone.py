"""
Milestone: Structuring Python Code for Readability and Reuse
This script calculates the Body Mass Index (BMI) for multiple users, 
determines their BMI category, and summarizes the results.

This code demonstrates:
1. Organizing code into sections.
2. Using functions for reuse.
3. Separating logic from execution.
4. Writing readable, maintainable code.
"""

import sys

# ================================
# 1. Helper Functions
# ================================

def calculate_bmi(weight_kg, height_m):
    """Calculate BMI given weight in kg and height in meters."""
    if height_m <= 0:
        return 0
    return round(weight_kg / (height_m ** 2), 2)

def get_bmi_category(bmi):
    """Return the BMI category based on standard thresholds."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25.0 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def process_user_data(user_data):
    """Process a list of user dictionaries and add BMI information."""
    processed_data = []
    for user in user_data:
        bmi = calculate_bmi(user['weight'], user['height'])
        category = get_bmi_category(bmi)
        processed_user = {
            'name': user['name'],
            'weight': user['weight'],
            'height': user['height'],
            'bmi': bmi,
            'category': category
        }
        processed_data.append(processed_user)
    return processed_data

def display_results(processed_data):
    """Print the final BMI results in a readable format."""
    print("--- User BMI Report ---")
    for user in processed_data:
        print(f"Name: {user['name']} | BMI: {user['bmi']} | Category: {user['category']}")
    print("-----------------------")

# ================================
# 2. Main Execution Block
# ================================

def main():
    """Main execution function to orchestrate the script."""
    # Setup data
    users = [
        {"name": "Alice", "weight": 65, "height": 1.70},
        {"name": "Bob", "weight": 85, "height": 1.75},
        {"name": "Charlie", "weight": 50, "height": 1.60},
        {"name": "David", "weight": 95, "height": 1.80}
    ]

    # Logic execution
    print("Processing user health data...")
    results = process_user_data(users)

    # Output
    display_results(results)

if __name__ == "__main__":
    # Ensure setup, logic, and execution are separate
    main()
