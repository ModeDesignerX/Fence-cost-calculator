continuescript = ""
while continuescript == "":
  def ask(Value):
    x = 0
    attempts = 0
    while x <= 0:
      if attempts > 0:
        print()
        print("Please enter a number higher than 0")
        print()
      try:
        attempts = attempts + 1
        x = float(input("{}: ".format(Value)))
      except:
        print()
        print("Please enter a valid number")
        print()
        attempts = 0
    return x
  width = ask("Width")
  height = ask("Length")
  cost = ask("Cost / m")
  perimeter = (height+width)*2
  cost = perimeter*cost
  print()
  print("Perimeter: ", perimeter)
  print("Cost: ", cost)
  print()
  continuescript = input("Again? ")
  print()
