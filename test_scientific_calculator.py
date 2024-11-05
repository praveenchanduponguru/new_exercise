import unittest
from scientific_calculator import sin_function, cos_function, tan_function, sqrt_function, log_function, exp_function, asin_function, acos_function, atan_function, sinh_function, cosh_function, tanh_function

class TestScientificCalculator(unittest.TestCase):

    def test_sin_positive_input(self):
        self.assertAlmostEqual(sin_function(90), 1.0, places=5)

    def test_sin_negative_input(self):
        self.assertAlmostEqual(sin_function(-90), -1.0, places=5)

    def test_sin_zero_input(self):
        self.assertAlmostEqual(sin_function(0), 0.0, places=5)

    def test_sin_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sin_function("hello")

    def test_cos_positive_input(self):
        self.assertAlmostEqual(cos_function(0), 1.0, places=5)

    def test_cos_negative_input(self):
        self.assertAlmostEqual(cos_function(-90), 0.0, places=5)

    def test_cos_zero_input(self):
        self.assertAlmostEqual(cos_function(90), 0.0, places=5)

    def test_cos_non_numeric_input(self):
        with self.assertRaises(TypeError):
            cos_function("hello")

    def test_tan_positive_input(self):
        self.assertAlmostEqual(tan_function(45), 1.0, places=5)

    def test_tan_negative_input(self):
        self.assertAlmostEqual(tan_function(-45), -1.0, places=5)

    def test_tan_zero_input(self):
        self.assertAlmostEqual(tan_function(0), 0.0, places=5)

    def test_tan_non_numeric_input(self):
        with self.assertRaises(TypeError):
            tan_function("hello")

    def test_sqrt_positive_input(self):
        self.assertAlmostEqual(sqrt_function(4), 2.0, places=5)

    def test_sqrt_zero_input(self):
        self.assertAlmostEqual(sqrt_function(0), 0.0, places=5)

    def test_sqrt_negative_input(self):
        with self.assertRaises(ValueError):
            sqrt_function(-4)

    def test_sqrt_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sqrt_function("hello")

    def test_log_positive_input(self):
        self.assertAlmostEqual(log_function(10), 2.302585092994046, places=5)

    def test_log_zero_input(self):
        with self.assertRaises(ValueError):
            log_function(0)

    def test_log_negative_input(self):
        with self.assertRaises(ValueError):
            log_function(-1)

    def test_log_non_numeric_input(self):
        with self.assertRaises(TypeError):
            log_function("hello")

    def test_exp_positive_input(self):
        self.assertAlmostEqual(exp_function(1), 2.71828, places=5)

    def test_exp_zero_input(self):
        self.assertAlmostEqual(exp_function(0), 1.0, places=5)

    def test_exp_non_numeric_input(self):
        with self.assertRaises(TypeError):
            exp_function("hello")

    def test_asin_positive_input(self):
        self.assertAlmostEqual(asin_function(1), 90.0, places=5)

    def test_acos_positive_input(self):
        self.assertAlmostEqual(acos_function(1), 0.0, places=5)

    def test_atan_positive_input(self):
        self.assertAlmostEqual(atan_function(1), 45.0, places=5)

    def test_sinh_positive_input(self):
        self.assertAlmostEqual(sinh_function(1), 1.17520, places=5)

    def test_cosh_positive_input(self):
        self.assertAlmostEqual(cosh_function(1), 1.54308, places=5)

    def test_tanh_positive_input(self):
        self.assertAlmostEqual(tanh_function(1), 0.76159, places=5)

    def test_asin_non_numeric_input(self):
        with self.assertRaises(TypeError):
            asin_function("hello")

    def test_acos_non_numeric_input(self):
        with self.assertRaises(TypeError):
            acos_function("hello")

    def test_atan_non_numeric_input(self):
        with self.assertRaises(TypeError):
            atan_function("hello")

    def test_sinh_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sinh_function("hello")

    def test_cosh_non_numeric_input(self):
        with self.assertRaises(TypeError):
            cosh_function("hello")

    def test_tanh_non_numeric_input(self):
        with self.assertRaises(TypeError):
            tanh_function("hello")

if __name__ == '__main__':
    unittest.main()
