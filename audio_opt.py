import sys
import speech_recognition as sr

def ascolto_continuo():
    r = sr.Recognizer()
    
    # 1. Regoliamo la soglia di energia per adattarla all'ambiente
    r.energy_threshold = 150  # Puoi alzarlo se c'è molto rumore di fondo (es. 500)
    r.dynamic_energy_threshold = True
    
    # 2. AUMENTIAMO LA PAUSA DI SILENZIO
    # Di default è circa 0.8. Portandola a 3.0 o 4.0 secondi, il sistema 
    # aspetterà che tu faccia una pausa lunga (es. finire un intero paragrafo) 
    # prima di considerare la frase conclusa.
    r.pause_threshold = 1.5  
    
    # 3. Tempo massimo consentito per una singola frase/paragrafo (es. 45 secondi)
    PHRASE_TIME_LIMIT = 45

    with sr.Microphone() as source:
        #print("🔊 Calibrazione rumore in corso... Rimani in silenzio per un attimo.", file=sys.stderr)
        r.adjust_for_ambient_noise(source, duration=1.5)
        #print("🎤 PRONTO! Puoi parlare liberamente (anche interi paragrafi). Farò una pausa solo dopo 3.5 secondi di silenzio.", file=sys.stderr)
        
        while True:
            try:
                #print("🎧 In ascolto (parla pure)...", file=sys.stderr)
                
                # Cattura l'audio aspettando che l'utente finisca il discorso lungo
                audio = r.listen(source, timeout=None, phrase_time_limit=PHRASE_TIME_LIMIT)
                
                #print("🔄 Elaborazione del paragrafo in corso...", file=sys.stderr)
                
                # Invia l'intero blocco audio a Google
                testo = r.recognize_google(audio, language="it-IT")
                
                # Stampa il testo completo sulla pipe
                print(testo, flush=True)
                
            except sr.UnknownValueError:
                # Nessun parlato chiaro rilevato, si rimettere in ascolto silenziosamente
                pass 
            except sr.RequestError as e:
                print(f"❌ Errore di rete con il servizio di riconoscimento: {e}", file=sys.stderr)
            except KeyboardInterrupt:
                print("\nInterrotto dall'utente.", file=sys.stderr)
                break

if __name__ == "__main__":
    ascolto_continuo()