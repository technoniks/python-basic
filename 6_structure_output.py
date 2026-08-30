from pydantic import BaseModel
from google import genai
from google.genai import types
import utils

class ReviewAnalysis(BaseModel):
  sentiment: str
  rating: int
  pros: list[str]
  cons: list[str]

utils.loadGoogleApiKey()
client = genai.Client()
response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents="I ordered the wireless earbuds last week. Sound quality is amazing and battery lasts all day, but the case feels cheap and it arrived two days late. Probably won't buy from this brand again.",
  config=types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=ReviewAnalysis,
  ),
)
print(response.text)
