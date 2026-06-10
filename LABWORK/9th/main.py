# Geometry helper functions
import math

def circle_area(radius):
    return math.pi * radius * radius

def circle_perimeter(radius):
    return 2 * math.pi * radius

def square_area(side):
    return side * side

def square_perimeter(side):
    return 4 * side

def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)

# Main loop for running the application continuously
while True:

    # Display figure selection menu
    print("\n===== GEOMETRY CALCULATOR =====")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Exit")

    # Take user's figure choice
    figure = int(input("Enter your choice: "))

    # Exit the application
    if figure == 4:
        print("Thank you for using the application.")
        break

    # Circle calculations
    elif figure == 1:

        # Accept radius
        radius = float(input("Enter radius: "))

        # Validate positive radius
        while radius <= 0:
            print("Radius must be positive.")
            radius = float(input("Enter radius: "))

        # Operation menu loop
        while True:

            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            # Take operation choice
            op = int(input("Enter your choice: "))

            # Calculate area
            if op == 1:
                print("Area of Circle =", circle_area(radius))

            # Calculate perimeter
            elif op == 2:
                print("Perimeter of Circle =", circle_perimeter(radius))

            # Return to figure menu
            elif op == 3:
                break

            # Invalid operation choice
            else:
                print("Invalid choice")

            # Ask user whether to continue with same figure
            again = input(
                "Do you want to perform another operation on the same figure? (Y/N): "
            )

            if again.upper() != "Y":
                break

    # Square calculations
    elif figure == 2:

        # Accept side length
        side = float(input("Enter side: "))

        # Validate positive side
        while side <= 0:
            print("Side must be positive.")
            side = float(input("Enter side: "))

        # Operation menu loop
        while True:

            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = int(input("Enter your choice: "))

            # Calculate area
            if op == 1:
                print("Area of Square =", square_area(side))

            # Calculate perimeter
            elif op == 2:
                print("Perimeter of Square =", square_perimeter(side))

            # Return to figure menu
            elif op == 3:
                break

            # Invalid operation choice
            else:
                print("Invalid choice")

            # Ask for another operation
            again = input(
                "Do you want to perform another operation on the same figure? (Y/N): "
            )

            if again.upper() != "Y":
                break

    # Rectangle calculations
    elif figure == 3:

        # Accept dimensions
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

        # Validate positive dimensions
        while length <= 0 or breadth <= 0:
            print("Length and Breadth must be positive.")
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))

        # Operation menu loop
        while True:

            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = int(input("Enter your choice: "))

            # Calculate area
            if op == 1:
                print("Area of Rectangle =", rectangle_area(length, breadth))

            # Calculate perimeter
            elif op == 2:
                print("Perimeter of Rectangle =", rectangle_perimeter(length, breadth))

            # Return to figure menu
            elif op == 3:
                break

            # Invalid operation choice
            else:
                print("Invalid choice")

            # Ask for another operation
            again = input(
                "Do you want to perform another operation on the same figure? (Y/N): "
            )

            if again.upper() != "Y":
                break

    # Invalid figure choice
    else:
        print("Invalid figure choice")

    # Ask whether user wants to continue using application
    cont = input("Do you want to continue using the application? (Y/N): ")

    if cont.upper() != "Y":
        print("Thank you for using the application.")
        break