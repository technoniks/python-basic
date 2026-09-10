class Father():
  def gardening(self):
    print("I enjoy Gardening")

class Mother():
  def cooking(self):
    print("I love Cooking")

class Child(Father, Mother):
  def sports(self):
    print("I play sports") 
  
  def skills(self):
    Father.gardening(self)
    Mother.cooking(self)
    self.sports()

c = Child()
c.skills()