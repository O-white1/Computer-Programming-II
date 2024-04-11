import sys
sys.setrecursionlimit(5000)
def FactLoop(x):
    if x >= 9669: return x
    return x + FactLoop(x+3)
def main():
    x = FactLoop(3)
    print(x)

if __name__ == "__main__":
    main()

