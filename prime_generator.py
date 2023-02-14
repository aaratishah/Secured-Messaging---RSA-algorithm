import random
import math

def prime_check(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def get_random_prime(lower, upper):
    potential_prime = random.randint(lower, upper)
    while not prime_check(potential_prime):
        potential_prime = random.randint(lower, upper)
    return potential_prime