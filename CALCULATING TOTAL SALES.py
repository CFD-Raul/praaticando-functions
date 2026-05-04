# Carlos works in a store and needs to know the total value of sales made during the day.
# The sales are provided in a single line separated by spaces.

# Your task is to create a program that receives this line,
# converts the values to numbers and displays the total.

def values_converter(lista):
    return [float(values) for values in lista]

values = input('Enter the sales values: ').split()
converted_values = values_converter(values)
total = sum(converted_values)
print(f'The total sales amount was: ${total:.2f}')