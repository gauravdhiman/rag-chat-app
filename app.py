import chainlit as cl
from rag import get_response

@cl.on_chat_start
def start():
    cl.user_session.set("message_history", [])

@cl.on_message
async def main(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_content = message.content  # Extract the content from the Message object
    message_history.append({"role": "user", "content": message_content})
    
    response = get_response(message_content)  # Pass the string content to get_response
    
    message_history.append({"role": "assistant", "content": response})
    cl.user_session.set("message_history", message_history)
    
    await cl.Message(content=response).send()

if __name__ == "__main__":
    cl.run()