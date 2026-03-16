# 1. Definizione della Classe (Il "Blueprint" o "Stampo")
class Task:
    """
    Questa classe rappresenta un singolo impegno nel sistema TaMaSy.
    È come la scheda tecnica di un task: definisce cosa può fare e che dati ha.
    """

    # 2. Il Costruttore: definisce cosa succede quando "nasce" un nuovo Task
    def __init__(self, titolo, descrizione, priorita):
        # --- 1. USO DI RAISE (Validazione dei dati) ---
        # Se il titolo è vuoto, lanciamo un errore invece di creare un task inutile
        if not titolo:
            raise ValueError("Errore: Il titolo del task non può essere vuoto!")

        # Validiamo la priorità: deve essere una di queste tre
        priorita_valide = ["Bassa", "Media", "Alta"]
        if priorita not in priorita_valide:
            raise ValueError(f"Errore: Priorità '{priorita}' non valida. Usa: {priorita_valide}")

        # Attributi di istanza (le caratteristiche del singolo task)
        self.titolo = titolo
        self.descrizione = descrizione
        self.priorita = priorita

        # Attributo "incapsulato": lo stato iniziale è sempre 'Aperto'
        # Usiamo il trattino basso _ per suggerire che non va toccato dall'esterno
        self._stato = "Aperto"

        # 3. Metodo per visualizzare i dettagli (Comportamento)

    def stampa_scheda(self):
        print("-" * 30)
        print(f"TASK: {self.titolo}")
        print(f"DESCRIZIONE: {self.descrizione}")
        print(f"PRIORITÀ: {self.priorita}")
        print(f"STATO: {self._stato}")
        print("-" * 30)

    # 4. Metodo per cambiare lo stato (Logica di business)
    def completa(self):
        # --- 2. USO DI RAISE (Logica di business) ---
        # Se il task è già chiuso, lanciamo un'eccezione specifica
        if self._stato == "Completato":
            raise Exception(f"Il task '{self.titolo}' è già stato completato!")

        self._stato = "Completato"
        print(f"Task '{self.titolo}' completato con successo.")

    # 5. Metodo per modificare la descrizione
    def aggiorna_descrizione(self, nuova_descrizione):
        self.descrizione = nuova_descrizione
        print(f"Descrizione di '{self.titolo}' aggiornata con successo.")


# --- UTILIZZO DELLA CLASSE (Programma Principale) ---
if __name__ == "__main__":

    # --- 3. USO DI TRY / EXCEPT (Gestione del programma) ---

    print("--- Tentativo 1: Creazione di un task corretto ---")
    try:
        t1 = Task("Studiare Python", "Ripassare try/except", "Alta")
        t1.stampa_scheda()
        t1.completa()
        # Proviamo a completarlo di nuovo per scatenare l'errore
        t1.completa()
    except Exception as e:
        print(f"Attenzione: {e}")

    print("\n--- Tentativo 2: Creazione di un task senza titolo ---")
    try:
        t2 = Task("", "Questo task fallirà", "Bassa")
    except ValueError as e:
        print(f"Bloccato dal sistema: {e}")

    print("\n--- Tentativo 3: Priorità inventata ---")
    try:
        t3 = Task("Comprare Pizza", "Margherita", "Urgentissima")
    except ValueError as e:
        print(f"Errore inserimento: {e}")

    print("\nIl programma non è crashato e continua a girare!")