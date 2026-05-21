import unittest
from calculator_impl import Calculator
from exceptions import CalcSyntaxError, CalcDivisionByZero

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # --- SPRINT 1: OPERAZIONI BASE & ULTIMO RISULTATO ---

    def test_inner_separate_elements(self):
        self.assertTrue(self.calc._separate_elements("a"), ["a"])
        self.assertTrue(self.calc._separate_elements("a b"), ["a", "b"])
        self.assertTrue(self.calc._separate_elements("a b"), ["a", "b"])
        self.assertTrue(self.calc._separate_elements("a b c"), ["a", "b", "c"])
        self.assertTrue(self.calc._separate_elements(" 1 + 2 "), ["1", "+", "2"])
        self.assertTrue(self.calc._separate_elements("a = 3"), ["a", "=", "3"])
        self.assertTrue(self.calc._separate_elements("a = 3 + 5"), ["a", "=", "3", "+", "5"])
        self.assertTrue(self.calc._separate_elements("a = 3"), ["a", "=", "3"])

    def test_inner_is_operator(self):
        self.assertTrue(self.calc._is_operator("+"))
        self.assertTrue(self.calc._is_operator("-"))
        self.assertTrue(self.calc._is_operator("*"))
        self.assertTrue(self.calc._is_operator("/"))
        self.assertFalse(self.calc._is_operator("="))
        self.assertFalse(self.calc._is_operator("a"))
        self.assertFalse(self.calc._is_operator("5"))

    def test_inner_is_assignment_sign(self):
        self.assertTrue(self.calc._is_operator("="))
        self.assertFalse(self.calc._is_operator("+"))
        self.assertFalse(self.calc._is_operator("-"))
        self.assertFalse(self.calc._is_operator("*"))
        self.assertFalse(self.calc._is_operator("/"))
        self.assertFalse(self.calc._is_operator("a"))
        self.assertFalse(self.calc._is_operator("5"))

    def test_inner_is_number(self):
        self.assertTrue(self.calc._is_number("1"))
        self.assertTrue(self.calc._is_number("1.0"))
        self.assertTrue(self.calc._is_number("0.5"))
        self.assertFalse(self.calc._is_number("a"))
        self.assertFalse(self.calc._is_number("1a"))
        self.assertFalse(self.calc._is_number("1a3"))
        self.assertFalse(self.calc._is_number("a13"))
    
    def test_inner_is_variable_name(self):
        self.assertTrue(self.calc._is_variable_name("a"))
        self.assertTrue(self.calc._is_variable_name("A"))
        self.assertTrue(self.calc._is_variable_name("ab"))
        self.assertTrue(self.calc._is_variable_name("aB1"))
        self.assertTrue(self.calc._is_variable_name("a54"))
        self.assertTrue(self.calc._is_variable_name("Z4av"))
        self.assertFalse(self.calc._is_variable_name("1a"))
        self.assertFalse(self.calc._is_variable_name("-a"))

    def test_is_assignment_with_calculation(self):
        self.assertTrue(self.calc._is_assignment_with_calculation(["a", "=", "5", "+", "1"]))
        self.assertTrue(self.calc._is_assignment_with_calculation(["a", "=", "b", "+", "1"]))
        self.assertTrue(self.calc._is_assignment_with_calculation(["a", "=", "5", "+", "c"]))

    def test_is_assignment(self):
        self.assertTrue(self.calc._is_assignment_with_calculation(["a", "=", "5"]))
        self.assertTrue(self.calc._is_assignment_with_calculation(["a", "=", "b"]))

    def test_is_calculation(self):
        self.assertTrue(self.calc._is_assignment_with_calculation(["a", "+", "5"]))
        self.assertTrue(self.calc._is_assignment_with_calculation(["a", "/", "b"]))

    def test_is_single_value(self):
        self.assertTrue(self.calc._is_single_value(["5"]))
        self.assertTrue(self.calc._is_single_value(["42"]))
        self.assertTrue(self.calc._is_single_value(["27.6"]))

    def test_is_variable(self):
        self.assertTrue(self.calc._is_variable(["a"]))
        self.assertTrue(self.calc._is_variable(["a42"]))
        self.assertTrue(self.calc._is_variable(["cs"]))

    def test_inner_parse_number(self):
        self.assertEqual(self.calc._parse_number("1"), 1.0)
        self.assertEqual(self.calc._parse_number("1.0"), 1.0)
        self.assertEqual(self.calc._parse_number("0.5"), 0.5)
    
    def test_inner_addition(self):
        self.assertEqual(self.calc.sum(10, 5), 15.0)

    def test_inner_subtraction(self):
        self.assertEqual(self.calc._diff(10, 4), 6.0)

    def test_inner_multiplication(self):
        self.assertEqual(self.calc._mult(3, 4), 12.0)

    def test_inner_division(self):
        self.assertEqual(self.calc._div(10, 2), 5.0)

    def test_inner_division_by_zero(self):
        with self.assertRaises(CalcDivisionByZero):
            self.calc._div(10, 0)

    def test_basic_addition(self):
        self.assertEqual(self.calc.evaluate("10 + 5"), 15.0)

    def test_basic_subtraction(self):
        self.assertEqual(self.calc.evaluate("10 - 4"), 6.0)

    def test_basic_multiplication(self):
        self.assertEqual(self.calc.evaluate("3 * 4"), 12.0)

    def test_basic_division(self):
        self.assertEqual(self.calc.evaluate("10 / 2"), 5.0)

    def test_assignments_value(self):
        self.calc.set_variable("a", 0.0)
        self.assertEqual(self.calc.evaluate("a = 10"), 10.0)
        self.assertEqual(self.calc.get_variable("a"), 10.0)

    def test_assignments_addiction(self):
        self.calc.set_variable("a", 0.0)
        self.assertEqual(self.calc.evaluate("a = 10 + 2"), 12.0)
        self.assertEqual(self.calc.get_variable("a"), 12.0)

    def test_assignments_subtract(self):
        self.calc.set_variable("a", 0.0)
        self.assertEqual(self.calc.evaluate("a = 10 - 2"), 8.0)
        self.assertEqual(self.calc.get_variable("a"), 8.0)

    def test_assignments_multiply(self):
        self.calc.set_variable("a", 0.0)
        self.assertEqual(self.calc.evaluate("a = 10 * 2"), 20.0)
        self.assertEqual(self.calc.get_variable("a"), 20.0)

    def test_assignments_division(self):
        self.calc.set_variable("a", 0.0)
        self.assertEqual(self.calc.evaluate("a = 10 / 2"), 5.0)
        self.assertEqual(self.calc.get_variable("a"), 5.0)

    def test_last_result_usage(self):
        self.calc.evaluate("10 + 10") # result 20
        self.assertEqual(self.calc.evaluate(f"{self.calc.last_value_variable} + 5"), 25.0)

    def test_calc_syntax_error(self):
        with self.assertRaises(CalcSyntaxError) as context:
            self.calc.evaluate("10 +")
        with self.assertRaises(CalcSyntaxError) as context:
            self.calc.evaluate("10 10")
        with self.assertRaises(CalcSyntaxError) as context:
            self.calc.evaluate("= 10 + 10")
        with self.assertRaises(CalcSyntaxError) as context:
            self.calc.evaluate("= = 10 + 10")
        with self.assertRaises(CalcSyntaxError) as context:
            self.calc.evaluate("a = 10 x 10")

    def test_division_by_zero(self):
        with self.assertRaises(CalcDivisionByZero):
            self.calc.evaluate("10 / 0")

    # --- SPRINT 2: VARIABILI E MEMORIA ---

