# -*- coding: utf-8 -*- 
import telebot
from telebot import types
import sqlite3
import keyboards
import time
# BOT
bot = telebot.TeleBot('токен')

admin = id

#ТОПОВЫЙ КАНАЛ СО СЛИВАМИ СКРИПТОВ  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT 
@bot.message_handler(commands=['start'])
def start_message(message):
	global ref_stavka
	global lose_money
	global ref_user
	global ref_donate
	global ref_earn
	global ref_count
	userid = str(message.chat.id)
	ref_user = message.text
	ref_count = 0
	amount = 0
	ref_donate = 0
	userid = str(message.chat.id)
	username = str(message.from_user.username)
	connection = sqlite3.connect('database.sqlite')
	q = connection.cursor()
	q = q.execute('SELECT * FROM users WHERE (id IS ? AND name IS ?)', (userid, username))
	row = q.fetchone()
	if row is None:
		q.execute("INSERT INTO users (id,name,amount,ref_user, ref_count, ref_donate) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"%(userid,username,amount,ref_user[7:],ref_count,ref_donate))
		connection.commit()
		if ref_user[7:] != '':
			q.execute("update users set ref_count = ref_count + 1" + " where id =" + str(ref_user[7:]))
			connection.commit()
			q.close()
			connection.close()
		else:
			connection = sqlite3.connect('database.sqlite')
			userid = str(message.chat.id)
			username = str(message.from_user.username)
			q = connection.cursor()
			q.execute("update users set ref_user = 05959 where id =" + str(userid))
			connection.commit()
			q.close()
			connection.close()
	bot.send_message(message.chat.id, """Как сделать заказ? :

<b>1 - Выберите свой город

2 - Выберите что вас интересует

3 - Оплатите выбранный товар(Строго с прикреплёным комментарием)

4 - Бот в течении часа вышлет: фото клада в близи/фото клада отдалёно/точные координаты</b>



 Хорошего отдыха!!!



❗️❗️ Внимание работа ❗️❗️

🔵Ищем ответственных людей

 🛑ВАШИ ТАЛАНТЫ НЕ ОСТАНУТСЯ НЕЗАМЕЧЕННЫМИ!

▪️Курьер (от 50.000 руб/неделя)
 Окупаемость залога один день!!

▪️Водитель - до 1.000.000 руб/месяц.

▪️Фасовщик на дому - от 50.000 рублей/неделя

▪️Менеджер по подбору персонала - от 500 рублей/1 человек + премии!

📢Обращаться - @id1448""",parse_mode='HTML', reply_markup=keyboards.keyboardMain)

#ТОПОВЫЙ КАНАЛ СО СЛИВАМИ СКРИПТОВ  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT 

@bot.message_handler(content_types=['text'])
def send_text(message):
#-----------------------Команды-----------------------
	if message.text.lower() == 'оплатил':
		bot.send_message(message.chat.id, 'Платеж не найден, попробуйте через 5 минут',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)


	elif message.text.lower() == '🔹 главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

	elif message.text.lower() == 'отменить':
		bot.send_message(message.chat.id, 'Заказ отменён, вернулись на главную', reply_markup=keyboards.keyboardMain)

	elif message.text.lower() == 'админ':
		if message.chat.id == admin:
			bot.send_message(message.chat.id, 'Мы в админке', reply_markup=keyboards.admin)
	elif message.text.lower() == 'количество пользователей':
		if message.chat.id == admin:
			connection = sqlite3.connect('database.sqlite')
			q = connection.cursor()
			q.execute("SELECT COUNT(id) from users	")
			stata_users_ids_message = str(q.fetchone()[0])
			bot.send_message(message.chat.id, '📈 Пользователей бота: ' + stata_users_ids_message)
			q.close()
			connection.close()
	elif message.text.lower() == 'изменить карту':
		if message.chat.id == admin:
			connection = sqlite3.connect('database.sqlite')
			q = connection.cursor()
			q.execute('select karta from config where Id = 1')
			karta = q.fetchone()[0]
			msg = bot.send_message(message.chat.id, 'Сейчас установлена карта: '+karta+'\n\nВведите новую карту\nP.S: Если вы случайно нажали на кнопку, укажите уже установленную карту')
			bot.register_next_step_handler(msg, admin_new_karta)

	elif message.text.lower() == 'изменить qiwi':
		if message.chat.id == admin:
			connection = sqlite3.connect('database.sqlite')
			q = connection.cursor()
			q.execute('select qiwi from config where Id = 1')
			qiwi = q.fetchone()[0]
			msg = bot.send_message(message.chat.id, 'Сейчас установлен qiwi: '+qiwi+'\n\nВведите новый qiwi кошелек\nP.S: Если вы случайно нажали на кнопку, укажите уже установленный')
			bot.register_next_step_handler(msg, admin_new_qiwi)

	elif message.text.lower() == 'изменить bitcoin':
		if message.chat.id == admin:
			connection = sqlite3.connect('database.sqlite')
			q = connection.cursor()
			q.execute('select bitcoin from config where Id = 1')
			bitcoin = q.fetchone()[0]
			msg = bot.send_message(message.chat.id, 'Сейчас установлен bitcoin: '+bitcoin+'\n\nВведите новый bitcoin кошелек\nP.S: Если вы случайно нажали на кнопку, укажите уже установленный')
			bot.register_next_step_handler(msg, admin_new_bitcoin)
