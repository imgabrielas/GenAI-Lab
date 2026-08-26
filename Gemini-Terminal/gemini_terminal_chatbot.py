# # pip install google-genai
from google import genai

client = genai.Client(api_key='PUT YOUR API KEY HERE')

# Create a chat session
chat = client.chats.create(model='PUT MODEL HERE')
# example gemini-2.5-flash

while True:
    question = input('You: ')

    if question.lower() == 'exit':
        break

    # Send message through the chat object
    response = chat.send_message(question)

    print('Gemini:', response.text)
