# Assigning variable:
math_score = 90 # Integer number
programming_score = 85.5 # Floating point
science_score = 95
students = 10

# Addition
total_score = math_score + programming_score
print(f"The average score is {total_score/2}")

# Substraction:
mathscience_diff = science_score - math_score
print(f"The science score is higher by {mathscience_diff} numbers than math score.")

# Multiplication
mathscore_alllstudents = math_score * students # Considering 10 students scored same marks in math
print("Total score in maths for all students is: ", mathscore_alllstudents)

# Division:
sciencescore_eachsection = science_score / 5 #Considering 5 sections were there in science paper
print(f"The student scored {sciencescore_eachsection} in each section in science paper.")

# Modulus
modulus_calculation = science_score % math_score
print(modulus_calculation) # The reminder after division

# Exponential:
exponent_math = math_score**2 # Exponent to the power 2.
print(exponent_math)

# Floor division:
floor_divion = science_score//math_score # Provide lower bound of integral divion.
print(floor_divion)

# Converting floating point to integer
print(int(programming_score)) # Programming score is 85.5(float), after converting to integer is 85.

# Converting integer to floating point:
print(float(math_score)) # Math score is 90(integer) and floating number is 90.0
