# Ekonomek

A Gemini-powered persona for Ekonomek, the gnome mascot of Wrocław University of Economics and Business (UEW). The notebook builds a chatbot with a system prompt and knowledge base, an interactive chat widget, text-to-speech, speech-to-text, and a small semantic search engine over the knowledge base.

Before running it, you need to:

1. **Install the SDK.** The import at the top of the notebook is left as a comment — copy it and run it yourself:
   ```
   pip install google-genai
   ```
2. **Get an API key.** Generate one from [Google AI Studio](https://aistudio.google.com/apikey).
3. **Add your API key to the code.** Replace `'PUT YOUR API KEY HERE'` in `genai.Client(api_key=...)` with your actual key.
4. **Run on Google Colab for the STT cell.** The speech-to-text cell records audio via the browser using `google.colab.output`, so that cell only works in Colab.

> **Do NOT share your API key.** Never commit it to git, paste it in chats/screenshots, or share it with anyone. Treat it like a password — anyone with your key can use your Gemini quota (and potentially rack up charges) on your account.

Once set up, run the notebook top to bottom and chat with Ekonomek using the widget.