# pip install google-genai

from google import genai

client = genai.Client(api_key='Put your API key here')

while True:
    question = input('You: ')

    if question.lower() == 'exit':
        break

    response = client.models.generate_content(
        model = 'Your model of choice',
        contents = question
    )

    print('Gemini:', response.text)