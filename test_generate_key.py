# Importing the unittest module from the Python Standard Library
import unittest
# Importing the generate_key module
from generate_key import *

# Defining the TestRSAFunctions class as a subclass of unittest.TestCase
class TestRSA(unittest.TestCase):

    # Testing the get_gcd function
    def test_get_gcd(self):
        self.assertEqual(gcd(24, 60), 12)
        self.assertEqual(gcd(10, 15), 5)
        self.assertEqual(gcd(55, 121), 11)

# Testing the mod_inverse function
    def test_mod_inverse(self):
        self.assertEqual(mod_inverse(7, 26), 15)
        self.assertEqual(mod_inverse(5, 26), 21)

    # Testing the encrypt_msg function
    def test_encrypt_msg(self):
        public_key = (23707, 29)
        message = "HELLO"
        encrypted_msg = encrypt(message, public_key)
        self.assertEqual(encrypted_msg, "丰䱈ՑՑದ")

    # Testing the decrypt_msg function
    def test_decrypt_msg(self):
        private_key = (151, 157, 8069)
        cipher_text = "丰䱈ՑՑದ"
        message = decrypt(cipher_text, private_key)
        self.assertEqual(message, "HELLO")

        private_key = (17, 19, 187)
        cipher_text = "AFLANSFS2"
        message = decrypt(cipher_text, private_key)
        self.assertEqual(message, "\x1bĺ\x13\x1bG\x1aĺ\x1a2")


if __name__ == "__main__":
    unittest.main()
