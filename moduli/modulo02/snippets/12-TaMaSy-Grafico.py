import tkinter as tk
from tkinter import messagebox, ttk
import os

# =========================================================
# 1. CLASSI LOGICHE (Stesse della versione CLI)
# =========================================================

class Task:
    def __init__(self, titolo, descrizione, stato="Aperto"):
        self.titolo = titolo; self.descrizione = descrizione; self.stato = stato
    def visualizza(self): return f"[{self.stato}] {self.titolo}"
    def formatta_per_file(self): return f"TASK|{self.titolo}|{self.descrizione}|{self.stato}"

class BugTask(Task):
    def __init__(self, titolo, descrizione, severita, stato="Aperto"):
        super().__init__(titolo, descrizione, stato); self.severita = severita
    def visualizza(self): return f"[{self.stato}] 🐞 BUG({self.severita}) {self.titolo}"
    def formatta_per_file(self): return f"BUG|{self.titolo}|{self.descrizione}|{self.stato}|{self.severita}"

class FeatureTask(Task):
    def __init__(self, titolo, descrizione, priorita, stato="Aperto"):
        super().__init__(titolo, descrizione, stato); self.priorita = priorita
    def visualizza(self): return f"[{self.stato}] ⭐ FEAT({self.priorita}) {self.titolo}"
    def formatta_per_file(self): return f"FEATURE|{self.titolo}|{self.descrizione}|{self.stato}|{self.priorita}"

# =========================================================
# 2. INTERFACCIA GRAFICA (Tkinter)
# =========================================================

class TamasyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TaMaSy - Task Management System")
        self.root.geometry("500x550")
        self.file_db = "tamasy_data.txt"
        self.miei_task = self.carica_da_file()

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

        self.aggiorna_lista_visuale()

    # --- Logica dell'applicazione ---

    def carica_da_file(self):
        lista = []
        if os.path.exists(self.file_db):
            with open(self.file_db, "r") as f:
                for riga in f:
                    d = riga.strip().split("|")
                    if d[0] == "TASK": lista.append(Task(d[1], d[2], d[3]))
                    elif d[0] == "BUG": lista.append(BugTask(d[1], d[2], d[4], d[3]))
                    elif d[0] == "FEATURE": lista.append(FeatureTask(d[1], d[2], d[4], d[3]))
        return lista

    def salva_su_file(self):
        with open(self.file_db, "w") as f:
            for t in self.miei_task:
                f.write(t.formatta_per_file() + "\n")

    def aggiorna_lista_visuale(self):
        self.listbox.delete(0, tk.END)
        for t in self.miei_task:
            self.listbox.insert(tk.END, t.visualizza())

    def annulla_task(self):
        self.ent_titolo.delete(0, tk.END)
        self.ent_desc.delete(0, tk.END)
        self.combo_tipo.current(0)
        self.listbox.selection_clear(0, tk.END)

    def modifica_task(self, event):
        indice = self.listbox.curselection()[0]
        t = self.miei_task[indice]
        self.ent_titolo.delete(0, tk.END)
        self.ent_desc.delete(0, tk.END)
        self.ent_titolo.insert(0, t.titolo)
        self.ent_desc.insert(0, t.descrizione)
        self.combo_tipo.current(1 if t.__class__.__name__ == "BugTask" else 2 if t.__class__.__name__ == "FeatureTask" else 0)

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
            self.miei_task[indice] = nuovo
        else:
            self.miei_task.append(nuovo)

        self.salva_su_file()
        self.aggiorna_lista_visuale()
        self.annulla_task()

    def rimuovi_task(self):
        try:
            indice = self.listbox.curselection()[0]
            self.miei_task.pop(indice)
            self.salva_su_file()
            self.aggiorna_lista_visuale()
            self.annulla_task()
        except IndexError:
            messagebox.showerror("Errore", "Seleziona un task dalla lista!")

    def inverti_stato(self):
        try:
            indice = self.listbox.curselection()[0]
            t = self.miei_task[indice]
            t.stato = "Completato" if t.stato == "Aperto" else "Aperto"
            self.salva_su_file()
            self.aggiorna_lista_visuale()
            self.annulla_task()
        except IndexError:
            messagebox.showerror("Errore", "Seleziona un task dalla lista!")

# Avvio
if __name__ == "__main__":
    root = tk.Tk()
    app = TamasyApp(root)
    root.mainloop()