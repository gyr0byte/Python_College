nums = []
n = int(input("How many numbers do you want to enter? "))
for i in range(n):
    num = int(input("Enter a number: "))
    nums.append(num)    
odd_sum = 0
even_sum = 0
for num in nums:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num  
        
print("Sum of odd numbers:", odd_sum)
print("Sum of even numbers:", even_sum)