# --- 1. DEFINIZIONE DELLA CLASSE (Il Progetto/Blueprint) ---
class Task:
    """
    Rappresenta un compito generico all'interno di TaMaSy.
    """

    # --- 2. COSTRUTTORE (Inizializzazione dell'oggetto) ---
    def __init__(self, titolo, descrizione, stato = "Aperto"):
        # Attributi Pubblici
        self.titolo = titolo
        self.descrizione = descrizione

        # --- 3. INCAPSULAMENTO (Dati protetti) ---
        # Usiamo l'underscore _ per dire "non modificare questo dato direttamente dall'esterno"
        self._stato = stato
        self._tipo = "Task"

        # --- 4. METODI (Comportamenti dell'oggetto) ---

    def completa(self):
        """Segna il task come completato"""
        self._stato = "Completato"
        print(f"Notifica: Il task '{self.titolo}' è stato completato!")

    def visualizza_info(self):
        """Metodo base per visualizzare i dettagli (verrà usato per il Polimorfismo)"""
        return f"{self._tipo} [{self._stato}] {self.titolo}: {self.descrizione}"

    # Trasforma l'oggetto in una riga di testo per il file
    def formatta_per_file(self):
        return f"TASK|{self.titolo}|{self.descrizione}|{self._stato}"


# --- 5. EREDITARIETÀ (Specializzazione) ---
class BugTask(Task):
    """Un tipo di Task specifico per gestire i Bug (errori del software)"""

    def __init__(self, titolo, descrizione, severita, stato = "Aperto"):
        # Chiamiamo il costruttore della classe "Padre" (Task)
        super().__init__(titolo, descrizione, stato)
        self.severita = severita  # Attributo specifico di BugTask
        self._tipo = "Bug"

    # --- 6. OVERRIDING (Riscrivere un metodo del padre) ---
    def visualizza_info(self):
        # Modifichiamo il comportamento del metodo per aggiungere la severità
        info_base = super().visualizza_info()
        return f"{info_base} | SEVERITÀ: {self.severita}"

    def formatta_per_file(self):
        return f"BUG|{self.titolo}|{self.descrizione}|{self._stato}|{self.severita}"


class FeatureTask(Task):
    """Un tipo di Task specifico per le nuove funzionalità"""

    def __init__(self, titolo, descrizione, priorita, stato = "Aperto"):
        super().__init__(titolo, descrizione, stato)
        self.priorita = priorita
        self._tipo = "Feature"

    def visualizza_info(self):
        info_base = super().visualizza_info()
        return f"{info_base} | PRIORITÀ: {self.priorita}"

    def formatta_per_file(self):
        return f"FEATURE|{self.titolo}|{self.descrizione}|{self._stato}|{self.priorita}"

tasks = []
