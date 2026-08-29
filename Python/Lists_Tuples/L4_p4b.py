# Write a program to sum a list with 4 numbers.
# Agar 4 numbers user se input lene hain:

numbers = []

for i in range(4):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Sum =", sum(numbers))

