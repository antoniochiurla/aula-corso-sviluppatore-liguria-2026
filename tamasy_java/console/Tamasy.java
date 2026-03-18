import java.util.ArrayList;
import java.util.Scanner;

// --- 1. DEFINIZIONE DELLA CLASSE BASE ---
class Task {
    // Attributi
    protected String titolo;
    protected String descrizione;
    protected String stato; // In Java usiamo protected per permettere alle sottoclassi di vederlo
    protected String tipo;

    // --- 2. COSTRUTTORE ---
    public Task(String titolo, String descrizione) {
        this.titolo = titolo;
        this.descrizione = descrizione;
        this.stato = "Aperto";
        this.tipo = "Task";
    }

    // --- 4. METODI ---
    public void completa() {
        this.stato = "Completato";
        System.out.println("Notifica: Il task '" + this.titolo + "' è stato completato!");
    }

    public String visualizzaInfo() {
        return String.format("%s [%s] %s: %s", tipo, stato, titolo, descrizione);
    }
}

// --- 5. EREDITARIETÀ: BUG TASK ---
class BugTask extends Task {
    private String severita;

    public BugTask(String titolo, String descrizione, String severita) {
        super(titolo, descrizione); // Chiama il costruttore del padre
        this.severita = severita;
        this.tipo = "Bug";
    }

    // --- 6. OVERRIDING ---
    @Override
    public String visualizzaInfo() {
        return super.visualizzaInfo() + " | SEVERITÀ: " + severita;
    }
}

// --- 5. EREDITARIETÀ: FEATURE TASK ---
class FeatureTask extends Task {
    private String priorita;

    public FeatureTask(String titolo, String descrizione, String priorita) {
        super(titolo, descrizione);
        this.priorita = priorita;
        this.tipo = "Feature";
    }

    @Override
    public String visualizzaInfo() {
        return super.visualizzaInfo() + " | PRIORITÀ: " + priorita;
    }
}

// --- CLASSE PRINCIPALE (GESTORE DEL PROGRAMMA) ---
public class Tamasy {
    private static ArrayList<Task> tasks = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        boolean rimani = true;
        while (rimani) {
            mostraMenu();
            String opzione = scanner.nextLine();

            switch (opzione) {
                case "1":
                    aggiungiTask();
                    break;
                case "2":
                    listaTask();
                    break;
                case "3":
                    completaTask();
                    break;
                case "0":
                    rimani = false;
                    break;
                default:
                    System.out.println("Opzione non valida.");
            }
        }
    }

    private static void mostraMenu() {
        System.out.println("\n--- MENU TAMASY ---");
        System.out.println("1 - aggiungi task");
        System.out.println("2 - lista task");
        System.out.println("3 - completa task");
        System.out.println("0 - esci");
        System.out.print("Scegli l'opzione: ");
    }

    private static void aggiungiTask() {
        System.out.println("1 - task generico");
        System.out.println("2 - task di tipo bug");
        System.out.println("3 - task di tipo feature");
        System.out.print("Tipo di task da creare: ");
        String tipo = scanner.nextLine();

        System.out.print("Dammi il titolo: ");
        String titolo = scanner.nextLine();
        System.out.print("Dammi la descrizione: ");
        String descrizione = scanner.nextLine();

        Task nuovoTask = null;

        if (tipo.equals("1")) {
            nuovoTask = new Task(titolo, descrizione);
        } else if (tipo.equals("2")) {
            System.out.print("Dammi la severità: ");
            String severita = scanner.nextLine();
            nuovoTask = new BugTask(titolo, descrizione, severita);
        } else if (tipo.equals("3")) {
            System.out.print("Dammi la priorità: ");
            String priorita = scanner.nextLine();
            nuovoTask = new FeatureTask(titolo, descrizione, priorita);
        }

        if (nuovoTask != null) {
            tasks.add(nuovoTask);
            System.out.println("Task aggiunto con successo.");
        }
    }

    private static void listaTask() {
        if (tasks.isEmpty()) {
            System.out.println("Nessun task in lista.");
            return;
        }
        for (int i = 0; i < tasks.size(); i++) {
            System.out.println(i + " - " + tasks.get(i).visualizzaInfo());
        }
    }

    private static void completaTask() {
        listaTask();
        if (tasks.isEmpty()) return;

        System.out.print("Dammi l'indice del task da completare: ");
        try {
            int indice = Integer.parseInt(scanner.nextLine());
            if (indice >= 0 && indice < tasks.size()) {
                Task t = tasks.get(indice);
                t.completa();
                System.out.println(t.visualizzaInfo());
            } else {
                System.out.println("Indice non valido.");
            }
        } catch (NumberFormatException e) {
            System.out.println("Errore: Inserisci un numero valido.");
        }
    }
}