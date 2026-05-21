package it.corso.tamasy;

public class Task {
    protected String titolo;
    protected String descrizione;
    protected String stato;

    public Task(String titolo, String descrizione, String stato) {
        this.titolo = titolo;
        this.descrizione = descrizione;
        this.stato = stato;
    }

    public String visualizza() {
        return "[" + stato + "] " + titolo + ": " + descrizione;
    }

    public String formattaPerFile() {
        return "TASK|" + titolo + "|" + descrizione + "|" + stato;
    }

    // Getters e Setters (Necessari in Java per l'incapsulamento professionale)
    public void setStato(String stato) { this.stato = stato; }
    public String getStato() { return stato; }
    public void setTitolo(String titolo) { this.titolo = titolo; }
    public void setDescrizione(String descrizione) { this.descrizione = descrizione; }
}