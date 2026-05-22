import os


# =========================================================
# 1. DEFINIZIONE DELLE CLASSI (LOGICA)
# =========================================================

class Task:
    def __init__(self, titolo, descrizione, stato="Aperto"):
        self.titolo = titolo
        self.descrizione = descrizione
        self.stato = stato

    def visualizza(self):
        return f"[{self.stato}] {self.titolo}: {self.descrizione}"

    def formatta_per_file(self):
        return f"TASK|{self.titolo}|{self.descrizione}|{self.stato}"


class BugTask(Task):
    def __init__(self, titolo, descrizione, severita, stato="Aperto"):
        super().__init__(titolo, descrizione, stato)
        self.severita = severita

    def visualizza(self):
        return f"[{self.stato}] BUG ({self.severita}) {self.titolo}: {self.descrizione}"

    def formatta_per_file(self):
        return f"BUG|{self.titolo}|{self.descrizione}|{self.stato}|{self.severita}"


class FeatureTask(Task):
    def __init__(self, titolo, descrizione, priorita, stato="Aperto"):
        super().__init__(titolo, descrizione, stato)
        self.priorita = priorita

    def visualizza(self):
        return f"[{self.stato}] FEAT ({self.priorita}) {self.titolo}: {self.descrizione}"

    def formatta_per_file(self):
        return f"FEATURE|{self.titolo}|{self.descrizione}|{self.stato}|{self.priorita}"


# =========================================================
# 2. GESTIONE PERSISTENZA (FILE)
# =========================================================

FILE_DB = "tamasy_data.txt"


def salva_tutto(lista_task):
    with open(FILE_DB, "w") as f:
        for t in lista_task:
            f.write(t.formatta_per_file() + "\n")


def carica_tutto():
    lista = []
    if not os.path.exists(FILE_DB):
        return lista
    with open(FILE_DB, "r") as f:
        for riga in f:
            d = riga.strip().split("|")
            if d[0] == "TASK":
                lista.append(Task(d[1], d[2], d[3]))
            elif d[0] == "BUG":
                lista.append(BugTask(d[1], d[2], d[4], d[3]))
            elif d[0] == "FEATURE":
                lista.append(FeatureTask(d[1], d[2], d[4], d[3]))
    return lista


# =========================================================
# 3. INTERFACCIA UTENTE (MENU)
# =========================================================

def mostra_menu():
    print("\n--- TaMaSy MENU ---")
    print("1. Lista Task")
    print("2. Aggiungi Task")
    print("3. Correzione (Modifica) Task")
    print("4. Rimuovi Task")
    print("5. Modifica Stato (Apri/Chiudi)")
    print("6. Esci")
    return input("Scegli un'opzione: ")


def main():
    miei_task = carica_tutto()

    while True:
        scelta = mostra_menu()

        if scelta == "1":  # LISTA
            print("\n--- I TUOI TASK ---")
            if not miei_task: print("Lista vuota.")
            for i, t in enumerate(miei_task):
                print(f"{i}. {t.visualizza()}")

        elif scelta == "2":  # AGGIUNTA
            print("\nTipo: 1. Base, 2. Bug, 3. Feature")
            tipo = input("Scegli tipo: ")
            tit = input("Titolo: ")
            desc = input("Descrizione: ")
            if tipo == "2":
                sev = input("Severità: ")
                miei_task.append(BugTask(tit, desc, sev))
            elif tipo == "3":
                prio = input("Priorità: ")
                miei_task.append(FeatureTask(tit, desc, prio))
            else:
                miei_task.append(Task(tit, desc))
            salva_tutto(miei_task)
            print("Task aggiunto e salvato!")

        elif scelta == "3":  # CORREZIONE
            idx = int(input("Indice del task da modificare: "))
            if 0 <= idx < len(miei_task):
                miei_task[idx].titolo = input("Nuovo titolo: ")
                miei_task[idx].descrizione = input("Nuova descrizione: ")
                salva_tutto(miei_task)
                print("Task aggiornato!")

        elif scelta == "4":  # RIMOZIONE
            idx = int(input("Indice del task da rimuovere: "))
            if 0 <= idx < len(miei_task):
                miei_task.pop(idx)
                salva_tutto(miei_task)
                print("Task rimosso!")

        elif scelta == "5":  # MODIFICA STATO
            idx = int(input("Indice del task: "))
            if 0 <= idx < len(miei_task):
                nuovo_stato = "Completato" if miei_task[idx].stato == "Aperto" else "Aperto"
                miei_task[idx].stato = nuovo_stato
                salva_tutto(miei_task)
                print(f"Stato cambiato in {nuovo_stato}!")

        elif scelta == "6":  # USCITA
            print("Arrivederci da TaMaSy!")
            break
        else:
            print("Opzione non valida.")


if __name__ == "__main__":
    main()