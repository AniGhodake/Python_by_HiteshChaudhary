def is_prime(num):
    if num < 2: return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


def print_primes(limit):
    count = 0
    num = 2
    while count < limit:
        if is_prime(num):
            print(num, end = " ")
            count = count + 1
        num = num + 1

n = int(input("Enter the value of n: "))
print_primes(n)