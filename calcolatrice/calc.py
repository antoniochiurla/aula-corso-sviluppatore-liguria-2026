from decimal import Decimal
from math import log
from .exchange import ExchangeAPI, ExchangeAPIFactory

class Calc:
    def add(self, adding1, adding2):
        return adding1 + adding2

    def subtract(self, minuend, subtrahend):
        return minuend - subtrahend
    
    def multiply(self, factor1, factor2):
        return factor1 * factor2
    
    def divide(self, dividend, divisor):
        return dividend / divisor
    
    def divide_int(self, dividend, divisor):
        return dividend // divisor
    
    def divide_remainder(self, dividend, divisor):
        return dividend % divisor
    
    def divide_with_remainder(self, dividend, divisor):
        return dividend // divisor, dividend % divisor
    
    def pow(self, base, exponent):
        return base ** exponent
    
    def log(self, x, base):
        return log(x, base)
    
    def exchange(self, amount, from_currency, to_currency):
        exchange_api: ExchangeAPI = ExchangeAPIFactory().create()
        exchange = Decimal(exchange_api.find_exchange(from_currency, to_currency))
        return round(exchange * Decimal(amount), 2)
    
def main():
    pass

if __name__ == '__main__':
    main()
