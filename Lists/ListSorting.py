numbers = []

n = int(input("Enter list size: "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

numbers.sort()

print("Sorted list:", numbers)