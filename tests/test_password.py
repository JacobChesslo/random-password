import unittest
import random
from password.password import Password


class TestPassword(unittest.TestCase):
    def test_init(self):
        test_object = Password()
        self.assertEqual(0, len(test_object.__dict__))
        with self.assertRaises(TypeError):
            test_object = Password(1, 2, 3, 'a', 'b', 'c')

    def test_save_requirements(self):
        nums = 20
        lengths = [random.randint(1, 100) for _ in range(nums)]
        numbers = [random.choice([True, False]) for _ in range(nums)]
        lowercases = [random.choice([True, False]) for _ in range(nums)]
        uppercases = [random.choice([True, False]) for _ in range(nums)]
        symbols = [random.choice([True, False]) for _ in range(nums)]
        for num, (length, number, lowercase, uppercase, symbol) in enumerate(
                zip(lengths, numbers, lowercases, uppercases, symbols)):
            Password._save_requirements(length=length, numbers=number, lowercase=lowercase, uppercase=uppercase,
                                        symbols=symbol)
            self.assertEqual(length, Password.length)
            self.assertEqual(number, Password.numbers)
            self.assertEqual(lowercase, Password.lowercase)
            self.assertEqual(uppercase, Password.uppercase)
            self.assertEqual(symbol, Password.symbols)

    def test_gather_requirements(self):
        pass

    #TODO Finish tests


if __name__ == '__main__':
    unittest.main()
