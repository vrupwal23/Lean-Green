from route4 import route_4
from functions import is_correct2
from functions import roll_two_dice

def route_1(userInput2):
  while (userInput2 == 1 or userInput2 == 2 ):
    if(userInput2 == 1):
      diceRolloutcome = roll_two_dice()
      if (diceRolloutcome < 6):
        print("You got {:.0f}, which is not high enough of a roll to take the jump. Would you like to roll for the jump or roll to survive? \n1- Roll to jump\n2- Roll to survive the night\n".format(diceRolloutcome))
        userInput2= int(input("Pick one of the numbers from above:\t"))
        userInput2 = is_correct2(userInput2)
        if(userInput2 == 2):
          print("You chose to wait around. Roll a die to see if you survived the night or to jump. If you get higher than 6 than you survive. \n1- Roll to jump\n2- Roll to survive the night\n")
          userInput2= int(input("Pick one of the numbers from above:\t"))
          userInput2 = is_correct2(userInput2)
          diceRolloutcome = roll_two_dice()
          if(diceRolloutcome < 6):
            print("You were eaten by an eagle. The End.")
            userInput2 = 4
          else:
            print("You survived the night. You can roll to take a jump or wait. \n1- Roll to jump\n2- Roll to survive the night\n")
            userInput2= int(input("Pick one of the numbers from above:\t"))
            userInput2 = is_correct2(userInput2)
        else:
          diceRolloutcome = roll_two_dice()
          if (diceRolloutcome < 6):
            print("You got {:.0f}, which is not high enough of a roll to take the jump. Would you like to roll for the jump or roll to survive? \n1- Roll to jump\n2- Roll to survive the night\n".format(diceRolloutcome))
            userInput2= int(input("Pick one of the numbers from above:\t"))
            userInput2 = is_correct2(userInput2)
          else:
            userInput2 = 3
      else:
        userInput2 = 3
    else:
      print("You survived the night. You can roll to take a jump or wait. \n1- Roll to jump\n2- Roll to survive the night\n")
      userInput2= int(input("Pick one of the numbers from above:\t"))
      userInput2 = is_correct2(userInput2)
      if (userInput2 == 1):
        diceRolloutcome = roll_two_dice()
        if (diceRolloutcome < 6):
          print("You got {:.0f}, which is not high enough of a roll to take the jump. Would you like to roll for the jump or roll to survive? \n1- Roll to jump\n2- Roll to survive the night\n".format(diceRolloutcome))
          userInput2= int(input("Pick one of the numbers from above:\t"))
          userInput2 = is_correct2(userInput2)
        else:
          userInput2 = 3
      else:
        diceRolloutcome = roll_two_dice()
        if(diceRolloutcome < 6):
          print("You were eaten by an eagle. The End.")
          userInput2 = 4
        else:
          print("You survived the night. You can roll to take a jump or wait. \n1- Roll to jump\n2- Roll to survive the night\n")
          userInput2= int(input("Pick one of the numbers from above:\t"))
          userInput2 = is_correct2(userInput2)
  if(userInput2 == 3):
    route_4()
