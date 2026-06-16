
































n = int(input("Enter a number: "))
total = 0

for i in range(3, n+1, 2):
    total += i
    
print("Sum of odd numbers between 2 and", n, "is:", total)
