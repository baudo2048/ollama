import subprocess
import sys

def elabora_testo(testo):
    testo_processato = ""
    
    try:
        comando = ["ollama", "run", "myterminal"]
        print(f"⏳ Esecuzione comando bash in streaming...", file=sys.stderr)
        
        # Usiamo Popen per avviare il processo e interagire con i flussi in tempo reale
        processo = subprocess.Popen(
            comando,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            bufsize=1  # Line buffered
        )
        
        # Inviamo il testo trascritto al processo tramite il suo standard input e chiudiamo lo stream
        # (questo evita che il comando rimanga in attesa di altro input all'infinito)
        processo.stdin.write(testo)
        processo.stdin.flush()
        processo.stdin.close()
        
        testo_processato = processo.stdout.read()
            
        # Attendiamo la chiusura del processo
        processo.wait()
        
        # Controlliamo se ci sono stati errori
        if processo.returncode != 0:
            errori = processo.stderr.read()
            if errori:
                print(f"\n❌ Errore dal comando: {errori}", file=sys.stderr)
                
    except FileNotFoundError:
        print("❌ Errore: Il comando 'ollama' non è stato trovato.", file=sys.stderr)
    except Exception as e:
        print(f"\n❌ Errore imprevisto: {e}", file=sys.stderr)
        
    return testo_processato.strip()