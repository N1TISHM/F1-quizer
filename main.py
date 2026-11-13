import streamlit as st

questions=("who won the 2026 sau paulo grand prix?",
          "who has won the most WDC's?",
          "Who has won the WDC in 2026",
          "Who was the F1 driver who had defeated Prime lewis Hamilton by winning the WDC in 2016",
          "What year has Max Verstappen made his debut to redbull racing?",
          "what F1 team was audi called previously?",
          "who is known as 'honeybadger' in F1",
          "what f1 team had redbull purchased to make their debut in F1",
          "who had crashed during the final laps at abu dhabhi gp in 2021 which caused a huge mess and a major reason for lewis not winning",
          "which f1 driver had crashed during bahrain gp caused a really big fire and a horrible crash and was alive covered with flames")


options=(("A. Max Verstappen","B. Carloz Sainz ","C. Lando Norris","D. Oscar Piastri"),
         ("A. Lewis Hamilton","B. Michael Schumacher","C. Sebastian Vettel","D. Both A and B"),
         ("A. Latifi","B. Fernado Alonso","C. Lance Stroll","D. Kimi Antionelli"),
         ("A. Max Verstappen","B. Sebastian Vettel","C. Nico Rosberg","D. Vallteri Bottas"),
         ("A. 2017","B. 2016","C. 2018","D 2020"),
         ("A. Kick Sauber","B. Renault","C. alfa Romeo","D. Jaguar"),
         ("A. Allan Prost","B. Daniel Riccardo","C. Alex Albon","D. Ollie Bearman"),
         ("A. Brabham","B.Lotus","C. Maserati","D. Jaguar"),
         ("A. Checo Perez","B. Lance stroll","C. Latifi","D. Yuki Tsunoda"),
         ("A. Roman Grosjean","B. Nico Hulkenberg","C. Jack Doohan","D. Franco Colapinto"))


answers=("C","D","D","C","B","A","B","D","C","A")

guesses=[]

score=0

question_num=0

st.title("-------------- 🎌Are u a true F1 fan? ---------------------")
print( )
print("------------------if correct = 🥬----------------------------")
print("------------------if wrong = 🍎--------------------------------")

print( )



for question in questions:
    print("------------------------------------------------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter ur option: ").upper().strip()
    guesses.append(guess) 

    if guess not in  ["A","B","C","D" , "a","b","c","d"]:
               print("invalid input kiddo!!")
               print("we aint continuing restart!!")
               break 

    if guess == answers[question_num]: 
     score += 1
     print("CORRECTO!! 🥬🥬🥬🥬")
    else:
       print("SERIOUSLY??? pffftt INCORRECT!!!!!  🍎🍎🍎🍎")
       print(f"{answers[question_num]} <--- OBVIOUSLYY!! ITS THISS!!!!")
    question_num +=1




print( )
print( )
print("-----TIME TO JUDGE YOU 😁😁-----")
print(" correcto answers!!: ",end="")
for answer in answers:
   print(answer, end= " ")
print()

print(" ur guesses: ",end="")
for guess in guesses:
   print(guess,end=" ")
print()

score = int(score/len(questions)*100)
print(f"your score is:{score}%")

if(score<=50):
   print("U probably are a larper or a Drunk F1 fan")
elif(score<80 and score>50):
   print("U are probably new to F1 ")
elif(score>=80 and score<100):
   print("U are qualifed to watch a race with me and can call urself an f1 fan!!!")      


