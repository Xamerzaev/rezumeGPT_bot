import os

import logging
import telegram
import openai
from flask import Flask, redirect, request, url_for
from dotenv import load_dotenv

load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")

# Set other constants
MODEL_NAME = "text-davinci-003"
TEMPERATURE = 0.6

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

try:
    # Initialize Telegram bot
    bot = telegram.Bot(token=TELEGRAM_API_KEY)
except Exception as e:
    # Raise error if initialization failed
    raise ValueError(f"Error initializing Telegram bot: {e}")


@app.route('/start', methods=['POST'])
def start():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat_id
    username = update.message.from_user.username
    bot.send_message(chat_id=chat_id, text=f"Привет, {username}! Я бот. Твой chat_id: {chat_id}")
    return 'ok'


@app.route('/animal', methods=['POST'])
def index():
    # Get update from Telegram or form data
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    animal = request.form.get('animal', update.message.text)

    try:
        # Call OpenAI API to generate response
        response = openai.Completion.create(
            model=MODEL_NAME,
            prompt=generate_prompt(animal),
            temperature=TEMPERATURE,
        )
        
        # Extract text from top suggestion
        result = response.choices[0].text
    except Exception as e:
        # Handle errors by returning empty result
        result = ''

    # Respond to user message in Telegram and redirect to index
    update.message.reply_text(result)
    return redirect(url_for('index', result=result))

def generate_prompt(animal):
    return f"{animal.capitalize()}"

app.logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
