print("I'm\nlearning\npython\"")

#example 2

whole_number1 = int(input("enter a whole number:"))
whole_number2 = int(input("input asecond whole number:"))
sum_of_whole_numbers = whole_number1 + whole_number2
print(f"The sum of the whole numbers are: {sum_of_whole_numbers}")

#example 3

print((4*3), (4**4))

#example 4

print(f"{"celsius":<10} | {"fahrenheit":<10}")

for celsius in range(0, 101):
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius:<10} | {fahrenheit:<10.1f}")
    
#example 5

total_sum = 0

for i in range(2, 100, 3):
    total_sum += i
print(total_sum)

#example 6

str = "ABGJAFAUANHAGJA"
countA = 0
for char in str:
    if char == 'A':
        countA += 1
        
print(countA)
        