questions = ("what does HTML stand for?: ", 
             "which programming language is often used for web development?: ",
             "which program language is often usedd for data analysis and scientific computing?: ",
             "In python, which keyword is used to define a function?: ",
             "which data type in python isused to represenr a sequence of characters?: ")

options = (("A. Hyperlink Text Markup Language","B. Hyper Transfer Markup Language","C. Hypertext Markup Language","D. High-Level Text Markup Language" ),
           ("A. Python","B. Java","C. Ruby","D. Javascript" ),
           ("A. Javascript","B. Python","C. C++","D. Java" ),
           ("A. define ","B. func","C. def","D. function" ),
           ("A. str","B. int","C. float ","D. list " ))

answers = ("C","D","B","C","A")
guesses = []
score = 0
question_num = 0 

for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A, B, C, D): ").upper() 
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")   
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1   
    
    
print("-----------------------")
print("--------RESULTS--------")
print("-----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"your score is: {score}%")