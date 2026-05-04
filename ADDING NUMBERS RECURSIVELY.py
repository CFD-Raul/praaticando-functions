# Paulo is developing a program to calculate accumulated values in a financial system.
# He needs to sum all integers from 1 to n, where n is a value chosen by the user.
# Help Paulo by creating a recursive function that receives a number n and returns the sum of all integers from 1 to N.

def recursive_sum(user_number):
    if user_number == 1:
        return 1
    return user_number + recursive_sum(user_number - 1)

user_number = int(input('Enter a number to perform the sum: '))
result = recursive_sum(user_number)
print(f' The sum of integers from 1 to {user_number} is: {result}')