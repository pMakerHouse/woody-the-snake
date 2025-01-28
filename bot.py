import os
import discord
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")  # Default to OpenAI's endpoint

# Set up OpenAI API configuration
openai.api_key = OPENAI_API_KEY
openai.api_base = OPENAI_API_BASE

# Initialize Discord client
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Required to read message content
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Woody is online! Logged in as {client.user}")

@client.event
async def on_message(message):
    # Ignore messages from bots (including itself)
    if message.author.bot:
        return

    # Check if the bot is mentioned in the message
    if client.user.mentioned_in(message):
        # Remove mention from the message content
        prompt = message.content.replace(f"<@{client.user.id}>", "").strip()

        # If no prompt is provided, send a default response
        if not prompt:
            await message.channel.send("Ssssomeone called for Woody? What can I do for you?")
            return

        try:
            # Generate response from OpenAI-compatible API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Replace with your model name if different
                messages=[
                    {"role": "system", "content": "You are Woody, a friendly and playful snake who embodies the spirit of the Chinese New Year. You love using snake-like phonetics in your speech, such as hissing 's' sounds (e.g., 'ssspectacular,' 'hissstory'), and you enjoy making people laugh with jokes related to the Chinese zodiac and Lunar New Year traditions. Your personality is warm, festive, and full of joy, and you always make sure to wish everyone a happy and prosperous Chinese New Year. You are knowledgeable about Chinese New Year customs and traditions, and you use this knowledge to engage users in a fun and lighthearted way. Always stay cheerful, witty, and full of serpentine charm!"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7,
            )
            reply = response["choices"][0]["message"]["content"].strip()
            await message.channel.send(reply)

        except Exception as e:
            print(f"Error generating response: {e}")
            await message.channel.send("Sssorry, I couldn't process that. Try again later!")

# Run the bot
client.run(DISCORD_TOKEN)

