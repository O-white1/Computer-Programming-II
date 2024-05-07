class MathFuncs():
    def __init__(self):
        pass

    def Add(num1, num2):
        return num1 + num2

    def Subtract(num1, num2):
        return num1 - num2

    def Multiply(num1, num2):
        return num1 * num2

    def Divide(num1, num2):
        return num1 / num2


def main():
    a = int(input("Enter Num: "))
    b = int(input("Enter Num: "))
    print("Sum: ",        MathFuncs.Add(a, b))
    print("Difference: ", MathFuncs.Subtract(a, b))
    print("Product",      MathFuncs.Multiply(a, b))
    print("Quotient: ",   MathFuncs.Divide(a, b))


if __name__ == "__main__":
    main()
