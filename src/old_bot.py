import telebot

bot_token = "8658936356:AAFJ1Lkzx9VHpOf1_3mQwCdL-W4qRKDgd0I"
bot = telebot.TeleBot(bot_token, parse_mode="HTML")

ADMINS_USERNAME = ["J_AHMDI"]
VALID_CHATS = ["test_test_Faq"]
  

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome Baby Girlll")


@bot.message_handler(
    func=lambda message: (message.reply_to_message is not None)
    & (message.from_user.username.lower() in ADMINS_USERNAME)
    & (message.chat.username.lower() in VALID_CHATS)
)
def echo_all(message):
    bot.reply_to(message, 'hi')


print("Bot is running")
bot.infinity_polling() 
