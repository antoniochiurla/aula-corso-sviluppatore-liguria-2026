import psycopg2
import time
import random

nomi = ['Antonio', 'Giovanni', 'Giorgio', 'Daniele', 'Giulio', 'Angelo', 'Ivo', 'Hamid', 'Sidar']
cognomi = ['Rossi', 'Bianchi', 'Gialli', 'Verdi', 'Blu', 'Gallo', 'Agnello']

cittas = ['Genova', 'Torino', 'Roma', 'Fasano', 'Milano', 'Alberobello']
commit_number = 0

city_max_id = None

def create_tables(conn):
    try:
        with conn.cursor() as cursore: # creating a cursor
            # comando per creare la tabella Studenti
            cursore.execute("DROP TABLE IF EXISTS STUDENTI")
            cursore.execute("""
            CREATE TABLE IF NOT EXISTS STUDENTI
            (
                ID INT   PRIMARY KEY NOT NULL,
                NOME TEXT NOT NULL,
                COGNOME TEXT NOT NULL,
                EMAIL TEXT NOT NULL,
                ID_CITTA INT NOT NULL
            )
            """)
            cursore.execute("""
            CREATE TABLE IF NOT EXISTS CITTA
            (
                ID INT   PRIMARY KEY NOT NULL,
                NOME TEXT NOT NULL
            )
            """)
        commit_on_db(conn)
    except Exception as e:
        print(f"La connessione al DB non funziona correttamente: {e}")

def create_student(conn, id, nome, cognome, email, id_citta):
    with conn.cursor() as cursore:
        cursore.execute("""
        INSERT INTO STUDENTI(ID, NOME, COGNOME, EMAIL, ID_CITTA)
            VALUES(%s, %s, %s, %s, %s)
        """,
            (id, nome, cognome, email, id_citta)
        )

def create_city(conn, id, nome):
    with conn.cursor() as cursore:
        cursore.execute("""
        INSERT INTO CITTA(ID, NOME)
            VALUES(%s, %s)
        """,
            (id, nome)
        )


def count_students(conn):
    with conn.cursor() as cursore:
        cursore.execute("""
            SELECT count(1) FROM STUDENTI
            """)
        risultato = cursore.fetchone()

        conteggio = risultato[0]

        print("Righe presenti:", conteggio)
    return conteggio

def choice_id_citta():
    return int(random.randint(1, city_max_id - 1))

def create_dummy_students(conn):
    id = 1
    for nome in nomi:
        for cognome in cognomi:
            email = f'{nome}.{cognome}@gmail.com'.lower()
            create_student(conn, id, nome, cognome, email, choice_id_citta())
            id += 1
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


def create_dummy_cities(conn):
    global city_max_id
    id = 1
    for citta in cittas:
            create_city(conn, id, citta)
            id += 1
    city_max_id = id

def commit_on_db(conn):
    global commit_number
    conn.commit()
    commit_number += 1



def delete_all_rows(conn):
    with conn.cursor() as cursore:
        cursore.execute("DELETE FROM STUDENTI")
        cursore.execute("DELETE FROM CITTA")
        commit_on_db(conn)


def list_students(conn):
    with conn.cursor() as cursore:
        cursore.execute("SELECT * FROM STUDENTI")
        rows = cursore.fetchall()
        for row in rows:
            print(row)

def list_cities(conn):
    with conn.cursor() as cursore:
        cursore.execute("SELECT * FROM CITTA")
        rows = cursore.fetchall()
        for row in rows:
            print(row)

if __name__ == "__main__":
    start_time = time.time()
    with psycopg2.connect(
        host="database_dev",
        database="devdb",
        user="devuser",
        password="devpassword") as conn:
        create_tables(conn)
        delete_all_rows(conn)
        create_dummy_cities(conn)
        create_dummy_students(conn)
        list_students(conn)
        list_cities(conn)
    print(f"Elapsed time: {time.time() - start_time}")
    print(f"Number of commit: {commit_number}")
