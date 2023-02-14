# Importing the unittest module from the Python Standard Library
import unittest
# Importing the prime_generator module
from prime_generator import *

# Defining the TestGenerateRandomPrime class as a subclass of unittest.TestCase
class TestGenerateRandomPrime(unittest.TestCase):
    # Defining the test_generate_random_prime method to test the generate_random_prime function
    def test_generate_random_prime(self):
        # Defining the start and end values for generating a random prime number
        start, end = 1, 20
        # Call generate_random_prime and store the result in a variable
        result = get_random_prime(start, end)
        # Check that the result is within the specified range
        self.assertTrue(start <= result <= end)
        # Check that the result is a prime number using the is_prime function
        self.assertTrue(prime_check(result))

# The main function is executed only when the module is run as a standalone program
if __name__ == '__main__':
    # Calling the unittest.main function to run the tests defined in the TestGenerateRandomPrime class
    unittest.main()
