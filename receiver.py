import sys
from executor import elabora_testo

def ricevi_dati():
    #print("⏳ Ricevitore in attesa di dati dal microfono...", file=sys.stderr)
    
    # Legge continuamente dallo standard input (pipe)
    for line in sys.stdin:
        # Rimuove spazi vuoti o a capo extra
        testo_ricevuto = line.strip()
        
        if testo_ricevuto:
            risultato = elabora_testo(testo_ricevuto)
            print(f"📥 Ricevuto dallo script 2: --> {risultato}")
            
            # --- QUI PUOI AGGIUNGERE LA TUA LOGICA ---
            # Esempio: se ricevi "spegni", fai qualcosa
            if "spegni" in testo_ricevuto.lower():
                print("🛑 Comando di spegnimento rilevato!")
                break

if __name__ == "__main__":
    try:
        ricevi_dati()
    except KeyboardInterrupt:
        print("\nRicevitore chiuso.")