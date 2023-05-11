import telegram
import openai
print(telegram.__version__)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work


# Установка токена OpenAI API
openai.api_key = "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"

# Создание экземпляра бота Telegram
bot = telegram.Bot(token="5987197501:AAHvadKeHvZqX_gOq3H_v-9p0vV_rra-lsQ")

# Обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот!")

# Обработчик текстовых сообщений
def generate_response(update, context):
    user_message = update.message.text
    response = openai.Completion.create(engine="davinci", prompt=user_message, max_tokens=50)
    bot_message = response.choices[0].text
    context.bot.send_message(chat_id=update.effective_chat.id, text=bot_message)

# Создание экземпляра обновления и регистрация обработчиков
updater = Updater(token="5987197501:AAHvadKeHvZqX_gOq3H_v-9p0vV_rra-lsQ", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, generate_response))

# Запуск бота
updater.start_polling()