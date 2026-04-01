import os


# --- 1. CLASSI CON METODI DI SERIALIZZAZIONE ---
class Task:
    def __init__(self, titolo, descrizione, stato="Aperto"):
        self.titolo = titolo
        self.descrizione = descrizione
        self._stato = stato

    def visualizza(self):
        return f"[{self._stato}] {self.titolo}: {self.descrizione}"

    # Trasforma l'oggetto in una riga di testo per il file
    def formatta_per_file(self):
        return f"TASK|{self.titolo}|{self.descrizione}|{self._stato}"


class BugTask(Task):
    def __init__(self, titolo, descrizione, severita, stato="Aperto"):
        super().__init__(titolo, descrizione, stato)
        self.severita = severita

    def visualizza(self):
        return super().visualizza() + f" [BUG - {self.severita}]"

    def formatta_per_file(self):
        return f"BUG|{self.titolo}|{self.descrizione}|{self._stato}|{self.severita}"


class FeatureTask(Task):
    def __init__(self, titolo, descrizione, priorita, stato="Aperto"):
        super().__init__(titolo, descrizione, stato)
        self.priorita = priorita

    def visualizza(self):
        return super().visualizza() + f" [FEATURE - {self.priorita}]"

    def formatta_per_file(self):
        return f"FEATURE|{self.titolo}|{self.descrizione}|{self._stato}|{self.priorita}"


# --- 2. FUNZIONI DI GESTIONE FILE ---

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


# --- 3. TEST DEL SISTEMA ---
if __name__ == "__main__":
    FILE_DATABASE = "tamasy_data.txt"

    # Proviamo a caricare i dati esistenti
    miei_task = carica_task(FILE_DATABASE)

    if not miei_task:
        print("Nessun dato trovato. Creo dei task di esempio...")
        miei_task.append(BugTask("Errore Grafico", "Il logo è storto", "Bassa"))
        miei_task.append(FeatureTask("Notifiche", "Aggiungere suoni", "Alta"))
        miei_task.append(Task("Riunione", "Check con il team"))

    # Visualizziamo i task correnti
    print("\n--- I TUOI TASK ATTUALI ---")
    for t in miei_task:
        print(t.visualizza())

    # Salviamo tutto per la prossima volta
    salva_task(miei_task, FILE_DATABASE)