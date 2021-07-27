from telegram.ext import Updater, CommandHandler


def start(update, context):

    update.message.reply_text('Hola, humano!')

if __main__ == '__main__':

    updater = Updater(token='', use_contenxt=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    # add handler

    updater.start_polling()
    updater.idle()