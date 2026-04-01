def sum_odd(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total
n = int(input("Enter your desired number: "))
sum = sum_odd(n)
print(f"The sum of odd numbers is {sum}")