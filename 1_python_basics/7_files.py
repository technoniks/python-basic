from google import genai
from google.genai import types
from pydantic import BaseModel
import utils 

def getFileData():
  with open("note.txt", "r", encoding="utf-8") as f:
    return f.read()
  
class Summary(BaseModel):
  title: str
  bullet_points: list[str]

# loaging gemini api key
utils.loadGoogleApiKey()

# model client
document = getFileData()

client = genai.Client()
prompt = f"""
  here is meeting transcript:
  {document}

  summarize it in 3 short bullet point, also output should be in json format and every bullet point should use as key
 """

try:
  response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      response_mime_type="application/json",
      response_schema=Summary
    )
  )
  summary = response.text
except Exception as e:
  summary = f"something went wrong: {e}"

with open("summary.txt", "w", encoding="utf-8") as f:
  f.write(summary)