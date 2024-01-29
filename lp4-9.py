from random import randint
x = randint(1, 21)
y = int(input("guess a number 1-20:"))
if x ==y:
  print("Yahoo, go you")
else: print("you suck")