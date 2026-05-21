from decimal import Decimal

import pytest

from .calc import Calc
from .exchange import set_implementation

calc = Calc()

def test_calc_add():
    assert 10 == calc.add(5, 5)
    assert 0 == calc.add(0, 0)
    assert 5 == calc.add(7, -2)

def test_calc_subtract():
    assert 0 == calc.subtract(5, 5)

def test_calc_multiply():
    assert 10 == calc.multiply(2, 5)

def test_calc_divide():
    assert 5 == calc.divide(10, 2)
    assert 2.5 == calc.divide(10, 4)
    assert 3.3333333333333335 == calc.divide(10, 3)

def test_cal_divide_int():
    assert 3 == calc.divide_int(10, 3)
    assert 3 == calc.divide_int(10.5, 3.2)

def test_calc_divide_remainder():
    assert 1 == calc.divide_remainder(10, 3)

def test_calc_divide_with_remainder():
    quotient, remainder = calc.divide_with_remainder(10, 3)
    assert quotient == 3
    assert remainder == 1

def test_calc_pow():
    assert 27 == calc.pow(3, 3)
    assert 3 == calc.pow(27, 1 / 3)

def test_calc_log():
    assert 3.0000000000000004 == calc.log(125, 5)
    assert 3 == round(calc.log(125, 5))

def test_calc_exchange():
    set_implementation("Test")

    from_currencies = {
        'USD': Decimal("1.16"),
        "AUD": Decimal("1.8"),
        "YEN": Decimal("10.5"),
        "CHF": Decimal("0.89"),
    }

    for from_currency in from_currencies:
        result = Decimal(calc.exchange(Decimal("100.16"), from_currency, "EUR"))
        expected = Decimal(round(Decimal(from_currencies[from_currency]) * Decimal("100.16"),2))
        print(from_currency, result, expected)
        assert result == expected

