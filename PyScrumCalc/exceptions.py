class CalcSyntaxError(Exception):
    def __init__(self, msg, info):
        super().__init__(msg, info)

class CalcDivisionByZero(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        