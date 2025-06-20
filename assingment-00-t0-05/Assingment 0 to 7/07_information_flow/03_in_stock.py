# # Function to check the stock of a given fruit
# def num_in_stock(fruit):
#     inventory = {
#         "apple": 500,
#         "banana": 300,
#         "pear": 1000,
#         "orange": 250,
#         "mango": 700
#     }
#     return inventory.get(fruit.lower(), 0)  # Return stock count or 0 if not found

# def main():
#     # Prompt the user for input
#     fruit = input("Enter a fruit: ").strip()

#     # Get the number of fruit in stock
#     stock = num_in_stock(fruit)

#     # Print appropriate message based on stock availability
#     if stock > 0:
#         print("This fruit is in stock! Here is how many:")
#         print(stock)
#     else:
#         print("This fruit is not in stock.")

# # Required line to run the program
# if __name__ == '__main__':
#     main()
    
    
    
    
    
    
def main():
	fruit : str = input("Enter a fruit: ")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("This fruit is not in stock.")
	else:
		print("This fruit is in stock! Here is how many:")
		print(stock)

# There is no need to edit code beyond this point

def num_in_stock(fruit):
	"""
	This function returns the number of fruit Sophia has in stock.
	"""
	if fruit == 'apple':
		return 2
	if fruit == 'durian':
		return 4
	if fruit == 'pear':
		return 1000
	else:
		# this fruit is not in stock.
		return 0


if __name__ == '__main__':
    main()    