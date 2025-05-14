# Prompt the user to enter height in meters
height = input("Enter height in meters (e.g., 1.65): ")

# Prompt the user to enter weight in kilograms
weight = input("Enter weight in kilograms (e.g., 72): ")

# Convert weight to an integer and height to a float
weight_as_int = int(weight)
height_as_float = float(height)

# Calculate BMI
bmi = weight_as_int / height_as_float**2

# Print the BMI rounded to the nearest whole number
print(round(bmi))