#-----------------------Города-----------------------
	elif message.text.lower() == '🔹 москва':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите Районы ⬇️', reply_markup=keyboards.moskow_rayons)
		bot.register_next_step_handler(msg, moskow)

	elif message.text.lower() == '🔹 санкт-петербург':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.sankt_rayons)
		bot.register_next_step_handler(msg, sankt_piter)

	elif message.text.lower() == '🔹 новосибирск':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.novosubirsk_rayons)
		bot.register_next_step_handler(msg, novosubirsk)

	elif message.text.lower() == '🔹 екатеринбург':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.ekb_rayons)
		bot.register_next_step_handler(msg, ekb)

	elif message.text.lower() == '🔹 нижний новгород':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.novgorod_rayons)
		bot.register_next_step_handler(msg, novgorod)

	elif message.text.lower() == '🔹 казань':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.kazan_rayons)
		bot.register_next_step_handler(msg, kazan)

	elif message.text.lower() == '🔹 челябинск':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.chelabinsk_rayons)
		bot.register_next_step_handler(msg, chelabinsk)

	elif message.text.lower() == '🔹 омск':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.omsk_rayons)
		bot.register_next_step_handler(msg, omsk)

	elif message.text.lower() == '🔹 самара':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.samara_rayons)
		bot.register_next_step_handler(msg, samara)

	elif message.text.lower() == '🔹 краснодар':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.krasnodar_rayons)
		bot.register_next_step_handler(msg, krasnodar)

	elif message.text.lower() == '🔹 саратов':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.saratov_rayons)
		bot.register_next_step_handler(msg, saratov)

	elif message.text.lower() == '🔹 тюмень':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.tymen_rayons)
		bot.register_next_step_handler(msg, tymen)

	elif message.text.lower() == '🔹 барнаул':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.barnaul_rayons)
		bot.register_next_step_handler(msg, barnaul)

	elif message.text.lower() == '🔹 барнаул':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.irkytsk_rayons)
		bot.register_next_step_handler(msg, irkytsk)

	elif message.text.lower() == '🔹 ярославль':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.yaroslavl_rayons)
		bot.register_next_step_handler(msg, yaroslavl)

	elif message.text.lower() == '🔹 владивосток':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.vladivostok_rayons)
		bot.register_next_step_handler(msg, vladivostok)

	elif message.text.lower() == '🔹 томск':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.tomsk_rayons)
		bot.register_next_step_handler(msg, tomsk)

	elif message.text.lower() == '🔹 оренбург':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.orenburb_rayons)
		bot.register_next_step_handler(msg, orenbyrg)

	elif message.text.lower() == '🔹 пермь':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.perm_rayons)
		bot.register_next_step_handler(msg, perm)

	elif message.text.lower() == '🔹 воронеж':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.voroneg_rayons)
		bot.register_next_step_handler(msg, voroneg)

	elif message.text.lower() == '🔹 волгоград':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.volgograd_rayons)
		bot.register_next_step_handler(msg, volgograd)

	elif message.text.lower() == '🔹 уфа':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.ufa_rayons)
		bot.register_next_step_handler(msg, ufa)

	elif message.text.lower() == '🔹 красноярск':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.krasnoyarsk_rayons)
		bot.register_next_step_handler(msg, krasnoyarsk)

	elif message.text.lower() == '🔹 тольятти':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.toliyati_rayons)
		bot.register_next_step_handler(msg, toliyati)
	elif message.text.lower() == '🔹 феодосия':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboards.feodisiya_rayons)
		bot.register_next_step_handler(msg, feodosiya)
	elif message.text.lower() == '🔹 тимашевск':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.timashevsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text.lower() == '🔹 ростов-на-дону':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ufa)
		bot.register_next_step_handler(msg, what_tovar)
