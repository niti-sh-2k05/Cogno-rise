import random
def game():
     users_choice=input("Enter your choice:").lower()
     computers_choice=random.choice(['scissor','rock','paper'])
    
     print("User choice=",users_choice)
     print("Computer's choice=",computers_choice)
     
     if((users_choice=='rock' and computers_choice=='scissor')):
         print("User wins!")
     
     elif((users_choice=='scissor' and computers_choice=='paper')):   
         print("User wins!")
     
     elif((users_choice=='paper' and computers_choice=='rock')):   
         print("User wins!") 
     
     elif((users_choice=='paper' and computers_choice=='paper')or(users_choice=='rock' and computers_choice=='rock')or(users_choice=='scissor' and computers_choice=='scissor')):   
         print("It's a Tie!")    
     else:
         print("Computer wins!")
game()