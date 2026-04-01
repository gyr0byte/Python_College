def sum_even(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total
n = int(input("Enter your desired number: "))
sum = sum_even(n)
print(f"The sum of even numbers is {sum}")