from telegram.ext import Updater, CommandHandler


def start(update, context):

    update.message.reply_text('Hola, humano! soy un bot')

if __main__ == '__main__':

    updater = Updater(token='YOUR_TOKEN', use_contenxt=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    # add handler

    updater.start_polling()
    updater.idle()
