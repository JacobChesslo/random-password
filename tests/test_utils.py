import unittest
import random
import string
from password.utils import to_int, to_bool


class TestToInt(unittest.TestCase):
    def test_bool_to_bool(self):
        self.assertTrue(to_bool(True))
        self.assertFalse(to_bool(False))

    def test_str_to_bool(self):
        self.assertTrue(to_bool('true'))
        self.assertTrue(to_bool('TRUE'))
        self.assertTrue(to_bool('True'))
        self.assertFalse(to_bool('false'))
        self.assertFalse(to_bool('FALSE'))
        self.assertFalse(to_bool('False'))

    def test_raise_str_to_bool(self):
        test_cases = [
            'this is not a bool',
            'test1',
            'test2',
            'test3'
        ]
        for case in test_cases:
            with self.assertRaises(TypeError):
                to_bool(case)

    def test_raise_other_to_bool(self):
        test_cases = [
            object(),
            str(),
            list(),
            int(),
            float(),
            1,
            3.1415,
            [True, True, False],
            [True]
        ]
        for case in test_cases:
            with self.assertRaises(TypeError):
                to_bool(case)


class TestToBool(unittest.TestCase):
    def test_int_to_int(self):
        test_cases = [random.randint(-1000, 1000) for _ in range(100)]
        for case in test_cases:
            self.assertEqual(to_int(case), case)

    def test_float_to_int(self):
        test_cases = [float(random.randint(-1000, 1000)) for _ in range(100)]
        for case in test_cases:
            self.assertEqual(to_int(case), case)

    def test_raise_float_to_int(self):
        test_cases = [random.random() + 0.01 for _ in range(100)]
        for case in test_cases:
            with self.assertRaises(TypeError):
                to_int(case)

    def test_str_to_int(self):
        test_cases = [str(random.randint(-1000, 1000)) for _ in range(100)]
        for case in test_cases:
            self.assertEqual(int(case), to_int(case))

    def test_raise_str_to_int(self):
        test_cases = [
            ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 100))) for _ in range(100)
        ]
        for case in test_cases:
            with self.assertRaises(TypeError):
                to_int(case)

    def test_array_to_int(self):
        test_cases = [[random.randint(-1000, 1000)] for _ in range(100)]
        for case in test_cases:
            self.assertEqual(case[0], to_int(case))

    def test_raise_array_to_int(self):
        test_cases = [
            [random.randint(-1000, 1000) for _ in range(1, 100)] for _ in range(100)
        ]
        for case in test_cases:
            with self.assertRaises(TypeError):
                to_int(case)

    def test_raise_other_to_int(self):
        test_cases = [
            object(),
            str(),
            list(),
            [1, 2, 3],
        ]
        for case in test_cases:
            with self.assertRaises(TypeError):
                to_int(case)


if __name__ == '__main__':
    unittest.main()
