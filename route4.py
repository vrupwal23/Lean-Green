from functions import is_correct1
from functions import is_correct2
from functions import is_correct3
from functions import roll_two_dice
from functions import die_or_live

def route_4():
  print("You made through the second set of the rapids. Up the stream there are some humans fishing. Run the simulation to see if you were caught. \n1- Run the simulation\n")
  userInput2= int(input("Please enter 1:\t"))
  userInput2 = is_correct3(userInput2)
  outcome = die_or_live()
  if(outcome == 3 or outcome == 4 or outcome == 5):
    print("You have been caught by the human. The human took you and some of the other fish that were caught to the fish market to be sold as Wild Salmon. The very same salmon that could be full of toxins or have pieces of plastic in them. That same salom is them bought by you or your friends and family and can be harmful to the health.")
  else:
    print("You escaped the hooks of the fishing lines and made it to the place where you layed your eggs. This journey is faced by salmons every year when they make the trip up rivers to lay eggs. After laying the eggs the salmons die as it is time to go.")
  pass
