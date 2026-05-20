from calculator_impl import Calculator

class CalculatorFactory:
    @staticmethod
    def create_calculator():
        return Calculator()