# **Woody the Snake - A Chinese New Year Discord Bot 🐍**

Woody is a fun and interactive Discord bot inspired by the Chinese New Year. He’s a friendly snake who uses snake-like phonetics, cracks jokes, and spreads festive joy. Woody responds to mentions in Discord channels and can generate unique replies using AI-powered responses.

---

## **Features**
- 🐍 **Snake-Themed Personality**: Woody speaks with snake-like phonetics (e.g., "ssspectacular") and embodies the spirit of the Chinese New Year.
- 🎉 **Chinese New Year Jokes & Facts**: Shares jokes, trivia, and well wishes related to the Lunar New Year.
- 💬 **AI-Powered Replies**: Generates intelligent and witty responses using OpenAI-compatible models.
- 🔄 **Fresh Conversations**: Treats every message as a standalone interaction with no context carried over.
-  ✍️ **Typing Indicator**: Simulates typing while processing responses for a more interactive experience.
- 🔗 **Discord Replies**: Responds directly to user messages as threaded replies.

---

## **Setup Instructions**

### **Prerequisites**
1. Python 3.8 or higher (but not 3.13 due to compatibility issues).
2. A Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
3. An OpenAI API key or a locally hosted OpenAI-compatible endpoint.

### **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/woody-the-snake.git
   cd woody-the-snake
   ```

2. Create a virtual environment:
   ```bash
   python -m venv woody-env
   source woody-env/bin/activate  # On Windows: woody-env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add the following:
   ```
   DISCORD_TOKEN=your_discord_bot_token
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_API_BASE=https://api.openai.com/v1  # Change this if using a custom endpoint
   ```

---

## **Usage**
1. Run the bot:
   ```bash
   python bot.py
   ```

2. Invite Woody to your server using an OAuth2 URL:

3. Mention Woody in any channel to interact with him:
   - Example: `@Woody Tell me a Chinese New Year joke!`

---

## **Customization**
- Modify Woody's personality in the system prompt within `bot.py`:
  ```python
  {"role": "system", "content": "You are Woody, a friendly snake-themed assistant who makes jokes about Chinese New Year and uses snake-like phonetics."}
  ```
- Adjust response creativity by changing the `temperature` parameter in the OpenAI API call:
  ```python
  temperature=0.7  # Lower values make responses more focused; higher values make them more creative.
  ```

---

## **Features Roadmap**
- 🐉 Add support for other Chinese zodiac animals.
- 🌟 Enhance personality with more festive greetings and interactive commands.
- 📜 Slash command support for easier interaction.

---

## **Troubleshooting**
### Common Issues:
1. **Bot is offline**:
   - Ensure your bot token is correct in the `.env` file.
   - Verify that the bot script is running without errors.

2. **Bot doesn't respond**:
   - Check if Woody has permissions to read/send messages in the channel.
   - Ensure you mentioned Woody correctly (e.g., `@Woody`).

3. **ModuleNotFoundError for `audioop`**:
   - Use Python 3.12 or install `audioop-lts` if you're using Python 3.13.

---

## **Contributing**
Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests to improve Woody.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
