
print("Welcome to South American capitals quiz!")
options=(("A.Brasilia ","B.Rio de janeiro ","C.Sao Paulo ", "D.Manaus "),
         ("A.Santa Marta ","B.Bogota ","C.Cartagena ", "D.Medellin"),
         ("A.La Serena ","B.Santiago ","C.Valparaiso ", "D.Temuco"),
         ("A.Buebos Aires ","B.Mendoza ","C.La Plata ", "D.Rosario "),
         ("A.Cusco ","B.Iquitos ","C.Lima ", "D.Arequipa "))
answers=("A","B","B","A","C")
guesses=[]
score=0
question_num=0

questions=("What is the capital of Brazil?",
           "What is the capital of Colombia?","What is the capital of Chile?"
           ,
           "What is the capital of Argentina?",
           "What is the capital of Peru?")

for x in questions:
  print("-----------------------")
  print(x)
  for option in options[question_num]:
    print(option)

  guess=input("Guess A,B,C,D!")
  if guess==answers[question_num]:
    score+=1
    print("Correct")
  else:
    print("Incorrect!")
    print("The correct answer is",answers[question_num])
  question_num+=1
print("-----------------------")
print("Congrats! Your final score was",str(score),".") 