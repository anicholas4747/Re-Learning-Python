import makin_modules

class Mammal:
  def breathe_oxygen(self):
    print("In... Out...")

class Person(Mammal):
  def think(self):
    print(f"Hmmm, 2+2={makin_modules.add_nums(2,2)}")

class Cow(Mammal):
  def moo(self):
    print("Moooo")

class Baby(Person):
  pass # telling py interpreter "dw about this empty function/class, i did this on purpose"

parent = Person()
parent.think()
print("-"*50)

kid = Baby()
kid.breathe_oxygen()
print("-"*50)

chicfilay = Cow()
chicfilay.breathe_oxygen()
chicfilay.moo()
