








































nums = []

while len(nums) < 20:
    x = int(input("Enter a number"))
    if x not in nums:
        nums.append(x)
    else:
        print("Duplicate")
        
print("Numbers")
for n in nums:
    print(n)
    
nums.sort()
print("sorted")
for n in nums:
    print(n)