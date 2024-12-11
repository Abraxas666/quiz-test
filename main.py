
import FlavioFx

selection = int(input(""" 
                *****************  PYTHON QUIZ V 1.0  *************************** 
                *                                                               * 
                *  Digitare 1 per avviare una prova di test                     * 
                *  Digitare 2 per aggiunger altre domande                       * 
                *  Digitare 3 per stampare un test cartaceo                     * 
                *                                                               * 
                *****************************************************************\n
                """
                ))

if selection == 1:
    print ( "Qui inseriremo la funzione che richiama il test")

questions = [
    {
        "question": "Come si chiamano i simboli < > = in python?",
        "choices": ["1. Operatori di confronto", "2. Operatori logici", "3. Metodi di confronto"],
        "answer": "1"
    },
    {
        "question": "Che operatori si usano per il controllo di flusso?",
        "choices": ["1. if, ifelse, while", "2. for, while", "3. try except"],
        "answer": "1"
    },
    {
        "question": "Nella definizione di funzione cosa viene contenuto tra le parentesi?",
        "choices": ["1. gli argomenti", "2.  i parametri", "3. le stringhe"],
        "answer": "2"
    }
]

def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        answer = input("Enter your answer:")
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")
    print(f"Your final score is {score}/{len(questions)}")

run_quiz(questions)

# if selection == 2:
#     print ( "Qui inseriremo la funzione che consente di aggiungere altre domande")
# if selection == 3:                            
#    print ( " Qui inseriremo una funzione che stampa un test cartaceo")