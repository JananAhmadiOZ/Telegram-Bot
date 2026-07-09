import telebot
from config import bot_token, ADMINS_USERNAME, VALID_CHATS
from constans import welcome_message

class PytopiaFAQBot:
    def __init__(self):
        self.bot = telebot.TeleBot(bot_token, parse_mode="HTML")
        self.setup_handlers()

    def setup_handlers(self):
        self.bot.message_handler(commands=["start", "help"])(self.send_welcome)
        self.bot.message_handler(func=self.is_valid_admin_reply)(self.admin_reply)

    def send_welcome(self, message):
        self.bot.reply_to(message, welcome_message)
    
    def is_valid_admin_reply(self, message):
        return (
            message.reply_to_message is not None
            and message.from_user.username.lower() in ADMINS_USERNAME
            and message.chat.username.lower() in VALID_CHATS
        )
    
    def admin_reply(self, message):
        self.bot.reply_to(message, 'test')
        
    def run(self):
        print("Bot is running...")
        self.bot.infinity_polling()


if __name__ == "__main__":
    bot = PytopiaFAQBot()
    bot.run()