#-----------------------Районы-----------------------

def moskow(message):
	if message.text == '🔹 Измайлово':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.moskow_tovar)
		
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Сокольники':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.moskow_tovar)
		
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Внуково':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.moskow_tovar)
		
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Кунцево':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.moskow_tovar)
		
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Крюково':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.moskow_tovar)
		
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Щукино':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.moskow_tovar)
		
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Лефортово':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.moskow_tovar)
		
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Выхино-Жулебина':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.moskow_tovar)
		
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Медведково':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.moskow_tovar)
		
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Якиманка':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.moskow_tovar)
		
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Отрадное':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.moskow_tovar)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)





def sankt_piter(message):
	if message.text == '🔹 Центральный район':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.sankt_tovar)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Невский район':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.sankt_tovar)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Кировский район':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.sankt_tovar)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Петроградский район':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.sankt_tovar)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Московский район':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.sankt_tovar)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Василеостровской район':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.sankt_tovar)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)



def novosubirsk(message):
	if message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novosubirsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Дзержинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novosubirsk)
		bot.register_next_step_handler(msg, what_tovar)
		
	elif message.text == '🔹 Советский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novosubirsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Центральный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novosubirsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Железнодорожный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novosubirsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Калининский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novosubirsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novosubirsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


def ekb(message):
	if message.text == '🔹 Верх-Исетский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ekb)
		bot.register_next_step_handler(msg, what_tovar)
	if message.text == '🔹 Железнодорожный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ekb)
		bot.register_next_step_handler(msg, what_tovar)
	if message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ekb)
		bot.register_next_step_handler(msg, what_tovar)
	if message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ekb)
		bot.register_next_step_handler(msg, what_tovar)
	if message.text == '🔹 Октябрьский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ekb)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)



def novgorod(message):
	if message.text == '🔹 Автозаводский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novgorod)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Богородский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novgorod)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Бутурлинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novgorod)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Гагинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novgorod)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Вознесенский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novgorod)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ветлужский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novgorod)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Варнавинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novgorod)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Вачский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.novgorod)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


def kazan(message):
	if message.text == '🔹 Советский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.kazan)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Приволжский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.kazan)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ново-Савиновский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.kazan)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Московский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.kazan)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.kazan)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Вахитовский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.kazan)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)




def chelabinsk(message):
	if message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.chelabinsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 ЧМЗ':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.chelabinsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Северо-Запад':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.chelabinsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 АМЗ':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.chelabinsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Центральный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.chelabinsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ново-Синеглазово':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.chelabinsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)



def omsk(message):
	if message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.omsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.omsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Октябрьский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.omsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Советский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.omsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Центральный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.omsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


def samara(message):
	if message.text == '🔹 Железнодорожный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.samara)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.samara)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Красноглинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.samara)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Куйбышевский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.samara)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.samara)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Октябрьский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.samara)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


def krasnodar(message):
	if message.text == '🔹 Западный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnodar)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Карасунский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnodar)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Прикубанский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnodar)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Центральный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnodar)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)



def saratov(message):
	if message.text == '🔹 Волжский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.saratov)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Заводской':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.saratov)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.saratov)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Октябрьский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.saratov)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Фрунзенский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.saratov)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.saratov)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)



