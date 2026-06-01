# env
from dotenv import load_dotenv
load_dotenv()

# create a client
from anthropic import Anthropic
client = Anthropic()
model = "claude-haiku-4-5"


# 3 helper funcs (from requests.ipynb)
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text