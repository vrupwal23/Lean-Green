import random

def is_correct1(a):
  while (not(a == "Yes" or a == "No")):
    a = input("Yes or No?\t")
  return a

def is_correct2(a):
  while (not(a == 1 or a == 2 )):
    a = int(input("Pick one of the numbers from above:\t"))
  return a

def is_correct3(a):
  while (not(a == 1)):
    a = int(input("Please enter 1:\t"))
  return a

def roll_two_dice():
  a = random.randrange(1,6)
  b = random.randrange(1,6)
  return a+b

def die_or_live():
  a = random.randrange(1,5)
  return a

