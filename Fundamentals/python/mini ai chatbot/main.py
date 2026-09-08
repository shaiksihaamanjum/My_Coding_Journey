from google import genai
from dotenv import load_dotenv
import os 
load_dotenv()
conversation=[]
my_api_key=os.getenv("my_api_key")
client = genai.Client(api_key=my_api_key)
previous_id=None
def chat(user_msg):
    global previous_id
    conversation.append({"role":"user","parts":{"text":user_msg}})
    if previous_id is None:
        interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=user_msg)
    else:
        interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=user_msg,
        previous_interaction_id=previous_id )
    previous_id=interaction.id
    reply=(interaction.output_text)
    conversation.append({"role":"model","parts":{"text":reply}})
    return reply
chat("give me step by step procedure to prepare maggie ")
chat("which maggie company is best i mean non harmful and tastes better")
chat("give me summary of our previous chats in json format")