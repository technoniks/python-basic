from dotenv import load_dotenv
import os

load_dotenv()

def loadGoogleApiKey():
  return os.getenv("GOOGLE_API_KEY")