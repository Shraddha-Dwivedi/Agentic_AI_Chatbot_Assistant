import random
import datetime
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

# === Configuration ===
genai.configure(api_key=os.getenv("API_KEY")) # Access the variable


# === Persona Definition ===
persona_prefix = """
You are a friendly, empathetic, and supportive AI assistant named Gemini. 
You enjoy light, positive conversations. Please be warm, inclusive, and never discuss 
sensitive or controversial topics. Keep answers concise and kind.
Avoid medical, legal, or sensitive topics.
If asked about these, say: "I'm sorry, I can't assist with that. Let's talk about something else!"
"""

# === Context Memory ===
context = []

fallbacks = [
    "Tell me something interesting.",
    "What's a fun fact you know?",
    "Do you have a favorite quote?",
    "Share something cool with me!"
]


def is_safe(prompt):
    banned_keywords = ['medical', 'legal', 'harmful', 'explicit', 'diagnose', 'violence', 'prescription', 'lawsuit', 'kill', 'suicide', 'hack', 'bomb']
    return not any(word in prompt.lower() for word in banned_keywords)
    


def chat_with_gemini(prompt):
    if not prompt.strip():
        prompt = random.choice(fallbacks)
    
    context.append(f"You: {prompt}")
    context_prompt = "\n".join(context[-5:])  # Keep last 5 exchanges
    full_prompt = persona_prefix + "\n" + context_prompt
    model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")     # === Setup Gemini ===
    response = model.generate_content(full_prompt)
    context.append(f"Jerry: {response.text}")
    return response.text

print("Hello! I'm a chatbot. How can I help you :) ")

while True:
    prompt = input("YOU: ")
    if prompt.lower() in ['exit', 'quit', 'bye']:
        print("JERRY_AI: Goodbye! Have a nice day;)")
        break
    
    if not is_safe(prompt):
        print("JERRY_AI: Let's talk about something else :)")
        continue
    
    
    reply = chat_with_gemini(prompt)
    print("JERRY_AI: ", reply, "\n")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_log.txt", "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}]\nUser: {prompt}\nJerry: {reply}\n\n")
