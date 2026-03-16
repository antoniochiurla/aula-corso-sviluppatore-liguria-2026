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


# --- 7. ESECUZIONE E POLIMORFISMO ---
if __name__ == "__main__":
    print("--- Benvenuti in TaMaSy (Task Management System) ---")

    # Creazione degli oggetti (Istanze)
    t1 = BugTask("Errore Login", "Il tasto login non clicca", "ALTA")
    t2 = FeatureTask("Modalità Notte", "Aggiungere tema scuro", "Media")
    t3 = Task("Riunione", "Discussione team settimanale")

    # Mettiamo tutti i task in una lista (Collezione)
    lista_task = [t1, t2, t3]

    # Dimostrazione del Polimorfismo:
    # Chiamiamo lo stesso metodo .visualizza_info() su oggetti diversi.
    # Ogni oggetto risponde a modo suo!
    for task in lista_task:
        print(task.visualizza_info())

    # Modifica dello stato (Uso di un metodo)
    print("\nLavorando sui task...")
    t1.completa()

    print("\nStato aggiornato:")
    print(t1.visualizza_info())