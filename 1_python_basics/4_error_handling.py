class Accident(Exception):
  def __init__(self, e):
    self.e = e
  
  def print_exception(self):
    print(f"User defined Exceptino: {self.e}")

  def handle(self):
    print("accident happen, call ambulance")

def process_file():
  try:
    f = open("c:\\code\\data.txt")
    x = 1/0
  except FileNotFoundError as e:
    print(f"except: {e}")
  except ZeroDivisionError as e:
    print(f"except: {e}")
  finally: # clean up / close up
    print("cleaning up file")
    f.close()

try:
  raise Accident("crash between two bikes")
except Accident as e:
  e.print_exception()
  e.handle()