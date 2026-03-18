# --- 1. DEFINIZIONE DELLA CLASSE (Il Progetto/Blueprint) ---
class Task:
    """
    Rappresenta un compito generico all'interno di TaMaSy.
    """

    # --- 2. COSTRUTTORE (Inizializzazione dell'oggetto) ---
    def __init__(self, titolo, descrizione):
        # Attributi Pubblici
        self.titolo = titolo
        self.descrizione = descrizione

        # --- 3. INCAPSULAMENTO (Dati protetti) ---
        # Usiamo l'underscore _ per dire "non modificare questo dato direttamente dall'esterno"
        self._stato = "Aperto"
        self._tipo = "Task"

        # --- 4. METODI (Comportamenti dell'oggetto) ---

    def completa(self):
        """Segna il task come completato"""
        self._stato = "Completato"
        print(f"Notifica: Il task '{self.titolo}' è stato completato!")

    def visualizza_info(self):
        """Metodo base per visualizzare i dettagli (verrà usato per il Polimorfismo)"""
        return f"{self._tipo} [{self._stato}] {self.titolo}: {self.descrizione}"


# --- 5. EREDITARIETÀ (Specializzazione) ---
class BugTask(Task):
    """Un tipo di Task specifico per gestire i Bug (errori del software)"""

    def __init__(self, titolo, descrizione, severita):
        # Chiamiamo il costruttore della classe "Padre" (Task)
        super().__init__(titolo, descrizione)
        self.severita = severita  # Attributo specifico di BugTask
        self._tipo = "Bug"

    # --- 6. OVERRIDING (Riscrivere un metodo del padre) ---
    def visualizza_info(self):
        # Modifichiamo il comportamento del metodo per aggiungere la severità
        info_base = super().visualizza_info()
        return f"{info_base} | SEVERITÀ: {self.severita}"


class FeatureTask(Task):
    """Un tipo di Task specifico per le nuove funzionalità"""

    def __init__(self, titolo, descrizione, priorita):
        super().__init__(titolo, descrizione)
        self.priorita = priorita
        self._tipo = "Feature"

    def visualizza_info(self):
        info_base = super().visualizza_info()
        return f"{info_base} | PRIORITÀ: {self.priorita}"

def mostra_menu():
    print("1 - aggiungi task")
    print("2 - lista task")
    print("3 - completa task")
    print("0 - esci")

def chiedi_opzione():
    opzione = input("Scegli l'opzione: ")
    return opzione

def richiedi_task():
    titolo = input("Dammi il titolo: ")
    descrizione = input("Dammi la descrizione: ")
    task = Task(titolo, descrizione)
    return task

def aggiungi_task():
    nuovo_task = richiedi_task()
    tasks.append(nuovo_task)

def lista_task():
    for indice, task in enumerate(tasks):
        print(indice, task.visualizza_info())


def completa_task():
    lista_task()
    indice = int(input("Dammi l'indice del task da completare: "))
    task = tasks[indice]
    task.completa()
    print(task.visualizza_info())

def main():
    rimani = True
    while rimani:
        mostra_menu()
        opzione = chiedi_opzione()
        if opzione == "0":
            rimani = False
        elif opzione == "1":
            aggiungi_task()
        elif opzione == "2":
            lista_task()
        elif opzione == "3":
            completa_task()

tasks = []

if __name__ == '__main__':
    main()
