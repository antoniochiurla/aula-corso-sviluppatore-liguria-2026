import tkinter as tk
from tkinter import ttk, messagebox
from modelli import Task, BugTask, FeatureTask, tasks
import persist_file as persist

class Finestra:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.root.title("TaMaSy - Task Management System")
        self.root.geometry("500x550")
        self.file_db = "tamasy_data.txt"

        # --- Elementi UI (Widget) ---
        tk.Label(root, text="TaMaSy Management", font=("Arial", 16, "bold")).pack(pady=10)

        # Form di inserimento
        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Titolo:").grid(row=0, column=0)
        self.ent_titolo = tk.Entry(frame_form, width=30)
        self.ent_titolo.grid(row=0, column=1)

        tk.Label(frame_form, text="Descrizione:").grid(row=1, column=0)
        self.ent_desc = tk.Entry(frame_form, width=30)
        self.ent_desc.grid(row=1, column=1)

        tk.Label(frame_form, text="Tipo:").grid(row=2, column=0)
        self.combo_tipo = ttk.Combobox(frame_form, values=["Task Base", "Bug", "Feature"], state="readonly")
        self.combo_tipo.current(0)
        self.combo_tipo.grid(row=2, column=1)

        tk.Button(root, text="Salva Task", command=self.salva_task).pack(pady=5)
        tk.Button(root, text="Annulla", command=self.annulla_task).pack(padx=5)

        # Lista visuale
        tk.Label(root, text="Lista dei tuoi impegni:").pack()
        self.listbox = tk.Listbox(root, width=60, height=10)
        self.listbox.bind('<<ListboxSelect>>', self.modifica_task)

        self.listbox.pack(pady=10, padx=10)

        # Pulsanti Azione
        frame_azioni = tk.Frame(root)
        frame_azioni.pack(pady=10)

        tk.Button(frame_azioni, text="Inverti Stato", command=self.inverti_stato).grid(row=0, column=0, padx=5)
        tk.Button(frame_azioni, text="Rimuovi", command=self.rimuovi_task).grid(row=0, column=1, padx=5)

        self.carica_dati()


    def carica_dati(self):
        tasks_letti = persist.carica_task(self.file_db)
        tasks.clear()
        for task in tasks_letti:
            tasks.append(task)
        self.aggiorna_lista_visuale()

    def aggiorna_lista_visuale(self):
        self.listbox.delete(0, tk.END)
        for t in tasks:
            print(t.visualizza_info())
            self.listbox.insert(tk.END, t.visualizza_info())

    def salva_task(self):
        tit = self.ent_titolo.get()
        desc = self.ent_desc.get()
        tipo = self.combo_tipo.get()

        if not tit:
            messagebox.showwarning("Attenzione", "Il titolo è obbligatorio!")
            return

        if tipo == "Bug": nuovo = BugTask(tit, desc, "Media")
        elif tipo == "Feature": nuovo = FeatureTask(tit, desc, "Normale")
        else: nuovo = Task(tit, desc)

        # Verifica se la lista ha un elemento selezionato
        if self.listbox.curselection():
            indice = self.listbox.curselection()[0]
            tasks[indice] = nuovo
        else:
            tasks.append(nuovo)

        self.salva_dati()
        self.aggiorna_lista_visuale()
        self.annulla_task()

    def salva_dati(self):
        persist.salva_task(tasks)

    def annulla_task(self):
        self.ent_titolo.delete(0, tk.END)
        self.ent_desc.delete(0, tk.END)
        self.combo_tipo.current(0)
        self.listbox.selection_clear(0, tk.END)

    def modifica_task(self, event):
        indice = self.listbox.curselection()[0]
        t = tasks[indice]
        self.ent_titolo.delete(0, tk.END)
        self.ent_desc.delete(0, tk.END)
        self.ent_titolo.insert(0, t.titolo)
        self.ent_desc.insert(0, t.descrizione)
        self.combo_tipo.current(1 if t.__class__.__name__ == "BugTask" else 2 if t.__class__.__name__ == "FeatureTask" else 0)

    def inverti_stato(self):
        try:
            indice = self.listbox.curselection()[0]
            t = tasks[indice]
            t.stato = "Completato" if t.stato == "Aperto" else "Aperto"
            self.salva_dati()
            self.aggiorna_lista_visuale()
            self.annulla_task()
        except IndexError:
            messagebox.showerror("Errore", "Seleziona un task dalla lista!")

    def rimuovi_task(self):
        try:
            indice = self.listbox.curselection()[0]
            tasks.pop(indice)
            self.salva_dati()
            self.aggiorna_lista_visuale()
            self.annulla_task()
        except IndexError:
            messagebox.showerror("Errore", "Seleziona un task dalla lista!")
    
    def loop(self):
        self.root.mainloop()


def gestisci_interfaccia():
    finestra = Finestra()
    finestra.loop()


if __name__ == "__main__":
    gestisci_interfaccia()

