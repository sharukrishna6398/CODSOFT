import random

rock='''
    _ _ _ _ _ _ _ _ _

_ _ _'
              _ _ _ _ )
              
             (_ _ _ _ _ _)
             
            (_ _ _ _ _ )
            
            (_ _ _ _ _)
---
     '_ __(_ _ _ _ )
     
'''

paper='''
    _ _ _ _ _ _ _ _ _

_ _ _'
              _ _ )_ _ _ 
              
             _ _ _ _ _ _ _ _)
             
            _ _ _ _ _ _ _ _ _ )
            
            _ _ _ _ _ _ _ _)
---
     '_ ___ _ _ _ _ _ _ )
     
'''

scissor='''
    _ _ _ _ _ _ _ _ _

_ _ _'
              _ _ )_ _ _ _ _
              
                _ _ _ _ _ _)
             
            _ _ _ _ _ _ _ _ )
            
            (_ _ _ _ _)
---
     '_ __(_ _ _ _ )
     
'''
game_images=[rock,paper,scissor]
user_choice=int(input("Enter your choice:Type 0 for rock,1 for paper,2 for scissors."))
if user_choice>3 or user_choice<0:
    print("You entered invalid number,You lose.")
else:
    print (game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer chose")
    print(computer_choice)
    print(game_images[computer_choice])
    if computer_choice==user_choice:
        print("It's a Draw.")
    elif computer_choice==0 and user_choice==2:
        print("You lose.")
    elif user_choice==0 and computer_choice==2:
        print("You Win.")
    elif computer_choice > user_choice:
        print("You Lose.")
    elif user_choice > computer_choice:
        print("You Win.")
    

