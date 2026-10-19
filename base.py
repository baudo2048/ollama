import ollama

print("Invio della richiesta a Ollama in corso...")

response = ollama.chat(model='phi3', messages=[
  {
    'role': 'user',
    'content': 'Dimmi una curiosità breve sullo spazio in italiano.',
  },
])

print("\nRisposta ricevuta:")
print(response['message']['content'])