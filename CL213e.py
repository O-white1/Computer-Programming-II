class AgesAndStuff():
    #def __init__(self, age):
       # self.age = age

    def Doit():
        i = 0
        j = 0
        k = 0
        l = 0
        m = 0
        with open("Langdat\prog213e.txt") as f:
            for line in f:
                if line < 20: i += 1
                elif 20 <= line <= 39: j += 1
                elif 39 < line <= 59: k += 1
                elif 59 < line <= 79: l += 1
                elif 79 < line: m += 1
            pi = i / 50
            pj = j / 50
            pk = k / 50
            pl = l / 50
            pm = m / 50

            print("Age Group   Distribution   percentage")
            print("20            ", i, "          ", pi)