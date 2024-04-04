import sys
sys.setrecursionlimit(5000)

def FactLoop(x):
    tot = 0
    tot += x
    if x <= 3: return x
    return x * FactLoop(x-3)

def main():
    x = 9669
    FactLoop(x)

if __name__ == "__main__":
    main()

