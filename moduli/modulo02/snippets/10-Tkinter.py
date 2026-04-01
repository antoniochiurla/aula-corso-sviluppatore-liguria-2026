import tkinter as tk
from tkinter import messagebox

# 1. Definizione della funzione che verrà eseguita al click del bottone
def azione_saluto():
    nome = voce_input.get()  # Recupera il testo scritto dall'utente
    if nome:
        messaggio = f"Ciao {nome}! Benvenuto nel mondo di TaMaSy."
        etichetta_risultato.config(text=messaggio, fg="blue") # Cambia il testo della label
    else:
        messagebox.showwarning("Attenzione", "Devi inserire un nome!")

# Avvio
if __name__ == "__main__":
    # 2. Creazione della finestra principale
    finestra = tk.Tk()
    finestra.title("Primo Esempio GUI")
    finestra.geometry("300x250")

    # 3. Creazione degli elementi (Widget)
    istruzione = tk.Label(finestra, text="Come si chiama il tuo Pou?", font=("Arial", 10))
    istruzione.pack(pady=10) # pady aggiunge spazio verticale

    voce_input = tk.Entry(finestra) # Campo dove l'utente scrive
    voce_input.pack(pady=5)

    bottone = tk.Button(finestra, text="Saluta!", command=azione_saluto)
    bottone.pack(pady=10)

    etichetta_risultato = tk.Label(finestra, text="", font=("Arial", 10, "italic"))
    etichetta_risultato.pack(pady=20)

    # 4. Avvio del ciclo infinito (ascolta gli eventi del mouse/tastiera)
    finestra.mainloop()