import time

print("Enter the number: ", end="")
num = int(input())

if num % 2 == 0:
    print("Processing Even Number...")
    time.sleep(1.4)
    for n in range(1,num+1):
        if num % n == 0:
            print(n)
else:
    print("Processing Odd Number...")
    time.sleep(1.4)
    for n in range(1,num+1,2):
        if num % n == 0:
            print(n)