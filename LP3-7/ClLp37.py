
class ClLp37:
	def __init__(self, num1, num2): # constructor
		self.n1 = num1 
		self.n2 = num2
		self._div = 0
		self._mod = 0
		
	def calc(self):
		self._div = self.n1 / self.n2
		self._mod = self.n1 % self.n2
		
	def GetDivMod(self):
		return (self._div, self._mod) # returns tuple
	
