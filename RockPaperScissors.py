import random

def determine_winner(user_choice):
    computer_choice=random.choice(['rock', 'paper', 'scissors'])
    if user_choice==computer_choice:
        return "It's a tie!"
    elif (user_choice=='rock' and computer_choice=='scissors'
    ) or (user_choice=='scissors' and computer_choice=='paper'
    ) or (user_choice=='paper' and computer_choice=='rock'):
        print("You win!")
    else:
        print("You lose!")
        
print("Rock, Paper, Scissors!")
while True:
    user_choice=input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input!")
        continue
    determine_winner(user_choice)
    again=input("Do you want to play again? (y/n): ").lower()
    if again!='y':
        print("Thanks for playing!")
        break
