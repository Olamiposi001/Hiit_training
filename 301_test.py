number = (input("Enter an Integer: "))

sum_of_number = 0
product_of_number = 1

#using for loop to get the sum and product of the digits in an interger
for n in number:
    digits = int(n)
    sum_of_number += digits
    product_of_number *= digits
    
print('\n', number, "digit sum is", sum_of_number, "and digit product is", product_of_number)





str = "ABCDEFGHIABCDJKLMNOPABCD"

count_A = 0

for A in str:
    if A == "A":
        count_A += 1
        
print(count_A)