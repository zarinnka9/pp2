def isprime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
numbers = [2, 3, 4, 7, 8, 12, 13, 14, 15, 17]
prime_numbers = list(filter(lambda x: isprime(x), numbers))

print("Prime numbers:", prime_numbers)