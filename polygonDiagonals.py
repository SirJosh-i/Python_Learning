### Below is the pre-test version.

# inputArr = []

# print("Enter the number of sides of the shape you decide: ")
# sides = int(input())
# arrInput = sides - 1

# inputArr.append(arrInput)

# finalArr = len(inputArr)

# for i in finalArr:

### The program below works.

print("Enter the number of sides of the shape you decide: ")
sides = int(input())

n = sides - 1
possibleSides = sides * n    # Total number of possible reach with repetition.
print("Total possible sides of each angle is: ", possibleSides)

for i in range(1, (sides+1)):   # From 1 to (sides + 1)
    possibleSides = possibleSides - i
    diagonals = possibleSides
print(diagonals)