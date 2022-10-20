#библиотеки, которые загружаем из вне
import telebot
import random
TOKEN = '5590792892:AAGDk3GhqoBfKQ7ozvrIlBn-0yJbR66nfM4'

from telebot import types
from random import choice

bot = telebot.TeleBot(TOKEN)

place1 = ['Парк Краснодар https://kukarta.ru/park-krasnodar-park-galitskogo/', 'Улица  Красная https://kukarta.ru/ulitsa-krasnaya-v-krasnodare/', 'Ботанический сад  https://kukarta.ru/botanicheskiy-sad-kubgau/','Чистяковская роща https://kukarta.ru/chistyakovskaya-roshha/', 'Парк Солнечный Остров https://kukarta.ru/park-solnechnyiy-ostrov/']
place2 = [' Пиноккио Джан https://www.tripadvisor.ru/Restaurant_Review-g298532-d6024833-Reviews-Pinocchio_Djan-Krasnodar_Krasnodar_Krai_Southern_District.html', ' Кафе «Краснодар» https://www.tripadvisor.ru/Restaurant_Review-g298532-d17353086-Reviews-Cafe_Krasnodar-Krasnodar_Krasnodar_Krai_Southern_District.html', 'Птичка-Невеличка https://www.tripadvisor.ru/Restaurant_Review-g298532-d20435971-Reviews-Ptichka_Nevelichka-Krasnodar_Krasnodar_Krai_Southern_District.html', 'FOODMARKET Центр Города https://www.tripadvisor.ru/Restaurant_Review-g298532-d21250960-Reviews-Foodmarket_Tsentr_Goroda-Krasnodar_Krasnodar_Krai_Southern_District.html', 'Угли-угли https://www.tripadvisor.ru/Restaurant_Review-g298532-d10587471-Reviews-Ugli_ugli-Krasnodar_Krasnodar_Krai_Southern_District.html'] 
place3 = [' Музей Фелицына https://felicina.ru/', ' Океанариум ОКЕАН ПАРК https://www.tourister.ru/world/europe/russia/city/krasnodar/zoo/22965', ' Краснодарский краевой художественный музей https://kovalenkomuseum.ru/, Музей Ретро Автомобилей https://www.tripadvisor.ru/Attraction_Review-g298532-d12885364-Reviews-Antique_Car_Museum-Krasnodar_Krasnodar_Krai_Southern_District.html']
place4 = ['Батутный парк FlyZone https://fly-z-one.ru/', 'Полеты в невесомости в Skydive park https://www.skykrasnodar.com/windtunnel', 'Квесты Паника https://panika.org/', 'Пейнтбол в клубе «Застава» https://zastava93.ru/']
place5 = [place1, place2,place3,place4]

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton(" Хочу пройтись пешком ☀️")
	item2 = types.KeyboardButton("Хочу перекусить 🍕")
	item3 = types.KeyboardButton(" Хочу узнать что-то новое 👨‍🎨")
	item4 = types.KeyboardButton("Хочу активностей 🏄‍♀️")
	item5 = types.KeyboardButton("Выбери за меня 🧞‍♂️")

	markup.add(item1, item2, item3, item4, item5)
	

	bot.send_message(message.chat.id, "Привет, {0.first_name}! Как хочешь провести день сегодня?".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Хочу пройтись пешком ☀️':
			bot.send_message(message.chat.id, random.choice(place1))
		elif message.text == 'Хочу перекусить 🍕':
			bot.send_message(message.chat.id, random.choice(place2))
		elif message.text == 'Хочу узнать что-то новое 👨‍🎨':
			bot.send_message(message.chat.id, random.choice(place3))
		elif message.text == 'Хочу активностей 🏄‍♀️':
			bot.send_message(message.chat.id, random.choice(place4))
		else:
			bot.send_message(message.chat.id, random.choice(place5))
		

	

bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods