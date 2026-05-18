import psycopg2
import time
import random
import statistics
import csv

create_all_data = False
create_fk_also = False

nomi = ['Antonio', 'Giovanni', 'Giorgio', 'Daniele', 'Giulio', 'Angelo', 'Ivo', 'Hamid', 'Sidar']
cognomi = ['Rossi', 'Bianchi', 'Gialli', 'Verdi', 'Blu', 'Gallo', 'Agnello']
materie = ['Storia', 'Matematica', 'Geometria', 'Lettere', 'Fisica', 'Chimica', 'Statistica']

comuni = []
commit_number = 0

id_indirizzo = 1
id_presenza = 1
id_studente_materia = 1

num_materie_studiate = 3

city_max_id = None

def create_tables(conn):
    try:
        with conn.cursor() as cursore: # creating a cursor
            # comando per creare la tabella Studenti
            cursore.execute("DROP TABLE IF EXISTS STUDENTI_MATERIE")
            cursore.execute("DROP TABLE IF EXISTS MATERIE")
            cursore.execute("DROP TABLE IF EXISTS PRESENZE")
            cursore.execute("DROP TABLE IF EXISTS STUDENTI")
            cursore.execute("DROP TABLE IF EXISTS INDIRIZZI")
            cursore.execute("DROP TABLE IF EXISTS CITTA")
            cursore.execute("""
            CREATE TABLE IF NOT EXISTS MATERIE
            (
                ID INT PRIMARY KEY NOT NULL,
                NOME TEXT NOT NULL
            )
            """)
            cursore.execute("""
            CREATE TABLE IF NOT EXISTS STUDENTI_MATERIE
            (
                ID INT PRIMARY KEY NOT NULL,
                ID_STUDENTE INT NOT NULL,
                ID_MATERIA INT NOT NULL
            )
            """)
            cursore.execute("""
            CREATE TABLE IF NOT EXISTS CITTA
            (
                ID INT PRIMARY KEY NOT NULL,
                NOME TEXT NOT NULL
            )
            """)
            cursore.execute("""
            CREATE TABLE IF NOT EXISTS INDIRIZZI
            (
                ID INT PRIMARY KEY NOT NULL,
                VIA TEXT NOT NULL,
                ID_CITTA INT NOT NULL
            )
            """)
            cursore.execute("""
            CREATE TABLE IF NOT EXISTS STUDENTI
            (
                ID INT   PRIMARY KEY NOT NULL,
                NOME TEXT NOT NULL,
                COGNOME TEXT NOT NULL,
                EMAIL TEXT NOT NULL,
                ID_INDIRIZZO INT NOT NULL
            )
            """)
            cursore.execute("""
            CREATE TABLE IF NOT EXISTS PRESENZE
            (
                ID INT   PRIMARY KEY NOT NULL,
                ID_STUDENTE INT NOT NULL,
                GIORNO TEXT NOT NULL
            )
            """)
            # cursore.execute("""
            # CREATE TABLE IF NOT EXISTS CITTA
            # (
            #     ID INT NOT NULL,
            #     NOME TEXT NOT NULL
            # )
            # """)

            if create_fk_also:
                cursore.execute("""
                ALTER TABLE PRESENZE 
                    ADD CONSTRAINT FK_PRESENZE_STUDENTI
                    FOREIGN KEY (ID_STUDENTE) 
                    REFERENCES STUDENTI (ID)
                """)
                cursore.execute("""
                ALTER TABLE STUDENTI 
                    ADD CONSTRAINT FK_STUDENTI_INDIRIZZI
                    FOREIGN KEY (ID_INDIRIZZO) 
                    REFERENCES INDIRIZZI (ID)
                """)
                cursore.execute("""
                ALTER TABLE INDIRIZZI
                    ADD CONSTRAINT FK_INDIRIZZI_CITTA
                    FOREIGN KEY (ID_CITTA) 
                    REFERENCES CITTA(ID)
                """)
                cursore.execute("""
                ALTER TABLE STUDENTI_MATERIE
                    ADD CONSTRAINT FK_STUDENTI_MATERIE_1
                    FOREIGN KEY (ID_STUDENTE) 
                    REFERENCES STUDENTI(ID)
                """)
                cursore.execute("""
                ALTER TABLE STUDENTI_MATERIE
                    ADD CONSTRAINT FK_STUDENTI_MATERIE_2
                    FOREIGN KEY (ID_MATERIA) 
                    REFERENCES MATERIE(ID)
                """)
        commit_on_db(conn)
    except Exception as e:
        print(f"La connessione al DB non funziona correttamente: {e}")


def delete_all_rows(conn):
    with conn.cursor() as cursore:
        cursore.execute("DELETE FROM MATERIE")
        cursore.execute("DELETE FROM STUDENTI_MATERIE")
        cursore.execute("DELETE FROM PRESENZE")
        cursore.execute("DELETE FROM INDIRIZZI")
        cursore.execute("DELETE FROM STUDENTI")
        cursore.execute("DELETE FROM CITTA")
        commit_on_db(conn)


def create_student(conn, id_studente, nome, cognome, email, id_citta):
    global id_indirizzo
    global id_presenza
    global id_studente_materia
    with conn.cursor() as cursore:
        via = f'via di {nome} {cognome}'
        cursore.execute("""
        INSERT INTO INDIRIZZI(ID, VIA, ID_CITTA)
            VALUES(%s, %s, %s)
        """,
            (id_indirizzo, via, id_citta)
        )
        cursore.execute("""
        INSERT INTO STUDENTI(ID, NOME, COGNOME, EMAIL, ID_INDIRIZZO)
            VALUES(%s, %s, %s, %s, %s)
        """,
            (id_studente, nome, cognome, email, id_indirizzo)
        )
        id_indirizzo += 1
        for num_presenza in range(1, 100):
            giorno = str(num_presenza)
            cursore.execute("""
            INSERT INTO PRESENZE(ID, ID_STUDENTE, GIORNO)
                VALUES(%s, %s, %s)
            """,
                (id_presenza, id_studente, giorno)
            )
            id_presenza += 1
        for num_materia_studiata in range(num_materie_studiate):
            id_materia = random.randint(1, len(materie))
            cursore.execute("""
            INSERT INTO STUDENTI_MATERIE(ID, ID_STUDENTE, ID_MATERIA)
                VALUES(%s, %s, %s)
            """,
                (id_studente_materia, id_studente, id_materia)
            )
            id_studente_materia += 1


def count_students(conn):
    with conn.cursor() as cursore:
        cursore.execute("""
            SELECT count(1) FROM STUDENTI
            """)
        risultato = cursore.fetchone()

        conteggio = risultato[0]

        print("Righe studenti presenti:", conteggio)
    return conteggio

def count_cities(conn):
    with conn.cursor() as cursore:
        cursore.execute("""
            SELECT count(1) FROM CITTA
            """)
        risultato = cursore.fetchone()

        conteggio = risultato[0]

        print("Righe citta' presenti:", conteggio)
    return conteggio

def choice_id_citta():
    return comuni[int(random.randint(1, len(comuni) - 1))]

def create_dummy_students(conn):
    id = 1
    for nome in nomi:
        for cognome in cognomi:
            email = f'{nome}.{cognome}@gmail.com'.lower()
            create_student(conn, id, nome, cognome, email, choice_id_citta())
            id += 1
    commit_on_db(conn)
    for nome1 in nomi:
        for nome2 in nomi:
            with psycopg2.connect(
                host="database_dev",
                database="devdb",
                user="devuser",
                password="devpassword") as conn2:
                if nome1 != nome2:
                    for cognome1 in cognomi:
                        for cognome2 in cognomi:
                            nome = f"{nome1} {nome2}"
                            cognome = f"{cognome1} {cognome2}"
                            email = f'{nome1}.{nome2}.{cognome1}.{cognome2}@gmail.com'.lower()
                            create_student(conn2, id, nome, cognome, email, choice_id_citta())
                            id += 1
                        commit_on_db(conn2)
                print(email)


def create_materie(conn):
    id_materia = 1
    with conn.cursor() as cursore:
        for materia in materie:
            cursore.execute("""
            INSERT INTO MATERIE(ID, NOME)
                VALUES(%s, %s)
            """,
                (id_materia, materia)
            )
            id_materia += 1
    commit_on_db(conn)

def create_cities(conn):
    row_number = 0
    with open('moduli/modulo03/snippets/comuni.csv', encoding='Latin-1') as comuni_csv:
        with conn.cursor() as cursore:
            csv_reader = csv.reader(comuni_csv, delimiter=';')
            for fields in csv_reader:
                if row_number > 2:
                    # print(fields)
                    codice_comune = fields[4]
                    nome_comune = fields[5]
                    comuni.append(codice_comune)
                    cursore.execute("""
                    INSERT INTO CITTA(ID, NOME)
                        VALUES(%s, %s)
                    """,
                        (codice_comune, nome_comune)
                    )
                row_number += 1


def commit_on_db(conn):
    global commit_number
    conn.commit()
    commit_number += 1



def list_students(conn):
    with conn.cursor() as cursore:
        cursore.execute("SELECT * FROM STUDENTI")
        rows = cursore.fetchall()
        for row in rows:
            print(row)

def list_presenze_with_students_and_indirizzo_and_city_and_materie(conn):
    with conn.cursor() as cursore:
        cursore.execute("""
            SELECT * FROM PRESENZE p
                JOIN STUDENTI s ON s.ID = p.ID_STUDENTE
                JOIN INDIRIZZI i ON i.ID = s.ID_INDIRIZZO
                JOIN CITTA c ON c.ID = i.ID_CITTA
                JOIN STUDENTI_MATERIE sm ON sm.ID_STUDENTE = s.ID
                JOIN MATERIE m ON m.ID = sm.ID_MATERIA
            """)
        rows = cursore.fetchall()
        # for row in rows:
        #     print(row)

def list_cities(conn):
    with conn.cursor() as cursore:
        cursore.execute("SELECT * FROM CITTA")
        rows = cursore.fetchall()
        for row in rows:
            print(row)

if __name__ == "__main__":
    times = []
    num_tries = 20
    if create_all_data:
        num_tries = 1
    for num_try in range(num_tries):
        start_time = time.time()
        with psycopg2.connect(
            host="database_dev",
            database="devdb",
            user="devuser",
            password="devpassword") as conn:
            if create_all_data:
                create_tables(conn)
                delete_all_rows(conn)
                create_cities(conn)
                create_materie(conn)
                create_dummy_students(conn)
                # list_students(conn)
            list_presenze_with_students_and_indirizzo_and_city_and_materie(conn)
            # list_cities(conn)
        elapsed = time.time() - start_time
        print(f"Elapsed time: {elapsed}")
        print(f"Number of commit: {commit_number}")
        times.append(elapsed)
    avg_elapsed = statistics.mean(times)
    print(f"Average elapsed time: {avg_elapsed}")
    

