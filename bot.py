import telegram
import openai
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Установка токенов и ключей API из переменных окружения
TELEGRAM_TOKEN = os.environ.get('5987197501:AAHvadKeHvZqX_gOq3H_v-9p0vV_rra-lsQ')
OPENAI_API_KEY = os.environ.get('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')

# Создание экземпляра бота Telegram
bot = telegram.Bot(token='5987197501:AAHvadKeHvZqX_gOq3H_v-9p0vV_rra-lsQ')

# Установка ключа API OpenAIэ
openai.api_key = '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'

# Обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот! Чтобы узнать, что я могу делать, напиши /help")

# Обработчик команды /help
def help(update, context):
    help_message = "Я умею отвечать на вопросы с помощью GPT-3. Просто напиши мне свой вопрос и я постараюсь дать на него ответ. Удачи!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)

# Обработчик текстовых сообщений
def generate_response(update, context):
    user_message = update.message.text
    try:
        response = openai.Completion.create(engine="davinci", prompt=user_message, max_tokens=50)
        bot_message = response.choices[0].text
    except Exception as e:
        # Обработка ошибок запроса к API OpenAI
        bot_message = "Произошла ошибка при запросе к OpenAI API. Попробуйте еще раз позже."
        print(e)
    context.bot.send_message(chat_id=update.effective_chat.id, text=bot_message)

# Создание экземпляра обновления и регистрация обработчиков
updater = Updater(token='5987197501:AAHvadKeHvZqX_gOq3H_v-9p0vV_rra-lsQ', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, generate_response))

# Запуск бота
updater.start_polling()