m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))

if n > m:
    temp = m
    m = n
    n = temp
else:
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n

print(f"Greatest common divisor is {n}")
