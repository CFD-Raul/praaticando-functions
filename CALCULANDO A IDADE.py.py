# Julia is a teacher and needs a program to help her students calculate their ages based on their birth year.
# Your task is to create a function that receives the birth year and the current year and returns the corresponding age.


def calculate_age(birth_year, current_year): 
    return current_year - birth_year 
 
birth = int(input("Enter the birth year: ")) 
current = int(input("Enter the current year: ")) 
age = calculate_age(birth, current) 
print(f"The age is {age} years.") 




# I DID IT THIS WAY: 
# def age_calculator():
#    year_of_birth = int(input('Enter your birth year: '))
#    current_year = int(input('Enter the current year: '))

#    student_age = current_year - year_of_birth
#    message = f'The student age is {student_age} years.'
#    return message

# print(age_calculator()) 
# BUT THIS WAY THE FUNCTION IS STATIC, THE MODEL ANSWER PROPOSED A MORE REUSABLE AND DYNAMIC SOLUTION: see above!

#The second version is less reusable because it mixes input/output operations with the function logic.
#It directly asks for user input (input()) inside the function.
#It returns a formatted message instead of just the calculated value.
#This makes it harder to reuse the function in other contexts (e.g., testing, APIs, or other programs).
#The first version is more flexible because:
#The function only performs the calculation.
#Inputs and outputs are handled outside the function.
#This separation makes the code more modular and reusable.



