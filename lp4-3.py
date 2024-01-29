eggs = int(input("Number of eggs: "))
dozens = eggs//12
rem = eggs % 12
ppd = 0
if 0 < dozens <= 4:
  ppd = 0.50
elif 4 < dozens <= 6:
  ppd = 0.45
elif 6 < dozens <= 11:
  ppd = 0.40
elif dozens > 11:
  ppd = 0.35
print("Total Cost is: $" + str(ppd * dozens) + str((ppd/12) * (rem)))