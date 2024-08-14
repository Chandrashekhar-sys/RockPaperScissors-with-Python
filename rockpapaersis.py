import random

print('Welcome to this place:\n'
      + "Come here to cure your boredom?\n"
      + "What better than a good old game of Rock Paper Scissors!"
     )
name=input("What's your name:")
print("Nice name you got there:", name)
user=0      #initializing counts
comp=0      #...
draw=0      #...

while True:                                                  #true statement going ahead and executing

    print("Enter your choice: \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice :"))

    while choice > 3 or choice < 1:
        choice = int(input('Stick to the rules please!'))    #checking and giving warning to user for invalid output

    if choice == 1:
        choice_name = 'ROCK'
    elif choice == 2:
        choice_name = 'PAPER'
    else:
        choice_name = 'SCISSORS'
    print(name+"'s", 'choice is... :' , choice_name)
    
    comp_choice = random.randint(1, 3)  #random valude of range 1 to 3

    while comp_choice == choice:        #looping till value sets from 1 to 3 both from user and computer 
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'ROCK'
    elif comp_choice == 2:
        comp_choice_name = 'PAPER'
    else:
        comp_choice_name = 'SCISSORS'
    print("Computer choice is... :", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    if choice == comp_choice:  # Draw condition
        print('It\'s a Draw!\n')
        draw += 1
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):   #win condition 1
        print('Paper wins!\n')
        result = 'PAPER'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):   #win condition 2
        print('Rock wins!\n')
        result = 'ROCK'
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):   #win condition 3
        print('Scissors wins!\n')
        result = 'SCISSORS'

    if (choice == 1 and result == 'ROCK') or (choice == 2 and result == 'PAPER') or (choice == 3 and result == 'SCISSORS'):  #user wins
        print("<== " + name + " wins! ==>")
        user += 1
    elif choice != comp_choice:       #computer wins
        print("<== Computer wins! ==>")
        comp += 1

    print("Do you want to play again? (yup/nope)")           #ask for loop
    ans = input().lower()
    if ans == 'yup':
        continue
    elif ans == 'nope':
        print('Final result:\n')
        print(name + "'s score: " + str(user) + "   ||   computer's score: " + str(comp) + '\n')
        break
    else:
        print("Type the specific keyword to continue!")
        break
    print("Do you want to play again? (yup/nope)")
    # if user input (nope) then condition is True
    ans = input().lower()
    if ans == 'yup':
        continue
    elif ans == 'nope':
        print('Final result:\n')
        print(name +"'s score: " + str(user) + "   ||   computer's score: " + str(comp) + '\n')
        break
    else:
        print("Type the specific keyword to continue!")
        break
if (user>comp):
    print("Great! Well Done you really beat it!")
elif (user<comp):
    print("Better Luck Next time!")
else:
    print("Woah it was a tough competition! its a DRAW!")

print("Thanks for playing")