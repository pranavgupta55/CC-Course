# env
from dotenv import load_dotenv
load_dotenv()

# create a client
from anthropic import Anthropic
client = Anthropic()
model = "claude-haiku-4-5"

from helperFuncsChatbot import add_user_message, add_assistant_message, chat

messages = []
print("Chatbot: Hello! Type something to chat with me (or type [exit]/[quit] to quit).")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    else:
        add_user_message(messages, user_input)
        response = chat(messages)
        add_assistant_message(messages, response)
        print(f"Chatbot: {response}")

