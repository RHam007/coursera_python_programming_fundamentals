"""
This is a code snippet to illistrate how the feature works.

To use this snippet in your IDE (should work with most, but built/tested in MS Studio Code):

 - Navigate to File > Preferences > Configure user Snippets
 - Scroll/Search for "python"
 - python.json will open
 - replace all content with the following code snippet (yes, even delete the existing {} in the python.json)
 - Save the python.json file
 - Open main.py (or whatever file you want to use the snippet in)
 - type 'calc_area' (IDE should prompt for code completion - use TAB to generate the template)
 - Cursor should appear at the first variable 'length'
 - Enter any positive int
 - Use TAB or mouse navigate to the next variable
 - Enter any positive int
 - Run the app via terminal and verify the results/output
"""

{
    "calculate_area": {
        "prefix": "calc_area",
        "body": [
            "def calculate_area(length, width):",
            "  \"\"\"Calculates the area of a rectangle.\"\"\"",
            "  # Calculate the area",
            "  area = length * width",
            "  ",
            "  # Output the area",
            "  return area",
            "",
            "# Example usage",
            "length = $1",
            "width = $2",
            "print(calculate_area(length, width))"
        ],
        "description": "Calculate the area of a rectangle"
    }
}