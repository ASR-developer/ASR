print("ESECUZIONE AVVIATA CON SUCCESSO")
print("#TESTATO")

nome = input("ASR:Ciao,sono ASR,modello 1.1,come ti chiami? ")
while True:
    età = input("ASR:" + nome + ",voglio farti un altra domanda,quanti anni hai? ")
    if età.isdigit():
        età = int(età)
        break
    else:
        print("ASR:ERRORE=LA RISPOSTA CONTIENE UN CARATTERE CHE NON È UN NUMERO! ")
if età <= 13:
    print ("ASR:ah,allora sei un bambino. ")
elif età >= 18:
    print ("ASR:ah,allora sei un adulto. ")
else:
    print("ASR:ah,allora sei un adolescente. ")
nazionalità = input("e invece dimmi,da dove vieni? ")
RISPOSTA00001 = input("ASR:che bel posto,ti piace il posto da cui vieni? ")
RISPOSTA00002 = input("ASR:ok,c'è altro che vuoi raccontarmi? ")

RISPOSTASCELTA1 = input("ASR:ah,ok,va bene.io invece ti racconto che NON sono un AI,sono un programma che risponde con le risposte che gli sono state preimpostate,programmato interamente da Edward Regillo,se vuoi interrompere qui la conversazione,digita 1,altrimenti scrivi altro. ")
if RISPOSTASCELTA1 == "1":
    print("ASR:ok,allora arrivederci.")
else:    
    RISPOSTA00003 = input("ASR:va bene,allora continuiamo a parlare,sei un maschio o una femmina? ")

    while True:
        RISPOSTASCELTA2 = input("ASR:adesso scegli tra A,B,C oppure D,se digiti A,ti spiego cos'è la luna,se digiti B ti spiego con cosa mi hanno programmato,se digiti C,la conversazione termina e se digiti D ti faccio vedere il tuo profilo. ")
        if RISPOSTASCELTA2 == "A" or RISPOSTASCELTA2 == "a":
            print("ASR:la luna è il satellite naturale della Terra,infatti gira intorno alla terra. ")
        elif RISPOSTASCELTA2 == "B" or RISPOSTASCELTA2 == "b":
            print("ASR:Edward regillo mi ha programmato usando google colab. ")
        elif RISPOSTASCELTA2 == "C" or RISPOSTASCELTA2 == "c":
            print("ASR:ok,arrivederci. ")
            break
        elif RISPOSTASCELTA2 == "D" or RISPOSTASCELTA2 == "d":
            print("ASR:ecco il tuo profilo:ti chiami", nome, "e hai", età, "anni.")
        else:
            print("ASR:ERRORE=PUOI SCEGLIERE SOLO UNA DI QUELLE 4 LETTERE,NON SCRIVERE NIENTE DI DIVERSO! ")