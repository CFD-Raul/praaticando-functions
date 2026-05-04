# Pedro is creating a product registration system for his store and realized that all customers' phone numbers are stored as strings.
# However, to make searching and validation easier, he needs these numbers to be treated as integers.

# Given the following code with a list of phone numbers incorrectly stored as str, create two functions,
# one that converts the types to integers and another that checks if the conversion was done correctly and all phone numbers are integers:


def convert_phones(list):  

   return [int(phone) for phone in list] 

def check_types(list):  

   for num in list:  

       if not isinstance(num, int):  

           return "Conversion error."  

   return "All numbers were converted correctly!" 

phones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

converted_phones = convert_phones(phones) 

print(check_types(converted_phones))  