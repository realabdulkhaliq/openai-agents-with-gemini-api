import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"Received from AK: {message.content}!").send()