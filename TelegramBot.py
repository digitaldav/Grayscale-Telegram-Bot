from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging
import os
from PhotoProc import Grayscale


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
	update.message.reply_text("Hi! Send a image and I will send you it in black and white")

def help(bot, update):
	update.message.reply_text("Send a image and I will send you it in black and white")

def ReplyBWImage(bot, update):
    user = update.message.from_user
    photo_file = bot.get_file(update.message.photo[-1].file_id)
    photoName = str(update.message.chat_id)+"Normal.png"
    photo_file.download(photoName)
    
    photoGS = Grayscale(photoName)

    update.message.reply_photo(photo=open(photoGS, 'rb'))

    os.remove(photoGS)
    os.remove(photoName)

def error(bot, update, error):
	logger.warning('Update "%s" caused error "%s"', update, error)


def main():
	updater = Updater("token")

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))

	dp.add_handler(MessageHandler(Filters.photo, ReplyBWImage))

	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()