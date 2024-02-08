import voidfunctions.py

def calcArea(len, wid) -> int:
  return len * wid

def calcPerim(len:int, wid:int) -> int:
  return 2*len + 2*wid

def AreaPerim(len, wid):
  area = calcArea(len, wid)
  perim = calcPerim(len, wid)
  return area, perim


def main():
  voidfunctions.doSomething() # uses function from import
  len = int(input("Length: "))
  wid = int(input("Width:  "))
  a, p = AreaPerim(len, wid)
  print(f"Area: {a}\nPerimeter:{p}")
  pass


if __name__ == "__main__":
  main()