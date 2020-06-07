class Dog:
  def __init__(self, name):
    self.name = name

  def bark(self):
    print("Arf! Arf!")
  
  def fetch(self,obj):
    print(f"{self.name} fetched the {obj}")


chico = Dog("Chico")
chico.bark()
chico.fetch("stick")

miss = Dog("Ms. Waggington")
miss.fetch("ball")