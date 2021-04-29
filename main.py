rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
import inquirer
questions = [
  inquirer.List('pick',
                message="Select your choise",
                choices=['rock', 'paper', 'scissors'],
               
            ),
]
play_again = [
  inquirer.List('pick',
                message="Play again",
                choices=['yes',"no"],
                ),
]
game_over = False
while not game_over:
  Player_choise = inquirer.prompt(questions)

  Player_choise =Player_choise.get('pick')

  cpu_picks = ["Rock", "Paper", "Scissors"]

  Images = [rock, paper, scissors]

  def image_return(choise):
    
    if choise == "rock":
      return 0
    elif choise == "paper":
      return 1
    elif choise == "scissors":
      return 2
      

  # while True:
  #   try:
  #     Player_choise = input("Input Rock Paper or Scissors \n\n-->>").lower()
  #     if Player_choise == "rock" or Player_choise == "paper" or Player_choise == "scissors":
  #       break
  #     else:
  #       print("Please enter a correct input")
  #   except:    
  #     continue
    
  cpu_choise = cpu_picks[random.randint(1,3)-1].lower()



  if Player_choise == cpu_choise:
    res = f"You picked {Player_choise} and the computer picked {cpu_choise} draw"
    print("You picked " + Player_choise)
    print(Images[image_return(Player_choise)])
    print("Computer picked " + cpu_choise)
    print(Images[image_return(cpu_choise)])
    print("It's as draw")
  elif Player_choise == "rock" and cpu_choise == "scissors":
    # res = f"You picked {Player_choise} and the computer picked {cpu_choise} you win"
    print("You picked " + Player_choise)
    print(Images[image_return(Player_choise)])
    print("Computer picked " + cpu_choise)
    print(Images[image_return(cpu_choise)])
    print("You Win")
  elif Player_choise == "paper" and cpu_choise == "rock":
    # res = f"You picked {Player_choise} and the computer picked {cpu_choise} you win"
    print("You picked " + Player_choise)
    print(Images[image_return(Player_choise)])
    print("Computer picked " + cpu_choise)
    print(Images[image_return(cpu_choise)])
    print("You Win")
  elif Player_choise == "scissors" and cpu_choise == "paper":
    # res = f"You picked {Player_choise} and the computer picked {cpu_choise} you win"
    print("You picked " + Player_choise)
    print(Images[image_return(Player_choise)])
    print("Computer picked " + cpu_choise)
    print(Images[image_return(cpu_choise)])
    print("You Win")
  else:
    # res = f"You picked {Player_choise} and the computer picked {cpu_choise} you loose"
    print("You picked " + Player_choise)
    print(Images[image_return(Player_choise)])
    print("Computer picked " + cpu_choise)
    print(Images[image_return(cpu_choise)])
    print("You loose")

  play_again_question  = inquirer.prompt(play_again)
  play_again_question = play_again_question.get('pick')
  if play_again_question == "no":
    print("Goodbye")
    game_over = True
    


