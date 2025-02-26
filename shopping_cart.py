# Functional cart snippet

"""shopping_cart = []
def add_item_to_cart(item):
    shopping_cart.append(item)
    for item in shopping_cart:
        print(item)
    return

item = add_item_to_cart(input("Add which item?: "))"""

# What the worksheet wants:

#initializing the shopping cart
shopping_cart = []

# defining the add_item_to_cart function
def add_item_to_cart(item):
    shopping_cart.append(item)
    return

# simulating user input by hardwiring the add_item_to_cart()
add_item_to_cart("apple")
add_item_to_cart("banana")
add_item_to_cart("milk")

# printing the shopping cart list
print("Shopping Cart:")
for item in shopping_cart:
    print(item)