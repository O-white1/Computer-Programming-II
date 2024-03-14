class Cl213f:
    def __int__(self, kwh, cost):
        self.kwh = kwh
        self.cost = 0.0
    def calc(self):
        no = 1
        while no < self.kwh:
            while no <=  2000: self.cost = 0.07
            while no <= 10000: self.cost = 0.05
            while no >  10000: self.cost = 0.04




    def __str__(self):
        return f"The Cost of{self.kwh} is: "
