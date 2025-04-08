# Add your code here
def calculate_diameter_circle(radius: float) -> float:
    """
    This function calculates the diameter of a circle using the given radius as a positive number greater than zero

    Argument(s):
    - radius is the straight-line distance from the center to any outer point of the circle
    
    Raises:
    - radius cannot be less than 0

    Example syntex:
    calculate_diameter_circle(10) >>> returns value diameter = 20
    
    """
    
    if radius < 0:
        raise ValueError("Error: Radius cannot be negative.")    
    
    circle_radius = radius
    diameter = circle_radius * 2    

    return diameter
