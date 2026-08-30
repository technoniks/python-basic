from google import genai
import utils

# loading gemini api key
utils.loadGoogleApiKey()
conversations = []

# model client
client = genai.Client()

def reset():
  conversations.clear()

def chat(user_message):
  conversations.append({
    'role': 'user',
    'parts': [{ 'text': user_message }]
  })
  try:
    res = client.models.generate_content(
      model='gemini-3.6-flash',
      contents=conversations
    )
    reply = res.text
  except Exception as e:
    return f'Sorry something went wrong: {e}'
  conversations.append({
    'role': 'model',
    'parts': [{'text': reply}]
  })
  return reply

print(chat("my nam is nikhil, remenber it"))
reset()
print('-------')
print(chat("what is my name"))

