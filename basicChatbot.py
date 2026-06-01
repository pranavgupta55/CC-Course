# env
from dotenv import load_dotenv
load_dotenv()

# create a client
from anthropic import Anthropic
client = Anthropic()
model = "claude-haiku-4-5"


########################################################################
# 3 helper funcs (from requests.ipynb)

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

########################################################################

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

