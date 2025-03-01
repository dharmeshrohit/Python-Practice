import sys

class InvalidAnswerException(Exception):
    pass

def get_answer(question, options):
    while True:
        try:
            print(question)
            print(options)
            answer = input("Enter your answer: ").strip().upper()
            if answer not in ["A", "B", "C", "D"]:
                raise InvalidAnswerException("Invalid input. Please enter A, B, C, or D." + "\n")
            return answer
        except InvalidAnswerException as e:
            print(e)

# Main program logic
try:
    # Question 1
    question1 = "Question 1: What is the capital of India?"
    options1 = ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"]
    answer1 = get_answer(question1, options1)
    if answer1 == "A":
        print("Correct answer. You won Rs.1000" + "\n")
    else:
        print("Wrong answer. You lost the game.")
        sys.exit()

    # Question 2
    question2 = "Question 2: Which planet is known as the Red Planet?"
    options2 = ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"]
    answer2 = get_answer(question2, options2)
    if answer2 == "B":
        print("Correct answer. You won Rs.1000" + "\n")
    else:
        print("Wrong answer. You lost the game.")
        sys.exit()

    # Question 3
    question3 = "Question 3: Who wrote the national anthem of India?"
    options3 = ["A. Rabindranath Tagor", "B. Bankim Chandra Chatterjit", "C. Sarojini Naidu", "D. Mahatma Gandhi"]
    answere3 = get_answer(question3, options3)
    if answere3 == "A" :
        print ( "Correct answer. You won Rs.3000" + "\n")
    else:
        print("Wrong answer. You lost the game.")
        sys.exit()

    # Question 4
    question4 = "Question 4: What is the largest mammal in the world?"
    options4 = ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"]
    answere4 = get_answer(question4, options4)
    if answere4 == "B" :
        print ( "Correct answer. You won Rs.5000" + "\n")
    else:
        print("Wrong answer. You lost the game.")
        sys.exit()

    # Question 5
    question5 = "Question 5: Which is the longest river in the world?"
    options5 = ["A. Amazon", "B. Nile", "C. Ganges", "D. Yangtze"]
    answere5 = get_answer(question5, options5)
    if answere5 == "B" :
        print ( "Correct answer. You won Rs.10,000" + "\n")
    else:
        print("Wrong answer. You lost the game.")
        sys.exit()

    # Question 6
    question6 = "Question 6: Who is the author of the Harry Potter series?"
    options6 = ["A. Stephen King", "B. J.K. Rowling", "C. George R.R. Martin", "D. Dan Brown"]
    answere6 = get_answer(question6, options6)
    if answere6 == "B" :
        print ( "Correct answer. You won Rs.20,000" + "\n")
    else:
        print("Wrong answer. You lost the game.")
        sys.exit()

    # Question 7
    question7 = "Question 7: What is the chemical name for table salt?"
    options7 = ["A. Calcium Carbonate", "B. Magnesium Sulfate", "C. Potassium Chloride", "D. Sodium Chloride"]
    answer7 = get_answer(question7, options7)
    if answer7 == "D":
        print("Correct answer. You won Rs.40,000" + "\n")
    else:
        print("Wrong answer. You lost the game.")
        sys.exit()

    # Question 8
    question8 = "Question 8: The book 'The Origin of Species' was written by which famous scientist?"
    options8 = ["A. Isaac Newton ", "B. Albert Einstein", "C. Charles Darwin", "D. Galileo Galilei"]
    answer8 = get_answer(question8, options8)
    if answer8 == "C":
        print("Correct answer. You won Rs.80,000" + "\n")
    else:
        print("Wrong answer. You lost the game.")
        sys.exit()

    # Question 9
    question9 = "Question 9: Which is the largest gland in the human body?"
    options9 = ["A. Pancreas", "B. Liver", "C. Thyroid", "D. Adrenal"]
    answer9 = get_answer(question9, options9)
    if answer9 == "B":
        print("Correct answer. You won Rs.1,60,000" + "\n")
    else:
        print("Wrong answer. You lost the game.")
        sys.exit()

     # Question 10
    question10 = "Question 10: The Nobel Peace Prize is awarded in which city?"
    options10 = ["A. Stockholm", "B. Geneva", "C. Vienna", "D. Oslo"]
    answer10 = get_answer(question10, options10)
    if answer10 == "D":
        print("Correct answer. 7 crorrrrrreeeeeeeeee yeeeeeee....."  + "\n")
    else:
        print("Wrong answer. You lost the game.")
        sys.exit()
        
        
except SystemExit:
    print("Better luck next time. Thank you for playing!")