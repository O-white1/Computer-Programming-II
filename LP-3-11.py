print("Enter time spent in the following categories: Designing // Coding // Testing //  Debugging //")
des =int(input("Designing: "))
cod =int(input("Coding:    "))
tes =int(input("Testing:   "))
deb =int(input("Debugging: "))
total = des+cod+tes+deb
scaler = 100 / total
print("Designing: ",    scaler * des, "%")
print("Coding:    ",    scaler * cod, "%")
print("Testing:   ",    scaler * tes, "%")
print("Debugging: ",    scaler * deb, "%")