def tymen(message):
	if message.text == '🔹 Восточный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tymen)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Калининский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tymen)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tymen)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Центральный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tymen)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


def barnaul(message):
	if message.text == '🔹 Железнодорожный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tymen)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Индустриальный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tymen)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tymen)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Центральный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tymen)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Октябрьский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tymen)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)



def irkytsk(message):
	if message.text == '🔹 Ленинский округ':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.irkytsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Октябрьский округ':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.irkytsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Правобережный округ':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.irkytsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Свердловский округ':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.irkytsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)



def yaroslavl(message):
	if message.text == '🔹 Дзержинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.yaroslavl)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Заволжский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.yaroslavl)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.yaroslavl)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Красноперекопский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.yaroslavl)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.yaroslavl)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Фрунзенский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.yaroslavl)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


def tomsk(message):
	if message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tomsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tomsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Октябрьский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tomsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Советский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.tomsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


def orenbyrg(message):
	if message.text == '🔹 Дзержинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.orenburb)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.orenburb)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Промышленный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.orenburb)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Центральный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.orenburb)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


def vladivostok(message):
	if message.text == '🔹 Первомайский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.vladivostok)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.vladivostok)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Советский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.vladivostok)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Первореченский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.vladivostok)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Фрунзенский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.vladivostok)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


def volgograd(message):
	if message.text == '🔹 Ворошиловский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.volgograd)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Дзержинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.volgograd)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Советский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.volgograd)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.volgograd)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Красноармейский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.volgograd)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Краснооктябрьский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.volgograd)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Советский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.volgograd)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Тракторозаводский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.volgograd)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Центральный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.volgograd)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

def voroneg(message):
	if message.text == '🔹 Железнодорожный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.voroneg)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Левобережный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.voroneg)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.voroneg)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Коминтерновский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.voroneg)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Советский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.voroneg)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Центральный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.voroneg)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

def perm(message):
	if message.text == '🔹 Свердловский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.perm)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Орджоникидзевский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.perm)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.perm)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Мотовилихинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.perm)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Индустриальный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.perm)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Дзержинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.perm)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.perm)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)






def ufa(message):
	if message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ufa)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Советский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ufa)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ufa)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Демский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ufa)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Орджоникидзевский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ufa)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Октябрьский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ufa)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Калининский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.ufa)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


def krasnoyarsk(message):
	if message.text == '🔹 Железнодорожный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnoyarsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Кировский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnoyarsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Ленинский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnoyarsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Октябрьский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnoyarsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Свердловский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnoyarsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Советский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnoyarsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Центральный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnoyarsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)





def toliyati(message):
	if message.text == '🔹 Автозаводский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnoyarsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Комсомольский':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnoyarsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Центральный':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.krasnoyarsk)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)



def feodosiya(message):
	if message.text == '🔹 Береговое':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.feodisiya)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Щебетовка':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.feodisiya)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Орджоникидзе':
		msg = bot.send_message(message.chat.id, '⬇️ Выберите товар ⬇️', reply_markup=keyboards.feodisiya)
		bot.register_next_step_handler(msg, what_tovar)
	elif message.text == '🔹 Главная':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


def what_tovar(message):
	global tovar
	tovar = message.text
	msg = bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboards.oplata)
	bot.register_next_step_handler(msg, what_oplata)


