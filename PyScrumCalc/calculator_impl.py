from interfaces import ICalculator
from exceptions import CalcDivisionByZero, CalcSyntaxError

class Calculator(ICalculator):
    def __init__(self):
        # Inizializzazione memoria: '=' memorizza sempre l'ultimo risultato
        self._variables = {self.last_value_variable: 0.0}

    def get_variables(self) -> dict:
        return self._variables

    @staticmethod
    def _separate_elements(expression: str) -> list[str]:
        """
        Restituisce una lista contenente le stringhe che rappresentano gli elementi dell'espressione
        """
        return expression.split(" ")
    
    @staticmethod
    def _is_operator(str_value: str) -> bool:
        """
        Restituisce True se str_value contiene un numero
        altrimenti restituisce False 
        """
        return str_value in Calculator.operators
    
    @staticmethod
    def _is_assignment_sign(str_value: str) -> bool:
        """
        Restituisce True se str_value contiene il simbolo = (uguale)
        altrimenti restituisce False 
        """
        return str_value == "="
    
    @staticmethod
    def _is_number(str_value: str) -> bool:
        """
        Restituisce True se str_value contiene un numero
        altrimenti restituisce False 
        """
        try:
            float(str_value)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def _is_variable_name(str_value: str) -> bool:
        """
        Restituisce True se str_value contiene un nome valido di variabile
        deve iniziare per una lettera maiuscola o minuscola e contenere solo lettere o cifre
        """
        return len(str_value) > 0 and str_value[0].isalpha() and str_value.isalnum() or str_value == Calculator.last_value_variable
    
    @staticmethod
    def _parse_number(str_number: str) -> float:
        """
        Converte la stringa in un numero float
        """
        return float(str_number)

    def get_variable(self, name: str) -> float:
        """
        ISTRUZIONI:
        Restituire il valore  della variabile con il nome fornito
        Se la variabile non esiste va restituito 0.0
        """
        return float(self._variables.get(name, 0.0))

    def set_variable(self, name: str, value: float):
        """
        ISTRUZIONI:
        Aggiungere la variabile con il valore fornito
        Se la variabile esiste già va sostituita
        Restituisce il valore assegnato alla variabile
        """
        self._variables[name] = value
        return value

    @staticmethod
    def sum(add1: float, add2: float) -> float:
        """
        ISTRUZIONI:
        Restituire il risultato della somma dei due parametri
        """
        return add1 + add2

    @staticmethod
    def percent(value: float, perc: float) -> float:
        """
        ISTRUZIONI:
        Restituire il risultato della percentuale dei due parametri
        """
        return value * perc / 100

    @staticmethod
    def diff(sub1: float, sub2: float) -> float:
        """
        ISTRUZIONI:
        Restituire il risultato della differenza tra i due parametri
        """
        return sub1-sub2

    @staticmethod
    def mult(mult1: float, mult2: float) -> float:
        """
        ISTRUZIONI:
        Restituire il risultato del prodotto dei due parametri
        """
        return mult1*mult2

    @staticmethod
    def div(div1: float, div2: float) -> float:
        """
        ISTRUZIONI:
        Restituire il risultato della divisione tra i due parametri
        """
        if div2 == 0:
            raise CalcDivisionByZero("Divisione per zero non consentita!!!")
        return div1/div2
    

    @staticmethod
    def _is_assignment_with_calculation(elements: list[str]) -> bool:
        """
        Verifica se la lista rappresenta un'assegnazione con calcolo
        nel formato:
            variabile = operando operatore operando

        Esempi validi:
            ["a", "=", "5", "+", "1"]
            ["a", "=", "b", "+", "1"]
            ["a", "=", "5", "+", "c"]
        """

        if len(elements) != 5:
            return False

        variable, assign, left, operator, right = elements

        valid_operators = Calculator._is_operator
        valid_variable = Calculator._is_variable_name

        return (
            valid_variable(variable)
            and Calculator._is_assignment_sign(assign)
            and (Calculator._is_number(left) or valid_variable(left))
            and valid_operators(operator)
            and (Calculator._is_number(right) or valid_variable(right))
        )
    
    @staticmethod
    def _is_assignment(elements: list[str]) -> bool:
        
        return (
        len(elements) == 3
        and Calculator._is_variable_name(elements[0])
        and Calculator._is_assignment_sign(elements[1])
        and (
            Calculator._is_number(elements[2])
            or Calculator._is_variable_name(elements[2])
        )
    )
    
    @staticmethod
    def _is_calculation(elements: list[str]) -> bool:
        
        return(
            len(elements) == 3
            and (Calculator._is_number(elements[0]) or Calculator._is_variable_name(elements[0]))
            and Calculator._is_operator(elements[1])
            and (Calculator._is_number(elements[2]) or Calculator._is_variable_name(elements[2]))
        )
    
    def _assignment_or_calculation(self,elements: list[str]) -> float:
        if self._is_assignment(elements):
            if self._is_variable_name(elements[2]):
                value = self.get_variable(elements[2])
            else:
                value = self._parse_number(elements[2])
            self.set_variable(elements[0], value)
        elif self._is_calculation(elements):
            value = self._calculation(elements)
        self.set_variable(self.last_value_variable, value)
        return value

   
    def _assignment_with_calculation(self,elements: list[str]) -> float:
         
         if len(elements) != 5:
            raise CalcSyntaxError(" ".join(elements), "assegnazione con calcolo non valida")

         if not Calculator._is_variable_name(elements[0]):
            raise CalcSyntaxError(" ".join(elements), "nome variabile non valido")

         if not Calculator._is_assignment_sign(elements[1]):
            raise CalcSyntaxError(" ".join(elements), "segno = mancante")

         if not (
            Calculator._is_number(elements[2])
            or Calculator._is_variable_name(elements[2])
        ):
            raise CalcSyntaxError(" ".join(elements), "primo valore non valido")

         if not Calculator._is_operator(elements[3]):
            raise CalcSyntaxError(" ".join(elements), "operatore non valido")

         if not (
            Calculator._is_number(elements[4])
            or Calculator._is_variable_name(elements[4])
        ):
            raise CalcSyntaxError(" ".join(elements), "secondo valore non valido")

         variable_name = elements[0]

         result = self._calculation(elements[2:])
         self.set_variable(variable_name, result)

         return result

    def _calculation(self, elements: list[str]):
         first_value = elements[0]
         operator = elements[1]
         second_value = elements[2]
         if Calculator._is_number(first_value):
           num1 = Calculator._parse_number(first_value)
         else:
           num1 = self.get_variable(first_value)

         if Calculator._is_number(second_value):
           num2 = Calculator._parse_number(second_value)
         else:
           num2 = self.get_variable(second_value)

         result = Calculator.operators[operator](num1, num2)

         return result
    
    @staticmethod
    def _is_single_value(elements: list[str]) -> bool:
        """
        Restituisce True se la lista contiene
        un solo valore numerico
        """
        return len(elements) == 1 and Calculator._is_number(elements[0])
        
    def _is_variable(self, elements: list[str]) -> bool:
        if len(elements) != 1:
            return False
        return self._is_variable_name(elements[0])
    
    def _single_value_or_variable(self, elements: list[str]) -> float:
        token = elements[0]
        return float(token) if Calculator._is_number (token) else self.get_variable(token)
    
    operators = {
        '+': sum,
        '-': diff,
        '*': mult,
        '/': div,
        '%': percent,
    }

    def evaluate(self, expression: str) -> float:
        """
        ISTRUZIONI:
        1. Gestire l'assegnazione (es. 'x = 5 + 2')
        2. Sostituire le variabili nell'espressione con i loro valori
        3. Calcolare il risultato delle 4 operazioni (+ - * /)
        4. Aggiornare sempre la variabile '=' con il risultato finale
        5. Lanciare ValueError per divisione per zero o sintassi errata
        """
        elements = self._separate_elements(expression)
        result = 0.0
        match len(elements):
            case 1: # single value or variable
                result = self._single_value_or_variable(elements)
            case 2: # error
                raise CalcSyntaxError(expression, "non interpretata correttamente!!!")
            case 3: # variable assignment with single value or calculation
                result = self._assignment_or_calculation(elements)
            case 4: # error
                raise CalcSyntaxError(expression, "non interpretata correttamente!!!")
            case 5: # variable assignment with calculation
                result = self._assignment_with_calculation(elements)
            case _:
                raise CalcSyntaxError(expression, "non interpretata correttamente!!!")
        self.set_variable(self.last_value_variable, result)
        return result
    
