# GenAI-Lab

A collection of small AI-related projects for me to play around with.

## Projects

### 1. Gemini Chatbot (IDE Terminal)

`Gemini-Terminal/gemini_terminal_chatbot.py`

A really simple terminal chatbot that talks to Google's Gemini API. Before running it, you need to:

1. **Install the SDK.** The import at the top of the file is left as a comment — copy it and run it yourself:
   ```
   pip install google-genai
   ```
2. **Get an API key.** Generate one from [Google AI Studio](https://aistudio.google.com/apikey).
3. **Add your API key to the code.** Replace `'Put your API key here'` in `genai.Client(api_key=...)` with your actual key.
4. **Choose a model.** Replace `'Your model of choice'` with a Gemini model name, e.g. `'gemini-3.5-flash-lite'`.

> **Do NOT share your API key.** Never commit it to git, paste it in chats/screenshots, or share it with anyone. Treat it like a password — anyone with your key can use your Gemini quota (and potentially rack up charges) on your account.

Once set up, run the script and chat with Gemini in your terminal. Type `exit` to quit.