class TestCalculatorWithVariables(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_inner_variable_assignment(self):
        # L'assegnazione deve restituire il valore assegnato
        self.assertEqual(self.calc.evaluate("pippo = 50"), 50.0)
        self.assertIn("pippo", self.calc.get_variables())

    def test_inner_variable_usage(self):
        self.calc.evaluate("x = 10")
        self.assertEqual(self.calc.evaluate("x * 2"), 20.0)


    def test_variable_assignment(self):
        # L'assegnazione deve restituire il valore assegnato
        self.assertEqual(self.calc.evaluate("pippo = 50"), 50.0)
        self.assertIn("pippo", self.calc.get_variables())

    def test_variable_assignment_by_expression(self):
        # L'assegnazione deve restituire il valore assegnato
        self.assertEqual(self.calc.evaluate("pippo = 50 * 10"), 500.0)
        self.assertIn("pippo", self.calc.get_variables())
        self.assertEqual(self.calc.get_variable("pippo"), 500.0)

    def test_variable_usage(self):
        self.calc.evaluate("x = 10")
        self.assertEqual(self.calc.evaluate("x * 2"), 20.0)

    def test_complex_variable_usage(self):
        self.calc.evaluate("a = 5")
        self.calc.evaluate("b = 10")
        self.assertEqual(self.calc.evaluate("a + b"), 15.0)

if __name__ == "__main__":
    unittest.main()