from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, telegram

updater = Updater(token ='750732573:AAFdeaN9Ut9Z-0Uuc-zMboyHjAeMSvE6yyo')
bot = telegram.Bot(token='750732573:AAFdeaN9Ut9Z-0Uuc-zMboyHjAeMSvE6yyo')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Bem-vindo! Selecione umas das palavras-passe a seguir para obter um diagnóstico:")

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

    caps_handler = CommandHandler('caps', caps, pass_args=True)
    dispatcher.add_handler(caps_handler)


updater.start_polling()
