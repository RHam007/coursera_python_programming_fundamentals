# Collection of simple functions

def calculate_area(length, width):
    """This function calculates a rectangle's area by multiplying the length by the width"""
    area = length * width
    return area

length = int(input("What is the length of the rectangle: "))
width = int(input("What is the width of the rectangle: "))

area = calculate_area(length,width)
print(area)