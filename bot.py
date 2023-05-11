import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import filters

# Создаем экземпляр бота
bot = telegram.Bot(token='5987197501:AAHvadKeHvZqX_gOq3H_v-9p0vV_rra-lsQ')

# Обработчик команд
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот!")

# Обработчик текстовых сообщений
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Создаем экземпляр обновления и регистрируем обработчики
updater = Updater(use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, echo))

# Запускаем бота
updater.start_polling(token='5987197501:AAHvadKeHvZqX_gOq3H_v-9p0vV_rra-lsQ')