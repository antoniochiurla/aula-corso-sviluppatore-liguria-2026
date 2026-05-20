from factory import CalculatorFactory

def start_app():
    calc = CalculatorFactory.create_calculator()
    print("--- Agile Scrum Calc (PyScrumCalc) ---")
    print("Inserisci operazioni (es: 5 + 3) o variabili (es: x = 10).")
    print(f"Usa '{calc.last_value_variable}' per l'ultimo risultato. Scrivi 'exit' per uscire.")

    while True:
        try:
            user_input = input("\ncalc > ").strip()
            if user_input.lower() == 'exit':
                break
            
            if not user_input:
                continue

            result = calc.evaluate(user_input)
            print(f"Risultato: {result}")
            print(f"Variabili correnti: {calc.get_variables()}")
            
        except ValueError as e:
            print(f"Errore di calcolo: {e}")
        except Exception as e:
            print(f"Errore generico: {e}")

if __name__ == "__main__":
    start_app()