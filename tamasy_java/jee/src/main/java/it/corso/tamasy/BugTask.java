package it.corso.tamasy;

public class BugTask extends Task {
    private String severita;

    public BugTask(String titolo, String descrizione, String stato, String severita) {
        super(titolo, descrizione, stato);
        this.severita = severita;
    }

    @Override
    public String visualizza() {
        return super.visualizza() + " 🐞 BUG (" + severita + ")";
    }

    @Override
    public String formattaPerFile() {
        return "BUG|" + titolo + "|" + descrizione + "|" + stato + "|" + severita;
    }
}