# Lucas is developing a system to generate financial reports
# and needs to filter only the even values from a list of numbers
# provided by the user.

# Create a program that receives a list of numbers
# and displays only the even ones using the filter() function.


user_numbers = input('Enter the numbers separated by space: ').split()
even_numbers = filter(lambda x: int(x) % 2 == 0, user_numbers) 
print("Even numbers:", " ".join(even_numbers))