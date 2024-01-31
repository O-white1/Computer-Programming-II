num1 = abs(int(input("Enter A non Negative number: ")))
num2 = abs(int(input("Enter another non Negative number: ")))
while num2 > 0:
  temp = num1 % num2
  num1 = num2
  num2 = temp
  print(str(temp))