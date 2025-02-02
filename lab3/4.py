def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter(numbers):
    return [num for num in numbers if prime(num)]
nums = list(map(int, input("write numbers with space: ").split()))
print("prime num:", filter(nums))
