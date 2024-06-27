#create a program capable of displaying questions to the user like kbc
# Use list data type to store the questions and their correct answers
# Display the final amount the person is taking home after playing 
# the game.
'''i need to display a question to the user which has four options 
in one of them is the correct option and if the user selects the correct
option then second question is displayed and if not then he has lost the game 
and goes home'''
ques_1 = "who is the prime minister of India"
print(ques_1)
print("option 1 Narender modi ")
print("option 2 Rahul ghandhi ")
print("option 3 Sonia ghandhi")
print("option 4 Lalu yadav")
answer = input("Select the correct option ")
match answer:
    case "1":
        print("congrats you have chosen the right answer")
        print("you won the amount of 5000")
    case  _ if answer =="2"or answer=="3" or answer=="4":
        print("your answer is wrong sorry to say you did n't won anything")

if(answer=="1"):
    ques_2 ="who is the president of India"
    print(ques_2)
    print("option 1 Narender modi ")
    print("option 2 Draupati murmu ")
    print("option 3 Sonia ghandhi")
    print("option 4 Lalu yadav")
    answer2 = input("select the correct option ")
    match answer2:
     case "2":
        print("congrats you have chosen the right answer")
        print("you won the amount of 10000")
        print("your total won prize is 15000")
     case  _ if answer2 =="1"or answer2=="3" or answer2=="4":
        print("your answer is wrong and you won only 5000 ")
if(answer2 == "2"):
   ques_3 ="who is the home minister of India"
   print(ques_3)
   print("option 1 Narender modi ")
   print("option 2 Draupati murmu ")
   print("option 3 Amit shah")
   print("option 4 Lalu yadav")
   answer3 = input("select the correct option ")
   match answer3:
      case "3":
         print("congrats you have chosen the right answer")
         print("you won the amount of 20,000")
         print("your total won prize is 35000")
      case  _ if answer3 =="1"or answer3=="2" or answer3=="4":
        print("your answer is wrong and you won only 15000 ")
         
        


