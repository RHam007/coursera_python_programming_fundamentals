# Hungry?  Have a sandwich making app! Context examples included below
def make_sandwich(bread_type, filling, cheese = "none", toasted = False):
    """
    App will make your sandwich based on your selections!

    Arguements:
    bread_type:  the bread you want to use (string, required)
    filling: what you want to have in your sandwich (string, required)
    cheese: what dairy you want (string, optional, default = None)
    toasted: is your sandwich toasted? (boolean, optional, defaul = False)

    Expected output:
    make_sandwich("wheat", "turkey", "cheddar", True) >>>> "Making a toasted wheat sandwich with turkey and cheddar cheese."

    """
    if toasted == True and cheese != "none":
        print(f"Making a toasted {bread_type} sandwich with {filling} and {cheese} cheese.")
    elif toasted == True and cheese == "none":
        print(f"Making a toasted {bread_type} sandwich with {filling}.")
    elif toasted == False and cheese != "none":
        print(f"Making a {bread_type} sandwich with {filling} and {cheese} cheese.")
    else:
        print(f"Making a {bread_type} sandwich with {filling}.")
    return

# usage examples
make_sandwich("wheat", "turkey", "cheddar", True)
make_sandwich("rye", "ham")
