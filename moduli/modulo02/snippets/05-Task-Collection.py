import os


# --- 1. CLASSI CON METODI DI SERIALIZZAZIONE ---
class Task:
    def __init__(self, titolo, descrizione, stato="Aperto"):
        self.titolo = titolo
        self.descrizione = descrizione
        self._stato = stato

    def visualizza(self):
        return f"[{self._stato}] {self.titolo}: {self.descrizione}"


class BugTask(Task):
    def __init__(self, titolo, descrizione, severita, stato="Aperto"):
        super().__init__(titolo, descrizione, stato)
        self.severita = severita

    def visualizza(self):
        return super().visualizza() + f" [BUG - {self.severita}]"


class FeatureTask(Task):
    def __init__(self, titolo, descrizione, priorita, stato="Aperto"):
        super().__init__(titolo, descrizione, stato)
        self.priorita = priorita

    def visualizza(self):
        return super().visualizza() + f" [FEATURE - {self.priorita}]"


# --- 2. TEST DEL SISTEMA ---
if __name__ == "__main__":

    # Creiamo una lista vuota per contenere i task
    task_list = []

    # Creiamo un primo task
    errore_grafico = BugTask("Errore Grafico", "Il logo è storto", "Bassa")
    # aggiungiamolo alla lista
    task_list.append(errore_grafico)

    # Creiamo altri due task
    notifiche = FeatureTask("Notifiche", "Aggiungere suoni", "Alta")
    task_list.append(notifiche)
    riunione = Task("Riunione", "Check con il team")
    task_list.append(riunione)

    # Visualizziamo i task correnti
    print("\n--- I TUOI TASK ATTUALI ---")
    # ad ogni "giro" t è associato a un task della lista
    for t in task_list:
        print(t.visualizza())

    print("\n--- IL PRIMO DELLA LISTA ---")
    print(task_list[0].visualizza())

    print("\n--- L'ULTIMO DELLA LISTA ---")
    print(task_list[-1].visualizza())



    # creiamo un dizionario per associare ogni task ad un indice
    task_dictionary = {}

    # aggiungiamo i task al dizionario associandoli al loro titolo come indice
    task_dictionary[errore_grafico.titolo] = errore_grafico
    task_dictionary[notifiche.titolo] = notifiche
    task_dictionary[riunione.titolo] = riunione

    print("\n--- TUTTI I TASK ---")
    # ad ogni "giro" i è associato all'indice
    for i in task_dictionary:
        print(f"{i}: {task_dictionary[i].visualizza()}")

    print("\n--- ANCORA TUTTI I TASK ---")
    # ad ogni "giro" i è associato all'indice e t al task
    for i, t in task_dictionary.items():
        print(f"{i}: {t.visualizza()}")

    print("\n--- TUTTI I TASK COMPLETATI ---")
    for i, t in task_dictionary.items():
        if t._stato == "Completato":
            print(f"{i}: {t.visualizza()}")

    print("\n--- TUTTI I TASK IN ORDINE ALFABETICO ---")
    for t in sorted(task_dictionary.keys()):
        print(f"{t}: {task_dictionary[t].visualizza()}")

    print("\n--- SOLO L'ERRORE GRAFICO ---")
    errore_grafico_da_dizionario = task_dictionary[errore_grafico.titolo]
    print(f"{errore_grafico_da_dizionario.titolo}: {errore_grafico_da_dizionario.visualizza()}")

