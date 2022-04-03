from functions import is_correct1
from functions import is_correct2
from functions import is_correct3
from functions import roll_two_dice
from route2 import route_2

print("Ready to play?")
userInput1 = input("Yes or No?\t")
userInput1 = is_correct1(userInput1)
print("Wild Salmons have to make a perilous journey reaching your plate, facing killer whales, seals, bears, eagles, kingfishers, and human activities. We'll start our journey in the Bering Sea by the Kuskolwin bay. Would you like to swim right or left. \n1-Right\n2-Left\n")
userInput2= int(input("Pick one of the numbers from above:\t"))
userInput2 = is_correct2(userInput2)
if(userInput2 == 1):
  print("You swim right and into a floating pile of plastics. Your fin gets stuck in a piece of pastic. Would you like to wrangle out of the grips of the plastic or keep it on? \n1-Wrangle Out\n2-Keep on it\n")
  userInput2= int(input("Pick one of the numbers from above:\t"))
  userInput2 = is_correct2(userInput2)
  if(userInput2 == 1):
    print("To take off the plastic around your fin you have to roll two dice to get a sum more than 6. Would you like to roll or keep it on? \n1- Roll\n2-Keep it on\n")
    userInput2= int(input("Pick one of the numbers from above:\t"))
    userInput2 = is_correct2(userInput2)
    while (userInput2 == 1):
      diceRolloutcome = roll_two_dice()
      if (diceRolloutcome < 9):
        print("You got {:.0f}, which is not high enough of a roll to take of the plastic. Would you like to roll or keep it on? \n1- Roll\n2-Keep it on\n".format(diceRolloutcome))
        userInput2= int(input("Pick one of the numbers from above:\t"))
        userInput2 = is_correct2(userInput2)
        if(userInput2 == 2):
          print("You couldn't get the plastic off your fin and it is not stuck to your fin. Your chances to die have greatly increased.")
      else:
        print("You got {:.0f}, which is enough to take off the plastic. Now you are free from the plastic on your fin.".format(diceRolloutcome))
        userInput2 = 2
    print("You keep on swimming towards the mouth of the Kuskokwim river, ready to embark on your journey upstream. As you swim through the harbor you encounter some seals. This is one of the first predators you will face o1n your journey. Roll the dice to see if you can escape the seals.\n1-Roll")
    userInput2= int(input("Please enter 1:\t"))
    userInput2 = is_correct3(userInput2)
    diceRolloutcome = roll_two_dice()
    if (diceRolloutcome > 3):
      print("You escaped the seal. You now start your journey upstream, battling the current. After traveling for two days continuously you reach the first rapids on your journey. To jump up the rapids you have to roll a number higher than 6. Or you wait and can roll to survive the night near the rapids. \n1- Roll to jump\n2- Roll to survive the night\n")
      userInput2= int(input("Pick one of the numbers from above:\t"))
      userInput2 = is_correct2(userInput2)
      if(userInput2 == 1):
        route_2(userInput2)
      else:
        print("You chose to wait around. Your chances to be eaten by a bear have greatly increased. Roll a die to see if you survived the night or to jump. If you get higher than 6 then you survive. \n1- Roll to jump\n2- Roll to survive the night\n")
        userInput2= int(input("Pick one of the numbers from above:\t"))
        userInput2 = is_correct2(userInput2)
        route_2(userInput2)
    else:
      print("You were eaten by the seal. The End.")
  else:
    print("You couldn't get the plastic off your fin and it is not stuck to your fin. Your chances to die have greatly increased. You keep on swimming towards the mouth of the Kuskokwim river, ready to embark on your journey upstream. As you swim through the harbor you encounter some seals. This is one of the first predators you will face on your journey. Roll the dice to see if you can escape the seals.\n1-Roll")
    userInput2= int(input("Please enter 1:\t"))
    userInput2 = is_correct3(userInput2)
    diceRolloutcome = roll_two_dice()
    if (diceRolloutcome > 3):
      print("You escaped the seal. You now start your journey upstream, battling the current. After traveling for two days continuously you reach the first rapids on your journey. To jump up the rapids you have to roll a number higher than 6. \n1- Roll to jump\n2- Roll to survive the night\n")
      userInput2= int(input("Pick one of the numbers from above:\t"))
      userInput2 = is_correct2(userInput2)
      if(userInput2 == 1):
        route_2(userInput2)
      else:
        print("You chose to wait around. Your chances to be eaten by a bear have greatly increased. Roll a die to see if you survived the night or to jump. If you get higher than 6 then you survive. \n1- Roll to jump\n2- Roll to survive the night\n")
        userInput2= int(input("Pick one of the numbers from above:\t"))
        userInput2 = is_correct2(userInput2)
        route_2(userInput2)
    else:
      print("You were eaten by the seal. The End. ")
else:
  print("You keep on swimming towards the mouth of the Kuskokwim river, ready to embark on your journey upstream. As you swim through the harbor you encounter some killer whales. This is one of the first predators you will face on your journey. Roll the dice to see if you can escape the killer whales.\n1- Roll to survive\n")
  userInput2= int(input("Pick one of the numbers from above:\t"))
  userInput2 = is_correct2(userInput2)
  diceRolloutcome = roll_two_dice();
  if (diceRolloutcome > 4):
    print("You escaped the killer whale. You now start your journey upstream, battling the current. After traveling for two days continuously you reach the first rapids on your journey. To jump up the rapids you have to roll a number higher than 6. \n1- Roll to jump\n2- Roll to survive the night\n")
    userInput2= int(input("Pick one of the numbers from above:\t"))
    userInput2 = is_correct2(userInput2)
    route_2(userInput2)
  else:
    print("You were eaten by the killer whale. The End.")
        
    
