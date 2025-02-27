# Product look-up using user input, for elements within nested dictionaries to print the product name and price

product_catalog = {

    "SKU123": {
        "name":"Widget A",
        "price":"19.99",
        "quantity":"50"
    },

    "SKU456": {
        "name":"Gadget B",
        "price":"34.99",
        "quantity":"25"
    },

    "SKU789": {
        "name":"Gizmo C",
        "price":"9.99",
        "quantity":"100"
    }

}
# defining the look-up input
sku_lookup = input("SKU to retrieve: ")

# printing the product name and price
print("The price of", product_catalog[sku_lookup]["name"],"is", "$"+product_catalog[sku_lookup]["price"])