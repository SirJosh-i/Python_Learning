# initialArr = [1,2,3,4,5,5,3]
# newArr = []

# for i in initialArr:
#     newArr.append(i)

# print(newArr)
# newArr.pop()
# print(newArr)

arr = [1,3,7,10,15,0,3,5]
target = 18
newArr = []

print("Before entering the loop, array = ",arr)
for i in arr:
    arrOfI = arr.index(i)
    for j in arr:
        sum = i + j
        if sum == target:
            # indexPos = arr.index(i)
            # newArr.append(indexPos)
            newArr.append(sum)
            arr.pop(arrOfI)
            
print("Old Array after popped: ",arr)
print("New Array with target: ", newArr, end="")