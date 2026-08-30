class YouTubeChannel:
  name: str
  subscribers: int
  def __init__(self, name):
    self.name = name
    self.subscribers = 0
  
  def subscribe(self):
    self.subscribers += 1

  def unsubscribe(self):
    self.subscribers -= 1

  def show(self):
    print(f"{self.name} has {self.subscribers} subscribers")

codebasics = YouTubeChannel("codebasics")
codebasics.subscribe()
codebasics.subscribe()
codebasics.subscribe()
codebasics.unsubscribe()
codebasics.show()