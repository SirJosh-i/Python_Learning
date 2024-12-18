# def shapes(sides):
#     angles = 180 * (sides - 2)
#     print(angles)

# print(shapes(3))    # Triangle = 3 sides equating 180 degrees of total angle.
# print(shapes(4))    # Quadrilateral
# print(shapes(5))    # Pentagon


# Diagonals increment with increasing numbers.
# For triangle: 0, Quadrilateral = +2, Pentagon = +5,....

def findingDiagonals(sides):
    otherThanSides = sides - 1  #Initiation
    totalPossibleSides = (sides * otherThanSides)   # Total number of sides
    pruningRepetition = totalPossibleSides/2    # Cutting out repetitive forming joints
    diagonals = int(pruningRepetition) - sides    # Final diagonals minus the adjacents sides.
    print(diagonals) # Printing out the diagonals 

print("The total number of diagonals in a \033[1mtriangle\033[0m is: ")
print(findingDiagonals(3))  # Triangle
print("The total number of diagonals in a \033[1mquadrilateral\033[0m is: ")
print(findingDiagonals(4))  # Quadrilateral
print("The total number of diagonals in a \033[1mPentagon\033[0m is: ")
print(findingDiagonals(5))  # Pentagon
print("The total number of diagonals in a \033[1mHexagon\033[0m is: ")
print(findingDiagonals(6))  # Hexagon
print("The total number of diagonals in a \033[1mIcositetragon\033[0m is: ")
print(findingDiagonals(24))  # Hexagon