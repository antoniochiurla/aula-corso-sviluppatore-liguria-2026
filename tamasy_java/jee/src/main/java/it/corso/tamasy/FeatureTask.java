package it.corso.tamasy;

public class FeatureTask extends Task {
    private String priorita;

    public FeatureTask(String titolo, String descrizione, String stato, String priorita) {
        super(titolo, descrizione, stato);
        this.priorita = priorita;
    }

    @Override
    public String visualizza() {
        return super.visualizza() + " ⭐ FEAT (" + priorita + ")";
    }

    @Override
    public String formattaPerFile() {
        return "FEATURE|" + titolo + "|" + descrizione + "|" + stato + "|" + priorita;
    }
}