#-----------------------Товары/Оплата-----------------------
def what_oplata(message):
	userid = str(message.chat.id)
	connection = sqlite3.connect('database.sqlite')
	q = connection.cursor()
	q.execute("select ref_user from users where Id =" + userid )
	ref_user = q.fetchone()[0]
	q.execute('select karta from config where Id = 1')
	karta = q.fetchone()[0]
	q.execute('select qiwi from config where Id = 1')
	qiwi = q.fetchone()[0]
	q.execute('select bitcoin from config where Id = 1')
	bitcoin = q.fetchone()[0]
	if message.text == 'Qiwi':
		if tovar == 'СК (син.крис) {0.3г/900 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.3г/900 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 900 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 900 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1300 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1300 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1300 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1300 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {1г/2200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {1г/2200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 2200 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2200 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {1г/1100 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {1г/1100 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1100 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1100 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {2г/2000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {2г/2000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 2000 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2000 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {5г/4000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {5г/4000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 4000 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 4000 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'MEPHEDRONE крис {1г/2100 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 MEPHEDRONE крис {1г/2100 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 2100 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2100 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Амфетамин HQ {2г/2400 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Амфетамин HQ {2г/2400 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 2400 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2400 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Шишки OG Kush {1г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Шишки OG Kush {1г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1200 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Шишки OG Kush {2г/2200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Шишки OG Kush {2г/2200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 2200 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2200 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Шишки OG Kush {5г/4200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Шишки OG Kush {5г/4200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 4200 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 4200 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'РОСС {5г/3000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 РОСС {5г/3000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 3000 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 3000 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Героин HQ {0.5г/1700 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Героин HQ {0.5г/1700 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1700 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1700 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.3г/700 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.3г/700 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 700 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 700 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1200 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Амфетамин HQ {2г/2000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Амфетамин HQ {2г/2000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 2000 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2000 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1200 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'РОСС {3г/1900 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 РОСС {3г/1900 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1900 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1900 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1200 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1100 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1100 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1100 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1100 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {1г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {1г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1200 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'MEPHEDRONE крис {1г/2000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 MEPHEDRONE крис {1г/2000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 2000 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2000 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Амфетамин HQ {2г/2200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Амфетамин HQ {2г/2200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 2200 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2200 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Героин HQ {0.5г/1300 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Героин HQ {0.5г/1300 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1300 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1300 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш SF {1г - 1000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш SF {1г - 1000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 1000 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1000 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш SF {5г - 3000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Героин HQ {5г - 3000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на QIWI.\n\n➖➖➖➖➖➖➖➖➖➖\n\n🏷QIWI кошелек: <code>'+str(qiwi)+'</code>\n\n💵Сумма: 3000 рублей\n\n💬Комментарий к платежу: ' + str(ref_user) + ' \n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 3000 или больше.\n\nБЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		else:
			bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)




	elif message.text == 'Карта':
		if tovar == 'СК (син.крис) {0.3г/900 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.3г/900 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 900 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 900 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1300 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1300 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта:  <code>'+str(karta)+'</code>\n\n💵Сумма: 1300 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1300 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {1г/2200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {1г/2200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта:  <code>'+str(karta)+'</code>\n\n💵Сумма: 2200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {1г/1100 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {1г/1100 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта:  <code>'+str(karta)+'</code>\n\n💵Сумма: 1100 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1100 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {2г/2000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {2г/2000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта:  <code>'+str(karta)+'</code>\n\n💵Сумма: 2000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {5г/4000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {5г/4000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 4000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 4000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'MEPHEDRONE крис {1г/2100 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 MEPHEDRONE крис {1г/2100 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 2100 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2100 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Амфетамин HQ {2г/2400 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Амфетамин HQ {2г/2400 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 2400 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2400 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Шишки OG Kush {1г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Шишки OG Kush {1г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 1200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Шишки OG Kush {2г/2200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Шишки OG Kush {2г/2200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 2200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Шишки OG Kush {5г/4200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Шишки OG Kush {5г/4200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 4200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 4200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'РОСС {5г/3000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 РОСС {5г/3000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 3000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 3000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Героин HQ {0.5г/1700 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Героин HQ {0.5г/1700 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 1700 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1700 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.3г/700 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.3г/700 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 700 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 700 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 1200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Амфетамин HQ {2г/2000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Амфетамин HQ {2г/2000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 2000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 1200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'РОСС {3г/1900 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 РОСС {3г/1900 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 1900 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1900 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 1200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1100 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1100 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 1100 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1100 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {1г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {1г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 1200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'MEPHEDRONE крис {1г/2000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 MEPHEDRONE крис {1г/2000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 2000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Амфетамин HQ {2г/2200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Амфетамин HQ {2г/2200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 2200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Героин HQ {0.5г/1300 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Героин HQ {0.5г/1300 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 1300 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1300 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш SF {1г - 1000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш SF {1г - 1000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 1000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш SF {5г - 3000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Героин HQ {5г - 3000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 3000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 3000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		else:
			bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

	elif message.text == 'Bitcoin':
		if tovar == 'СК (син.крис) {0.3г/900 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.3г/900 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 900 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 900 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1300 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1300 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 1300 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1300 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {1г/2200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {1г/2200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 2200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {1г/1100 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {1г/1100 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 1100 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1100 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {2г/2000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {2г/2000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 2000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {5г/4000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {5г/4000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 4000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 4000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'MEPHEDRONE крис {1г/2100 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 MEPHEDRONE крис {1г/2100 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 2100 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2100 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Амфетамин HQ {2г/2400 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Амфетамин HQ {2г/2400 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 2400 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2400 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Шишки OG Kush {1г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Шишки OG Kush {1г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 1200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Шишки OG Kush {2г/2200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Шишки OG Kush {2г/2200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 2200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Шишки OG Kush {5г/4200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Шишки OG Kush {5г/4200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 4200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 4200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'РОСС {5г/3000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 РОСС {5г/3000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 3000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 3000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Героин HQ {0.5г/1700 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Героин HQ {0.5г/1700 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 1700 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1700 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.3г/700 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.3г/700 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 700 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 700 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 1200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Амфетамин HQ {2г/2000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Амфетамин HQ {2г/2000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 2000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 1200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'РОСС {3г/1900 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 РОСС {3г/1900 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на карту.\n➖➖➖➖➖➖➖➖➖➖\n🏷Карта: <code>'+str(karta)+'</code>\n\n💵Сумма: 1900 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1900 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 1200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'СК (син.крис) {0.5г/1100 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 СК (син.крис) {0.5г/1100 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 1100 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1100 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш EURO {1г/1200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш EURO {1г/1200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 1200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'MEPHEDRONE крис {1г/2000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 MEPHEDRONE крис {1г/2000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 2000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Амфетамин HQ {2г/2200 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Амфетамин HQ {2г/2200 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 2200 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 2200 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Героин HQ {0.5г/1300 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Героин HQ {0.5г/1300 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 1300 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1300 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш SF {1г - 1000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Гашиш SF {1г - 1000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 1000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 1000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		elif tovar == 'Гашиш SF {5г - 3000 RUB}':
			bot.send_message(message.chat.id, 'Вы приобретаете:\n\n👉 Героин HQ {5г - 3000 RUB}\n\n➖➖➖➖➖➖➖➖➖➖\n\nВы зарезервировали товар на 30⌛️ минут.\nЧтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n\n➖➖➖➖➖➖➖➖➖➖\n🏷Кошелек: <code>'+str(bitcoin)+'</code>\n\n💵Сумма: 3000 рублей\n\n➖➖➖➖➖➖➖➖➖➖\n\nСумма платежа должна быть равна 3000 или больше.',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
		else:
			bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

def admin_new_karta(message):
	new_karta = message.text
	connection = sqlite3.connect('database.sqlite')
	q = connection.cursor()
	try:
		q.execute("update config set karta = " + str( new_karta ) + " where id = 1")
		connection.commit()
		q.close()
		connection.close()
		bot.send_message(message.chat.id, 'Успешно!', reply_markup=keyboards.admin)
	except:
		bot.send_message(admin, 'Ошибка', reply_markup=keyboards.admin)

def admin_new_qiwi(message):
	new_qiwi = message.text
	connection = sqlite3.connect('database.sqlite')
	q = connection.cursor()
	try:
		q.execute("update config set qiwi = " + str( new_qiwi ) + " where id = 1")
		connection.commit()
		q.close()
		connection.close()
		bot.send_message(message.chat.id, 'Успешно!', reply_markup=keyboards.admin)
	except:
		bot.send_message(admin, 'Ошибка', reply_markup=keyboards.admin)


#ТОПОВЫЙ КАНАЛ СО СЛИВАМИ СКРИПТОВ  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT 

bot.polling(none_stop=True)
#ТОПОВЫЙ КАНАЛ СО СЛИВАМИ СКРИПТОВ  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT 
