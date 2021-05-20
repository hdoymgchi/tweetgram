import telebot
import tweet
bot = telebot.TeleBot("1765737707:AAHXXP8-7Dh9p28LE3WHMRs4bqFxXN3lp0M")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message.text)
    tweet.api.update_status(message.text)
    bot.reply_to(message, "Tweet Terkirim")

print("tweetgram is running")
bot.polling()