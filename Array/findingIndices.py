import sys

arr = [1,3,7,10,15,0,3,5]
target = 18

for i in arr:
    for j in arr:
        if i + j == target:
            print("Numbers in Array : ",i, j)
            print("Index Position   : ", arr.index(i), arr.index(j))
            print("------------------------")

