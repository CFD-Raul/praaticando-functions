# Miguel is developing a discount coupon system and needs a way to apply different discount rates to purchase values.
# Given this problem, create a closure that generates a function capable of calculating the final price with a fixed discount defined by the user.

def discount(discount_percentage):
    def final_value(purchase_value):
        return purchase_value - (purchase_value * (discount_percentage / 100))
    return final_value

purchase_value = float(input('Enter the gross price of the product: '))
discount_percentage = float(input('Enter the desired discount percentage (from 1 to 100): '))
calculate_discount = discount(discount_percentage)
final_price = calculate_discount(purchase_value)
print(f'The final price with discount is: ${final_price}')
