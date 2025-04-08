import pandas as pd

grocery_list_df = pd.read_csv('grocery_list.csv')
grocery_list = grocery_list_df['item'].tolist()

print(grocery_list)

items_to_add = ['Kiwis', 'Raspberries']

for item in items_to_add:
    grocery_list.append(item)

print(grocery_list)

new_item = input("Enter an item to add to your grocery list: ")
grocery_list.append(new_item)

print("Updated list:", grocery_list)

grocery_list.append("Cinnamon")
grocery_list.append("Paprika")

print("\nYour Updated List:") # \n creates a new line
print(grocery_list)

grocery_list.remove("Eggs")
grocery_list.remove("Apples")

print("\nYour Updated List:") # \n creates a new line
print(grocery_list)