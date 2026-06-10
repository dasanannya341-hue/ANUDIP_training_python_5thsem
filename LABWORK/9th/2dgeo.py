# geometry.py

# Value of pi used in circle calculations
pi = 3.14

# Function to calculate area of a circle
def circle_area(radius):
    return pi * radius * radius

# Function to calculate perimeter (circumference) of a circle
def circle_perimeter(radius):
    return 2 * pi * radius

# Function to calculate area of a square
def square_area(side):
    return side * side

# Function to calculate perimeter of a square
def square_perimeter(side):
    return 4 * side

# Function to calculate area of a rectangle
def rectangle_area(length, breadth):
    return length * breadth

# Function to calculate perimeter of a rectangle
def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)