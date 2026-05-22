from abc import ABC, abstractmethod

class ICalculator(ABC):
    """
    Interfaccia per la logica della calcolatrice.
    Gli studenti devono implementare questa classe.
    """

    last_value_variable = "!"
    
    @abstractmethod
    def evaluate(self, expression: str) -> float:
        """
        Valuta un'espressione stringa (es. "5 + 3" o "x = 10 / 2")
        e restituisce il risultato numerico.
        """
        pass

    @abstractmethod
    def get_variables(self) -> dict:
        """Restituisce il dizionario delle variabili memorizzate."""
        pass

    @abstractmethod
    def get_variable(self) -> dict:
        """Restituisce il valore della variabili memorizzata."""
        pass

    @abstractmethod
    def set_variable(self, name: str, value: float) -> float:
        """Imposta il valore della variable e lo restituisce."""
        pass

    @abstractmethod
    def sum(self, add1: float, add2: float) -> float:
        """
        Restituisce il risultato della somma dei due parametri
        """
        pass

    @abstractmethod
    def diff(self, sub1: float, sub2: float) -> float:
        """
        Restituisce il risultato della differenza tra i due parametri
        """
        pass

    @abstractmethod
    def mult(self, mult1: float, mult2: float) -> float:
        """
        Restituisce il risultato del prodotto dei due parametri
        """
        pass

    @abstractmethod
    def div(self, div1: float, div2: float) -> float:
        """
        Restituisce il risultato della divisione tra i due parametri
        """
        pass
