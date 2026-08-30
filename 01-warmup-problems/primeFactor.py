n = int(input("Enter the Num:"))
factors = []
i = 2
while(i<n):
    if n%i==0:
        factors.append(i)
    i+=1
# print(factors)

# Input list
factors
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True
# Filter primes
prime_numbers = [num for num in factors if is_prime(num)]

print("Prime numbers:", prime_numbers)


