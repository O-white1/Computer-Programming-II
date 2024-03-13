class Cl213f:

    def __int__(self, kwh):
        self.kwh = kwh
        self.cost = 0.0
    def calc(self):
        if self.kwh <= 2000:
            self.cost = self.kwh * 0.07
        elif 2000 < self.kwh < 10000:
            self.cost = 2000 * 0.07 + (self.kwh - 2000)*0.05



        """
        no = 1
        while no < self.kwh:
            while no <= 2000: cost = 0.07
            while no <= 10000: cost = 0.05
            while no > 10000: cost = 0.04
            bill = kwh*cost
        """




    def __str__(self):
        return f"The Cost of{self.kwh} is: "
