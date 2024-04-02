import sys
sys.setrecursionlimit(5000)

def FactLoop():
    prod = 1
    for i in range(9669, 3, -3):
        prod += i
    print(prod)

def main():
    FactLoop()

if __name__ == "__main__":
    main()