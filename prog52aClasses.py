class Shape:
 #constructor sets up class data 
  def __init__(self, length, width):
    self.length = length
    self.width = width
    self._area = 0 # _ prefix means private
    self._perim = 0 # __ truly locks it
  # mutators / setters: modifies class data
  def calculate(self):
    self._area = self.length * self.width
    self._perim = self.length*2 + self.width*2

  def setLength(self, length):
    self.length = length # redundant

  #accesor/getter: returns class data
  def getArea(self):
    return self._area
    
  def getPerim(self):
    return self._perim


  len = int(input("Enter Length: "))
  wid = int(input("Enter Width:  "))
  # make a new shape object
  shape = Shape(len, wid) # call the Shape contructor
  # shape.setLength(5) changes length variable
  shape.calculate()
  print("Area ", shape.getArea())
  print("Perimter", shape.getPerimeter)