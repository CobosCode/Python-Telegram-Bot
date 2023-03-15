import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = 'TU_TOKEN_DE_ACCESO_AQUI'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! Soy un bot de Telegram.")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()