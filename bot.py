import telebot

TOKEN = '7742479143:AAHzp86TrQwLngS7BPko2xcWRpmY3HW-cIo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "أهلاً بيك في بوت شركة الشحن ShahenX!")

bot.polling()
