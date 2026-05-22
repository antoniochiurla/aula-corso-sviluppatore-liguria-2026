class CalcSyntaxError(SyntaxError):
    def __init__(self, msg, info):
        super().__init__(msg, info)

class CalcDivisionByZero(ZeroDivisionError):
    def __init__(self, *args):
        super().__init__(*args)
        