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
    print("1 - task generico")
    print("2 - task di tipo bug")
    print("3 - task di tipo feature")
    tipo = input("Tipo di task da creare: ")
    
    titolo = input("Dammi il titolo: ")
    descrizione = input("Dammi la descrizione: ")
    if tipo == "1":
        task = Task(titolo, descrizione)
    elif tipo == "2":
        severita = input("dammi la severità: ")
        task = BugTask(titolo, descrizione, severita)
    elif tipo == "3":
        priorita = input("dammi la priorità")
        task = FeatureTask(titolo, descrizione, priorita)
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

def salva_task(lista_task, nome_file):
    """Prende una lista di oggetti e li scrive sul file"""
    try:
        with open(nome_file, "w") as f:
            for t in lista_task:
                f.write(t.formatta_per_file() + "\n")
        print(f"Backup di TaMaSy completato su {nome_file}")
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")


def carica_task(nome_file):
    """Legge il file e ricostruisce gli oggetti corretti"""
    lista_ricostruita = []
    if not os.path.exists(nome_file):
        return lista_ricostruita  # Ritorna lista vuota se il file non esiste ancora

    try:
        with open(nome_file, "r") as f:
            for riga in f:
                dati = riga.strip().split("|")
                tipo = dati[0]

                if tipo == "TASK":
                    obj = Task(dati[1], dati[2], dati[3])
                elif tipo == "BUG":
                    obj = BugTask(dati[1], dati[2], dati[4], dati[3])
                elif tipo == "FEATURE":
                    obj = FeatureTask(dati[1], dati[2], dati[4], dati[3])

                lista_ricostruita.append(obj)
        print(f"Dati caricati correttamente da {nome_file}")
    except Exception as e:
        print(f"Errore durante il caricamento: {e}")

    return lista_ricostruita

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
