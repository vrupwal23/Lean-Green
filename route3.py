from functions import die_or_live
from functions import is_correct3
from functions import is_correct2
from route1 import route_1

def route_3():
  print("You were able to jump over the rapids and continue your journey. Traveling upstream you are met with another challenge. A nearby chemical factory has its drainage outlet into the river. You have been poisoned by the toxic chemicals. You are now halfway to where you will lay your eggs. You are far from the sea and now the water temperature that you are used to is much hotter. You have a 20% chance of dying of heatstroke. Enter 1 to run the simulation. \n1- Run the simulation\n ")
  userInput2= int(input("Please enter 1:\t"))
  userInput2 = is_correct3(userInput2)
  outcome = die_or_live()
  if(outcome == 3):
    print("You have died of a heatstroke. The End.")
  else:
    print("You are not affected by the heat. You countinue your journey upstream. You are getting weaking because of the toxics in your body. You have a 40% chance of dying due to the toxins. Enter 1 to run the simulation. \n1- Run the simulation\n ")
    userInput2= int(input("Please enter 1:\t"))
    userInput2 = is_correct3(userInput2)
    outcome = die_or_live()
    if(outcome == 1 or outcome == 5):
      print("You have died becuase of the toxic buildup. The End.")
    else:
      print("You luckly did not die, but the toxins are still in your body. You swim upstream coming to anouther set of rapids. To jump up the rapids you have to roll a number higher than 9. Or you wait and can roll to survive the night near the rapids. \n1- Roll to jump\n2- Roll to survive the night\n")
      userInput2= int(input("Pick one of the numbers from above:\t"))
      userInput2 = is_correct2(userInput2)
      if(userInput2 == 1):
        route_1(userInput2)
      else:
        print("You chose to wait around. Your chances to be eaten by an eagle have greatly increased. Roll a die to see if you survived the night or to jump. If you get higher than 6 then you survive. \n1- Roll to jump\n2- Roll to survive the night\n")
        userInput2= int(input("Pick one of the numbers from above:\t"))
        userInput2 = is_correct2(userInput2)
        route_1(userInput2)
  pass
