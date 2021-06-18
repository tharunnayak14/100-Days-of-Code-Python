import math


def is_prime(num):
    if num == 1 or num == 0:
        return False
    prime_no = True
    for i in range(2, round(math.sqrt(num) + 1)):
        if num % i == 0:
            prime_no = False
    return prime_no



for i in range(1, 100):
    if is_prime(i):
        print(f"{i} prime")
