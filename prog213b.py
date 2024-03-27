# Prog213b.py
def main():

    with open("Langdat/prog213b.txt", "r") as f:
        q = int(input("Enter Quantity: "))

        price = 0.0
        curline = f.readline()

        if q <= 99: price = 5.95
        elif 99 < q <= 199: price = 5.75
        elif 199 < q <= 299: price = 5.40
        elif q > 299: price = 5.15
        else: print("Invalid Quantity")

        tot = price*q
        for line in f:
            q = f.readline()
            print("___________________________________")

            print("Quantity: ",q)
            print("Price: ", price)
            print(f"Total: ", tot)
            print("\n")



if __name__ == "__main__":
    main()

