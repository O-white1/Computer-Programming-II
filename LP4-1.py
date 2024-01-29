copies = int(input("Numer of copies:"))
price = 0.0
if 0 < copies <= 99:
  price = 0.30
elif 99 < copies <= 499:
  price = 0.28
elif 499 < copies <= 749:
  price = 0.27
elif 749 < copies <= 1000:
  price = 0.26
elif copies > 1000:
  price = 0.25
else:
  print("Invalid number of copies!")
print("Total number of copies: $" + str(price))
print("Total number of copies: $" + str(price*copies))