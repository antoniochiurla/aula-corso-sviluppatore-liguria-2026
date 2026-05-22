import os
from modelli import Task, BugTask, FeatureTask

NOME_FILE = "tamasy_data.txt"

def salva_task(lista_task, nome_file = NOME_FILE):
    """Prende una lista di oggetti e li scrive sul file"""
    try:
        with open(nome_file, "w") as f:
            for t in lista_task:
                f.write(t.formatta_per_file() + "\n")
        print(f"Backup di TaMaSy completato su {nome_file}")
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")


def carica_task(nome_file = NOME_FILE):
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
        raise e

    return lista_ricostruita

