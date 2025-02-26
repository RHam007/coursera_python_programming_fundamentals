# Functional cart snippet

"""shopping_cart = []
def add_item_to_cart(item):
    shopping_cart.append(item)
    for item in shopping_cart:
        print(item)
    return

item = add_item_to_cart(input("Add which item?: "))"""

# What the worksheet wants:

shopping_cart = []
def add_item_to_cart(item):
    shopping_cart.append(item)
    return

add_item_to_cart("apple")
add_item_to_cart("banana")
add_item_to_cart("milk")

print("Shopping Cart:")
for item in shopping_cart:
    print(item)