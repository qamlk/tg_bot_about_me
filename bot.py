#библиотеки, которые загружаем из вне
import telebot
TOKEN = '5787672381:AAESgS-88436sKpQvLJZL7EWGkTkyOcc9aM'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.jpg', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Мой репозиторий")
	item2 = types.KeyboardButton("😋 Написать мне в личку")
	item3 = types.KeyboardButton("📥 Моя почта")
	item4 = types.KeyboardButton("🎮 Мой Steam")
	item5 = types.KeyboardButton("📷 Мой Инстаграм")

	markup.add(item1, item2, item3, item4, item5)

	bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/qamlk')
		elif message.text == '😋 Написать мне в личку':
			bot.send_message(message.chat.id, 'https://t.me/qamlk')
		elif message.text == '📥 Моя почта':
			bot.send_message(message.chat.id, 'Почта: melik.shixragimov98@mail.ru')
		elif message.text == '🎮 Мой Steam':
			bot.send_message(message.chat.id, 'Steam: https://steamcommunity.com/id/qamlk/')
		elif message.text == '📷 Мой Инстаграм':
			bot.send_message(message.chat.id, 'Инстаграм: https://instagram.com/melik_shikhragimov?igshid=MmJiY2I4NDBkZg==')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)