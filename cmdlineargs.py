import sys # gives access to command line args


def main(args):
  #C-style "Main/enterypoint" function
  if len(args) <= 0:
    print("Hello!")
    return
  print("Hello", args[0]) # args is a variable, args is just common syntax
  for arg in args:
    print(arg)

if __name__ == "__main__":
  main(sys.argv[1:]) # sys.args 1 and beyond
  
  