def is_prime(n):
    """Check whether a number is prime or not"""
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


def prime_sequence(number):
    """Return n first primes"""
    for num in range(2, number + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
