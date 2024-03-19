import telebot
import tweet
bot = telebot.TeleBot("5957261449:AAGnSIajkIVbWVH4-uIabx9uCBVJS0TyZuk")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message.text)
    tweet.api.update_status(message.text)
    bot.reply_to(message, "Tweet Terkirim")

print("tweetgram is running")
bot.polling()
