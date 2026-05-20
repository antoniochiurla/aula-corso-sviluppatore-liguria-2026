from interfaces import ICalculator
from exceptions import CalcSyntaxError

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
        # TODO: Implementare la funzione e verificare che il
        # corrispondente test funzioni correttamente
        return False
    
    @staticmethod
    def _is_assignment_sign(str_value: str) -> bool:
        """
        Restituisce True se str_value contiene il simbolo = (uguale)
        altrimenti restituisce False 
        """
        # TODO: Implementare la funzione e verificare che il
        # corrispondente test funzioni correttamente
        return False
    
    @staticmethod
    def _is_number(str_value: str) -> bool:
        """
        Restituisce True se str_value contiene un numero
        altrimenti restituisce False 
        """
        # TODO: Implementare la funzione e verificare che il
        # corrispondente test funzioni correttamente
        return False
    
    @staticmethod
    def _is_variable_name(str_value: str) -> bool:
        """
        Restituisce True se str_value contiene un nome valido di variabile
        deve iniziare per una lettera maiuscola o minuscola e contenere solo lettere o cifre
        """
        # TODO: Implementare la funzione e verificare che il
        # corrispondente test funzioni correttamente
        return False
    
    @staticmethod
    def _parse_number(str_number: str) -> float:
        """
        Converte la stringa in un numero float
        """
        # TODO: Implementare la funzione restituendo il valore float corrispondente al contenuto della stringa
        return 0.0

    def get_variable(self, name: str) -> float:
        """
        ISTRUZIONI:
        Restituire il valore  della variabile con il nome fornito
        Se la variabile non esiste va restituito 0.0
        """
        # TODO: Implementare la funzione restituendo il valore float contenuto nella variabile
        return 0.0

    def set_variable(self, name: str, value: float) -> float:
        """
        ISTRUZIONI:
        Aggiungere la variabile con il valore fornito
        Se la variabile esiste già va sostituita
        Restituisce il valore assegnato alla variabile
        """
        # TODO: Implementare la funzione impostando il valore nella variabile
        pass

    @staticmethod
    def sum(add1: float, add2: float) -> float:
        """
        ISTRUZIONI:
        Restituire il risultato della somma dei due parametri
        """
        # TODO: implementare la somma
        return 0.0

    @staticmethod
    def diff(sub1: float, sub2: float) -> float:
        """
        ISTRUZIONI:
        Restituire il risultato della differenza tra i due parametri
        """
        # TODO: implementare la differenza
        return 0.0

    @staticmethod
    def mult(mult1: float, mult2: float) -> float:
        """
        ISTRUZIONI:
        Restituire il risultato del prodotto dei due parametri
        """
        # TODO: implementare la moltiplicazione
        return 0.0

    @staticmethod
    def div(div1: float, div2: float) -> float:
        """
        ISTRUZIONI:
        Restituire il risultato della divisione tra i due parametri
        """
        # TODO: implementare la divisione e generare CalcDivisionByZero se il divisore è zero
        return 0.0

    def _is_assignment_with_calculation(elements: list[str]) -> bool:
        # TODO: Implementare verificando che sia un'assegnazione con calcolo
        # esempi:
        #    a = 5 + 7
        return False
    
    def _is_assignment(elements: list[str]) -> bool:
        # TODO: Implementare verificando che sia un'assegnazione semplice
        # esempi:
        #    a = 5
        return False
    
    def _is_calculation(elements: list[str]) -> bool:
        # TODO: Implementare verificando che sia un calcolo semplice
        # esempi:
        #    a + 5
        #    a - 5
        return False
    
    def _assignment_with_calculation(elements: list[str]) -> float:
        # TODO: Implementare e verificare che la sintassi sia corretta
        # esempi:
        #    a = 5 + 7
        return 0.0
    
    def _assignment_or_calculation(elements: list[str]) -> float:
        # TODO: Implementare e verificare che la sintassi sia corretta
        # esempi:
        #    a = 5
        #    3 * 2
        return 0.0

    def _is_single_value(elements: list[str]) -> bool:
        # TODO: Implementare e verificare che la sintassi sia corretta
        # esempi:
        #    5
        #    42
        return False
        
    def _is_variable(elements: list[str]) -> bool:
        # TODO: Implementare e verificare che la sintassi sia corretta
        # esempi:
        #    a
        #    b5
        return False
        
    def _single_value_or_variable(elements: list[str]) -> float:
        # TODO: Implementare e verificare che la sintassi sia corretta
        # esempi:
        #    5
        #    a
        return 0.0
    
    operators = {
        '+': sum,
        '-': diff,
        '*': mult,
        '/': div,
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
                result = Calculator._single_value_or_variable(elements)
            case 2: # error
                raise CalcSyntaxError(expression, "non interpretata correttamente!!!")
            case 3: # variable assignment with single value or calculation
                result = Calculator._assignment_or_calculation(elements)
            case 4: # error
                raise CalcSyntaxError(expression, "non interpretata correttamente!!!")
            case 5: # variable assignment with calculation
                result = Calculator._assignment_with_calculation(elements)
            case _:
                raise CalcSyntaxError(expression, "non interpretata correttamente!!!")
        self.set_variable(self.last_value_variable, result)
        return result
    
