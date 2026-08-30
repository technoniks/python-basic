# define HashTable class
class HashTable():
  def __init__(self):
    self.MAX = 10
    self.arr = [[] for i in range(self.MAX)]

  def get_hash(self, key):
    hash = 0
    for char in key:
      hash += ord(char)
    return hash % self.MAX
  
  def __getitem__(self, key):
    h = self.get_hash(key)
    for element in self.arr[h]:
      if element[0] == key:
        return element[1]
  
  def __setitem__(self, key, value):
    h = self.get_hash(key)
    found = False
    for idx, element in enumerate(self.arr[h]):
      if len(element) == 2 and element[idx] == key:
        self.arr[h][idx] = (key, value)
        found = True
        break
    if not found:
      self.arr[h].append((key, value))

  def __delitem__(self, key):
    h = self.get_hash(key)
    for idx, element in enumerate(self.arr[h]):
      if element[0] == key:
        del self.arr[h][idx]
        break

h = HashTable()
h["march 6"] = 12
h["march 16"] = 12
h["march 7"] = 14
h["march 17"] = 33
del h["march 17"]

for i in h.arr:
  print(i)