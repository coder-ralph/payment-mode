# stacktrek - coding workshop 2 - 24/06/2022

# variables
price_per_item = 50
wholesale_discount_per_item = 5
number_of_discounted_item = 0
subtotal = 0
discount = 0
shipping_fee = 0
total_amount = 0.00

# inputs
customer = input()
item_name = input()
number_of_items = int(input())
mode_of_delivery = input()
mode_of_payment = input()

# if/else
# Only compute of their are items
if number_of_items > 0:
	# Compute the subtotal
	subtotal = price_per_item * number_of_items

# Determine shipping fee
	if (mode_of_payment == "JandT"):
		shipping_fee = 50
	else:
		shipping_fee = 150
		
	# Determine the discount
	number_of_discounted_item = number_of_items - 1
	discount = number_of_discounted_item * wholesale_discount_per_item
	total_amount = subtotal - discount + shipping_fee

# print the results
print("Name:" + customer)
print("Item Name:" + item_name)
print("Number of Items:" + str(number_of_items))
print("Mode of Delivery:" + mode_of_delivery)
print("Mode of Payment:" + mode_of_payment)
print("Total:" + str(total_amount))