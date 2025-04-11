from datetime import date, datetime

def menu_utente():
    print("\nMenu Assistente Virtuale")
    print("1. Qual è la data di oggi?")
    print("2. Che ore sono?")
    print("3. Come ti chiami?")
    print("4. Esci\n")

def assistente_virtuale(comando):
    if comando == "1":
        oggi = date.today()
        risposta = "\n --> La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "2":
        ora_attuale = datetime.now()
        risposta = "\n --> L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "3":
        risposta = "\n --> Mi chiamo Assistente Virtuale."
    elif comando == "4":
        return None
    else:
        risposta = "\n --> Comando non valido. Inserisci un numero da 1 a 4."
    return risposta

while True:
    menu_utente()
    comando = input("Inserisci il numero del comando: ").strip()

    risposta = assistente_virtuale(comando)

    if risposta is None:
        print("Arrivederci!\n")
        break
    else:
        print(risposta)











        