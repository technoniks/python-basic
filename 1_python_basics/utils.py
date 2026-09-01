from dotenv import load_dotenv
import os, time

load_dotenv()

def loadGoogleApiKey():
  return os.getenv("GOOGLE_API_KEY")

def time_it(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"{func.__name__} took {str((end-start)*1000)} milliseconds")
  
  return wrapper