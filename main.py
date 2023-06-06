import telebot

bot = telebot.TeleBot(token="YOUR TOKEN")

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    my_channel_id = -123456789  # Your channel ID
    statuss = ['creator', 'administrator', 'member']
    for i in statuss:
        if i == bot.get_chat_member(chat_id=my_channel_id, user_id=message.from_user.id).status:
             bot.send_message(message.chat.id,
                              "You are subscribed!")
        break
    else:
        bot.send_message(message.chat.id, "Subscribe to the channel to continue")

        
if __name__ == '__main__':
    bot.polling(none_stop=True)
