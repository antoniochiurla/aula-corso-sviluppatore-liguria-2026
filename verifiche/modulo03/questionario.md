Verifica Modulo 3: Sviluppo Web e Database
==
Nome e Cognome: _______________________________________

Data: ___________

PARTE 1: Architettura e Fondamenti del Web (Risposta Chiusa)
===

1. Nell'architettura Client-Server, qual è il ruolo principale del "Client"?

    A) Gestire il database e la sicurezza dei dati.

    B) Inviare richieste al server e visualizzare l'interfaccia all'utente.

    C) Eseguire le migrazioni del database.

    D) Rispondere alle richieste degli altri browser.

2. Cosa succede durante una richiesta HTTP di tipo "POST"?

    A) Il browser richiede solo di visualizzare una pagina senza inviare dati.

    B) Il browser invia dati al server (es. i dati di un nuovo task) per essere elaborati.

    C) Il server cancella automaticamente il database.

    D) Viene aggiornato solo il file CSS della pagina.

3. L'architettura "3-tier" (a tre livelli) divide l'applicazione in:

    A) HTML, CSS e JavaScript.

    B) Presentation Layer, Logic Layer e Data Layer.

    C) Windows, Mac e Linux.

    D) Header, Body e Footer.

PARTE 2: Frontend - HTML, CSS e Bootstrap
===
4. In HTML5, quale tag è corretto per creare un modulo di inserimento dati?

    A) <input>

    B) <table_form>

    C) <form>

    D) <section>

5. A cosa serve il "Grid System" di Bootstrap (basato su 12 colonne)?

    A) A decidere il colore dei font nel sito.

    B) A creare layout responsivi che si adattano a diverse dimensioni di schermo.

    C) A velocizzare la connessione al database.

    D) A nascondere il codice JavaScript agli utenti.

6. Quale classe Bootstrap useresti per rendere un pulsante rosso (indicando ad esempio un Bug o un'azione di eliminazione)?

    A) .btn-primary

    B) .btn-success

    C) .btn-danger

    D) .btn-warning

7. Che cos'è il DOM (Document Object Model) in JavaScript?

    A) Un nuovo tipo di database relazionale.

    B) La rappresentazione ad albero della pagina HTML che JS può modificare dinamicamente.

    C) Il protocollo che cripta le password.

    D) Una libreria di icone per Bootstrap.

PARTE 3: Backend e Database (Django & SQL)
===

8. Nel pattern MVT di Django, a cosa serve il "Template"?

    A) A definire la struttura delle tabelle nel database.

    B) A gestire la logica di business e i calcoli.

    C) A generare l'output HTML che verrà visualizzato dall'utente.

    D) A smistare le URL del sito.

9. In un database SQL, che cos'è una "Foreign Key" (Chiave Esterna)?

    A) La password per accedere al server.

    B) Un vincolo che stabilisce una relazione tra due tabelle (es. collega un Task a un Utente).

    C) L'ID principale e univoco di una riga.

    D) Un comando per cancellare l'intera tabella.

10. Quale comando SQL useresti per modificare lo stato di un task esistente?

    A) INSERT

    B) SELECT

    C) UPDATE

    D) ALTER

11. A cosa serve il file models.py in Django?

    A) A definire la struttura dei dati (tabelle) tramite classi Python.

    B) A scrivere il codice CSS del sito.

    C) A configurare l'indirizzo IP del server.

    D) A gestire i click dell'utente sulla pagina.

PARTE 4: Risposte Aperte (Spiegazione e Analisi)
===

12. Spiega brevemente il flusso di una richiesta in Django: cosa succede dal momento in cui l'utente clicca su un link al momento in cui vede la pagina?

13. In TaMaSy Web, abbiamo usato {% csrf_token %} all'interno dei form. Spiega a cosa serve e perché è importante per la sicurezza.

14. Descrivi la differenza tra un Database Relazionale (come MySQL o SQLite) e un file di testo semplice (come il .txt usato nel modulo 2).

15. Che cos'è un ORM e quali vantaggi offre a un programmatore Django rispetto allo scrivere SQL a mano?

16. Perché le password degli utenti non dovrebbero mai essere salvate in "chiaro" nel database? Cosa si usa al loro posto?

17. Cosa si intende per "Responsive Design" e come lo abbiamo implementato in TaMaSy utilizzando Bootstrap?

18. In Django, a cosa servono i comandi makemigrations e migrate?

19. Spiega il concetto di "Relazione 1 a Molti" facendo l'esempio del rapporto tra Utenti e Task in TaMaSy.

20. Descrivi la funzione del decoratore @login_required applicato a una View.


