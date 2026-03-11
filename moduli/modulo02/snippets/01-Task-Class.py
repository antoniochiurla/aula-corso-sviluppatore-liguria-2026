# 1. Definizione della Classe (Il "Blueprint" o "Stampo")
class Task:
    """
    Questa classe rappresenta un singolo impegno nel sistema TaMaSy.
    È come la scheda tecnica di un task: definisce cosa può fare e che dati ha.
    """

    # 2. Il Costruttore: definisce cosa succede quando "nasce" un nuovo Task
    def __init__(self, titolo, descrizione, priorita):
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
        if self._stato == "Aperto":
            self._stato = "Completato"
            print(f"Ottimo lavoro! Il task '{self.titolo}' è stato chiuso.")
        else:
            print(f"Il task '{self.titolo}' è già stato completato in precedenza.")

    # 5. Metodo per modificare la descrizione
    def aggiorna_descrizione(self, nuova_descrizione):
        self.descrizione = nuova_descrizione
        print(f"Descrizione di '{self.titolo}' aggiornata con successo.")


# --- UTILIZZO DELLA CLASSE (Programma Principale) ---
if __name__ == "__main__":

    # Creazione di due oggetti (Istanze) distinti
    print("Creazione dei primi task in TaMaSy...\n")

    task_a = Task("Comprare il latte", "Prendere quello parzialmente scremato", "Bassa")
    task_b = Task("Studiare Python", "Ripassare i concetti di classe e oggetto", "ALTA")

    # Utilizzo dei metodi sugli oggetti
    task_a.stampa_scheda()
    task_b.stampa_scheda()

    # Interazione con gli oggetti
    task_b.completa()  # Cambiamo lo stato del secondo task
    task_b.stampa_scheda()  # Verifichiamo il cambiamento

    # Proviamo a completarlo di nuovo per vedere la gestione dell'errore interno
    task_b.completa()