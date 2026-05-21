package it.corso.tamasy;

import java.util.*;
import java.io.*;

public class TaMaSyApp {
    private static final String FILE_DB = "tamasy_data.txt";
    private static List<Task> mieiTask = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        caricaTutto();
        
        while (true) {
            System.out.println("\n--- TAMASY JAVA MENU ---");
            System.out.println("1. Lista Task | 2. Aggiungi | 3. Modifica | 4. Rimuovi | 5. Toggle Stato | 6. Esci");
            System.out.print("Scegli: ");
            String scelta = scanner.nextLine();

            switch (scelta) {
                case "1": listaTask(); break;
                case "2": aggiungiTask(); break;
                case "3": modificaTask(); break;
                case "4": rimuoviTask(); break;
                case "5": toggleStato(); break;
                case "6": System.exit(0);
                default: System.out.println("Opzione errata.");
            }
        }
    }

    private static void listaTask() {
        for (int i = 0; i < mieiTask.size(); i++) {
            System.out.println(i + ". " + mieiTask.get(i).visualizza());
        }
    }

    private static void aggiungiTask() {
        System.out.print("Tipo (1. Base, 2. Bug, 3. Feature): ");
        String tipo = scanner.nextLine();
        System.out.print("Titolo: "); String tit = scanner.nextLine();
        System.out.print("Descrizione: "); String desc = scanner.nextLine();

        if (tipo.equals("2")) {
            System.out.print("Severità: "); String sev = scanner.nextLine();
            mieiTask.add(new BugTask(tit, desc, "Aperto", sev));
        } else if (tipo.equals("3")) {
            System.out.print("Priorità: "); String prio = scanner.nextLine();
            mieiTask.add(new FeatureTask(tit, desc, "Aperto", prio));
        } else {
            mieiTask.add(new Task(tit, desc, "Aperto"));
        }
        salvaTutto();
    }

    private static void toggleStato() {
        System.out.print("Indice task: ");
        int idx = Integer.parseInt(scanner.nextLine());
        Task t = mieiTask.get(idx);
        t.setStato(t.getStato().equals("Aperto") ? "Completato" : "Aperto");
        salvaTutto();
    }

    // --- GESTIONE FILE (SIMILE A PYTHON MA PIÙ VERBOSA) ---
    private static void salvaTutto() {
        try (PrintWriter out = new PrintWriter(new FileWriter(FILE_DB))) {
            for (Task t : mieiTask) {
                out.println(t.formattaPerFile());
            }
        } catch (IOException e) {
            System.out.println("Errore salvataggio: " + e.getMessage());
        }
    }

    private static void caricaTutto() {
        File f = new File(FILE_DB);
        if (!f.exists()) return;
        try (Scanner fileScanner = new Scanner(f)) {
            while (fileScanner.hasNextLine()) {
                String[] d = fileScanner.nextLine().split("\\|");
                if (d[0].equals("TASK")) mieiTask.add(new Task(d[1], d[2], d[3]));
                else if (d[0].equals("BUG")) mieiTask.add(new BugTask(d[1], d[2], d[3], d[4]));
                else if (d[0].equals("FEATURE")) mieiTask.add(new FeatureTask(d[1], d[2], d[3], d[4]));
            }
        } catch (FileNotFoundException e) {
            System.out.println("File non trovato.");
        }
    }
    
    // Altri metodi (rimuovi, modifica) seguono la stessa logica del set/remove della lista
    private static void rimuoviTask() {
        System.out.print("Indice da rimuovere: ");
        int idx = Integer.parseInt(scanner.nextLine());
        mieiTask.remove(idx);
        salvaTutto();
    }

    private static void modificaTask() {
        System.out.print("Indice da modificare: ");
        int idx = Integer.parseInt(scanner.nextLine());
        System.out.print("Nuovo titolo: "); mieiTask.get(idx).setTitolo(scanner.nextLine());
        System.out.print("Nuova desc: "); mieiTask.get(idx).setDescrizione(scanner.nextLine());
        salvaTutto();
    }
}