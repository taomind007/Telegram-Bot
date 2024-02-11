from telegram import *
from telegram.ext import *

# fetch the bot information
bot = Bot("Past token ID")
print(bot.get_me())

# Update for future changes
updater=Updater("Past token ID ",use_context=True)
# use_context is use for if your telegram version is low than use false else use true

# dispatch this update to the telegram bot
dispatcher=updater.dispatcher

# create the command for a specific reply
def test_fnc2(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to the Copyassignment.com ",
        )
start_value2=CommandHandler('start', test_fnc2)
dispatcher.add_handler (start_value2)

def test_fnc(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="tutorial link: https://copyassignment.com/python/ ",
        )
start_value=CommandHandler('python', test_fnc)
dispatcher.add_handler (start_value)

# polling the update
updater.start_polling()