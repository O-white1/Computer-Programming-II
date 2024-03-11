def getRad():
    rad = int(input("Enter Radius: "))
    return rad
def Calc(rad):
    area = 2 * 3.14159 * rad
    circ = (3.14159 * rad)**2
    print("Area: ", area, "\nCircumference: ", circ)

Calc(getRad(rad))