# Binary Search

arr = [1,2,3,4,5,6,7]
skipArr = []
target = 1
count = 0

startIndex = 0
endIndex = (len(arr)-1)

while startIndex <= endIndex:
    midPointIndex = int((startIndex + endIndex) / 2)
    if arr[midPointIndex] == target:
        print("Match found after " + str(count) + " iterations")
        break
    
    elif target > arr[midPointIndex]:
        count+=1
        startIndex = midPointIndex + 1
        print(arr[startIndex],arr[midPointIndex])
    elif target < arr[midPointIndex]:
        count+=1
        endIndex = midPointIndex - 1