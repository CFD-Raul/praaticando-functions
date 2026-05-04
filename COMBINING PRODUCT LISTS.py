# Clara is managing her store's inventory and received two separate lists: one containing product names and another with their respective prices.
# To make organization easier, she needs to combine these lists so that each product is associated with its price.

# Create a program that joins the lists and displays the result in the format product: price

products_for_sale = input('Enter the product names separated by commas: ').split(',')
product_prices = input('Enter the product prices separated by commas: ').split(',')
priced_products = '\n'.join(f'{n.strip()} : {p.strip()}' for n, p in zip(products_for_sale, product_prices))
print(priced_products)