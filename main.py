import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN kiritilmagan!")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(
        types.KeyboardButton("🎬 Kino izlash"),
        types.KeyboardButton("💎 VIP olish")
    )

    bot.send_message(
        message.chat.id,
        "🎬 Kino botga xush kelibsiz!",
        reply_markup=menu
    )


@bot.message_handler(func=lambda message: True)
def messages(message):
    if message.text == "🎬 Kino izlash":
        bot.send_message(message.chat.id, "🔍 Kino kodini yuboring.")
    elif message.text == "💎 VIP olish":
        bot.send_message(message.chat.id, "💎 VIP uchun admin bilan bog‘laning.")


print("Bot ishga tushdi!")
bot.infinity_polling()
