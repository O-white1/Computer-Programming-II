class AgesAndStuff():
    def __init__(self, age):
        self.age = age
    def Doit(self, age):
        lessThanTwenty = 0
        twentyToThirtNnine = 0
        fourtyToFiftyNine = 0
        sixtyToSeventyNine = 0
        aboveSeventyNine = 0
        with open("Langdat\prog213e.txt") as f:
            for line in f:
                if line < 20: lessThanTwenty += 1
                elif 20 <= line <= 39: twentyToThirtNnine += 1
                elif 39 < line <= 59: fourtyToFiftyNine += 1
                elif 59 < line < 79: sixtyToSeventyNine += 1
                elif 79 < line: aboveSeventyNine += 1
            percentage = line / 50









def main():
    pass

if __name__ == "__main__":
    main()