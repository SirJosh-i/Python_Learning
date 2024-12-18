import sys

usedIndex = []
arr = [1,3,7,1,10,15,0,3,5,4]
target = 18

for i in arr:
    for j in arr:
        sum = i + j
        if sum == target:
            usedIndex.append(i)
            usedIndex.append(j)
            if i and j == usedIndex:
                continue
            else:
                

print(usedIndex)
