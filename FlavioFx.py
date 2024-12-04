### Funzioni che potrebbero essere utili in futuro
### non utili al momento 


from random import sample
from fpdf import FPDF
import os

def init_quiz():

    f = open("questions.txt", "r")                              # apre il file
    quest_numb = len(f.readlines()) // 5                        # calcola il numero di domande presenti nel file
    questions = [""] * quest_numb                               # crea una lista per le domande
    answers = [""] * quest_numb                                 # crea una lista per le risposte

    file = open("questions.txt", "r")                           # legge il contenuto del file

    for y in range ( 0, quest_numb ):                           # scrive le domande e le risposte nelle liste
        for x in range ( 0,4):
            questions[y] = questions[y] + file.readline()
        answers[y] = int(answers[y] + file.readline())

    return(questions + answers)                                 # ritorna le liste al programma main

def end_test ():
    choice = input("Digit space to continue or q to quit and press enter\n")  # chiede all'utente se vuole continuare
    if choice == "q":
        return True                
    if choice == " ":                                     
        return False
    
def play_quiz (questions,answers,lenght):
    maxscore = 10
    score = 0
    countQ = 10                                                 # ask 5 questions to the student
    numbersQ = sample(range(0,lenght // 2), countQ )            # seleziona 5 domande a caso senza ripetizioni

    for x in range (0, countQ):
        answ = int(input(questions[numbersQ[x]]))               # stampa la domanda e raccoglie la risposta
        if answ == answers[numbersQ[x]]:                        # se la risposa è corretta
            print("Well done! Answer is correct\n")             # se corretta avvisa l'utente
            score += 1                                          # aumenta lo score di un punto
        if (x < countQ-1):
            if end_test():                                      # chiede all'utente se vuoel continuare
                break
        os.system('cls')
    print("Test complete!")
    print(f"Your score is: {score} punti su {maxscore}\n")

def print_quiz (quest):                                         # stampa un pdf con il test scritto
    pdf = FPDF()                                                # inizalizza il pdf
    pdf.add_page()
    pdf.set_font("Arial", size = 10)
    
    file = open("questions.txt", "r")                           # verifica la dimensione del file
    lenght = len(file.readlines())
    file = open("questions.txt", "r")                           # copia il contenuto del file nella variabile file

    numbersQ = sample(range(0,lenght // 5), lenght // 5 )       # genera un arrai di numeri casuali. lunghezza diviso 5 perchè nel file ogni domanda occupa cinque righe ( domanda 1,risposta2-3-4.soluzione 5)
                                                                # lenght // 5 si puo sostituire con un numero intero pari alle domande che si vuole includere nel test

    for x in range(0,lenght // 5):                                                  
        testo = quest[numbersQ[x]]                              # estre una domanda dal testo
        testo = testo.split("\n")                               # splitta la domanda in una lista di 4 sringhe ( domanda 0, risp 1 risp 2 , risp 3 )
        if x % 6 == 0 and x > 0:                                # ogni 6 domande aggiunge due righe di spazio per impostare la pagina
            pdf.cell(200, 10, txt = "", ln = 1, align = 'L')
            pdf.cell(200, 10, txt = "", ln = 1, align = 'L')

        for y in range(0,4):                                    # aggiunge la domanda e le possibili risposte al pdf 
            pdf.cell(200, 10, txt = testo[y], ln = 1, align = 'L')
        
    pdf.output("Test.pdf")                                      # stampa il pdf

def quiz_add():
    while True:
        Q = input("Insert the question\n")
        file = open("questions.txt", "a")
        file.write(Q+"\n")
        file.close()
        for x in range (0,3):
            A = input(f"Insert the answer{x+1}\n")
            file = open("questions.txt", "a")
            file.write("\t "+ str(x+1) + A +"\n")
            file.close()
        S = input("Insert the solution\n")
        file = open("questions.txt", "a")
        file.write(S+ "\n")
        file.close()
        if end_test ():
            break

def quiz_add():
    
    while True:
        os.system('cls')
        Q = input("Insert the question\n")
        file = open("questions.txt", "a")
        file.write(Q+"\n")
        file.close()
        for x in range (0,3):
            A = input(f"Insert the answer{x+1}\n")
            file = open("questions.txt", "a")
            file.write("\t "+ str(x+1) + A +"\n")
            file.close()
        S = input("Insert the solution\n")
        file = open("questions.txt", "a")
        file.write(S+ "\n")
        file.close()
        if end_test ():
            break


##  AGGIUNTA FUNZIONE CHE RACCOGLIE LA RISPOSTA CHE RESTITUISCE LA FUNZIONE DI ALINA
##  E COMPARA IL RISULTATO CON LA TUPLE RISPOSTE DI GIADA


punteggio = 0
risposte = ("1","2","3","1")


def check_reply( reply,num_domanda):

    if (int(reply) == risposte[int(num_domanda)]):
        punteggio += 1
    else:
        pass
