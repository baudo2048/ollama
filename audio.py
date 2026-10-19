import speech_recognition as sr

def ascolto_continuo():
    r = sr.Recognizer()
    
    # Sensibilità e configurazioni per l'ascolto continuo
    r.pause_threshold = 0.8  # Secondi di silenzio prima di considerare finita una frase
    
    with sr.Microphone() as source:
        #print("🔊 Regolazione del rumore di fondo in corso... Attendere.")
        r.adjust_for_ambient_noise(source, duration=1)
        #print("✅ Configurazione completata!")
        #print("🎤 Il sistema è ora in ascolto continuo. Parla liberamente! (Premi Ctrl+C per uscire)\n")
        
        while True:
            try:
                #print("🎧 In ascolto...")
                # Ascolta dal microfono (senza timeout generico, attende finché non parli)
                audio = r.listen(source, phrase_time_limit=15)
                
                #print("🔄 Trascrittore in corso...")
                testo = r.recognize_google(audio, language="it-IT")
                
                print(testo, flush=True)
                
            except sr.UnknownValueError:
                # Scattato se viene rilevato del suono che il sistema non riesce a decifrare come parole
                print("⚠️  Audio non riconosciuto. Riprova a parlare.\n")
                
            except sr.RequestError as e:
                print(f"❌ Errore di rete con il servizio di riconoscimento: {e}\n")
                
            except KeyboardInterrupt:
                # Cattura la pressione di Ctrl+C per uscire in modo pulito
                print("\nInterruzione da tastiera. Chiusura dello script.")
                break

if __name__ == "__main__":
    try:
        ascolto_continuo()
    except KeyboardInterrupt:
        print("\nProgramma terminato.")