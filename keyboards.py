import telebot
#ТОПОВЫЙ КАНАЛ СО СЛИВАМИ СКРИПТОВ  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT 

keyboardMain = telebot.types.ReplyKeyboardMarkup(True)
keyboardMain.row('🔹 Москва')
keyboardMain.row('🔹 Санкт-Петербург')
keyboardMain.row('🔹 Ростов-на-Дону')
keyboardMain.row('🔹 Екатеринбург')
keyboardMain.row('🔹 Челябинск')
keyboardMain.row('🔹 Новосибирск')
keyboardMain.row('🔹 Нижний Новгород')
keyboardMain.row('🔹 Казань')
keyboardMain.row('🔹 Омск')
keyboardMain.row('🔹 Самара')
keyboardMain.row('🔹 Краснодар')
keyboardMain.row('🔹 Саратов')
keyboardMain.row('🔹 Тюмень')
keyboardMain.row('🔹 Барнаул')
keyboardMain.row('🔹 Иркутск')
keyboardMain.row('🔹 Ярославль')
keyboardMain.row('🔹 Владивосток')
keyboardMain.row('🔹 Оренбург')
keyboardMain.row('🔹 Томск')
keyboardMain.row('🔹 Воронеж')
keyboardMain.row('🔹 Пермь')
keyboardMain.row('🔹 Волгоград')
keyboardMain.row('🔹 Уфа')
keyboardMain.row('🔹 Красноярск')
keyboardMain.row('🔹 Тольятти')
keyboardMain.row('🔹 Феодосия')
keyboardMain.row('🔹 Тимашевск')

moskow_rayons = telebot.types.ReplyKeyboardMarkup(True)
moskow_rayons.row('🔹 Измайлово')
moskow_rayons.row('🔹 Сокольники')
moskow_rayons.row('🔹 Внуково')
moskow_rayons.row('🔹 Кунцево')
moskow_rayons.row('🔹 Крюково')
moskow_rayons.row('🔹 Щукино')
moskow_rayons.row('🔹 Лефортово')
moskow_rayons.row('🔹 Выхино-Жулебина')
moskow_rayons.row('🔹 Медведково')
moskow_rayons.row('🔹 Якиманка')
moskow_rayons.row('🔹 Отрадное')
moskow_rayons.row('🔹 Главная')

moskow_tovar = telebot.types.ReplyKeyboardMarkup(True)
moskow_tovar.row('СК (син.крис) {0.3г/900 RUB}',)
moskow_tovar.row('СК (син.крис) {0.5г/1300 RUB}')
moskow_tovar.row('СК (син.крис) {1г/2200 RUB}')
moskow_tovar.row('Гашиш EURO {1г/1100 RUB}')
moskow_tovar.row('Гашиш EURO {2г/2000 RUB}')
moskow_tovar.row('Гашиш EURO {5г/4000 RUB}')
moskow_tovar.row('MEPHEDRONE крис {1г/2100 RUB}')
moskow_tovar.row('Амфетамин HQ {2г/2400 RUB}')
moskow_tovar.row('Шишки OG Kush {1г/1200 RUB}')
moskow_tovar.row('Шишки OG Kush {2г/2200 RUB}')
moskow_tovar.row('Шишки OG Kush {5г/4200 RUB}')
moskow_tovar.row('РОСС {5г/3000 RUB}')
moskow_tovar.row('Героин HQ {0.5г/1700 RUB}')


sankt_rayons = telebot.types.ReplyKeyboardMarkup(True)
sankt_rayons.row('🔹 Центральный район')
sankt_rayons.row('🔹 Невский район')
sankt_rayons.row('🔹 Кировский район')
sankt_rayons.row('🔹 Петроградский район')
sankt_rayons.row('🔹 Московский район')
sankt_rayons.row('🔹 Василеостровской район')
sankt_rayons.row('🔹 Главная')

sankt_tovar = telebot.types.ReplyKeyboardMarkup(True)
sankt_tovar.row('СК (син.крис) {0.3г/700 RUB')
sankt_tovar.row('СК (син.крис) {0.5г/1200 RUB}')
sankt_tovar.row('СК (син.крис) {1г/2200 RUB}')
sankt_tovar.row('Гашиш EURO {1г/1100 RUB}')
sankt_tovar.row('Гашиш EURO {2г/2000 RUB}')
sankt_tovar.row('Гашиш EURO {5г/4000 RUB}')
sankt_tovar.row('MEPHEDRONE крис {1г/2100 RUB}')
sankt_tovar.row('Амфетамин HQ {2г/2000 RUB}')
sankt_tovar.row('Шишки OG Kush {1г/1200 RUB}')


novosubirsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
novosubirsk_rayons.row('🔹 Кировский')
novosubirsk_rayons.row('🔹 Дзержинский')
novosubirsk_rayons.row('🔹 Советский')
novosubirsk_rayons.row('🔹 Центральный')
novosubirsk_rayons.row('🔹 Железнодорожный')
novosubirsk_rayons.row('🔹 Калининский')
novosubirsk_rayons.row('🔹 Ленинский')
novosubirsk_rayons.row('🔹 Главная')


novosubirsk = telebot.types.ReplyKeyboardMarkup(True)
novosubirsk.row('СК (син.крис) {0.3г/700 RUB')
novosubirsk.row('СК (син.крис) {0.5г/1200 RUB}')
novosubirsk.row('СК (син.крис) {1г/2200 RUB}')
novosubirsk.row('Гашиш EURO {1г/1100 RUB}')
novosubirsk.row('Гашиш EURO {2г/2000 RUB}')
novosubirsk.row('Гашиш EURO {5г/4000 RUB}')
novosubirsk.row('РОСС {3г/1900 RUB}')
novosubirsk.row('Амфетамин HQ {2г/2000 RUB}')
novosubirsk.row('Шишки OG Kush {1г/1200 RUB}')

#ТОПОВЫЙ КАНАЛ СО СЛИВАМИ СКРИПТОВ  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT  @END_SOFT 


ekb_rayons = telebot.types.ReplyKeyboardMarkup(True)
ekb_rayons.row('🔹 Верх-Исетский')
ekb_rayons.row('🔹 Железнодорожный')
ekb_rayons.row('🔹 Кировский')
ekb_rayons.row('🔹 Ленинский')
ekb_rayons.row('🔹 Октябрьский')
ekb_rayons.row('🔹 Главная')


ekb =  telebot.types.ReplyKeyboardMarkup(True)
ekb.row('СК (син.крис) {0.3г/900 RUB}')
ekb.row('СК (син.крис) {0.5г/1300 RUB}')
ekb.row('СК (син.крис) {1г/2200 RUB}')
ekb.row('Гашиш EURO {1г/1100 RUB}')
ekb.row('Гашиш EURO {2г/2000 RUB}')
ekb.row('Гашиш EURO {5г/4000 RUB}')
ekb.row('MEPHEDRONE крис {1г/2100 RUB}')
ekb.row('Амфетамин HQ {2г/2400 RUB}')
ekb.row('Шишки OG Kush {1г/1200 RUB}')
ekb.row('Шишки OG Kush {2г/2200 RUB}')
ekb.row('Шишки OG Kush {5г/4200 RUB}')
ekb.row('РОСС {5г/3000 RUB}')
ekb.row('Героин HQ {0.5г/1700 RUB}')



novgorod_rayons = telebot.types.ReplyKeyboardMarkup(True)
novgorod_rayons.row('🔹 Автозаводский')
novgorod_rayons.row('🔹 Богородский')
novgorod_rayons.row('🔹 Бутурлинский')
novgorod_rayons.row('🔹 Гагинский')
novgorod_rayons.row('🔹 Вознесенский')
novgorod_rayons.row('🔹 Ветлужский')
novgorod_rayons.row('🔹 Варнавинский')
novgorod_rayons.row('🔹 Вачский')
novgorod_rayons.row('🔹 Главная')


novgorod = telebot.types.ReplyKeyboardMarkup(True)
novgorod.row('СК (син.крис) {0.3г/800 RUB}')
novgorod.row('СК (син.крис) {0.5г/1200 RUB}')
novgorod.row('СК (син.крис) {1г/2000 RUB}')
novgorod.row('Гашиш EURO {1г/1100 RUB}')
novgorod.row('Гашиш EURO {2г/2000 RUB}')
novgorod.row('Гашиш EURO {5г/4000 RUB}')
novgorod.row('MEPHEDRONE крис {1г/2100 RUB}')
novgorod.row('Амфетамин HQ {2г/2400 RUB}')
novgorod.row('Шишки OG Kush {1г/1200 RUB}')
novgorod.row('Шишки OG Kush {2г/2200 RUB}')
novgorod.row('Шишки OG Kush {5г/4200 RUB}')
novgorod.row('РОСС {5г/3000 RUB}')
novgorod.row('Героин HQ {0.5г/1700 RUB}')


kazan_rayons = telebot.types.ReplyKeyboardMarkup(True)
kazan_rayons.row('🔹 Советский')
kazan_rayons.row('🔹 Приволжский')
kazan_rayons.row('🔹 Ново-Савиновский')
kazan_rayons.row('🔹 Московский')
kazan_rayons.row('🔹 Кировский')
kazan_rayons.row('🔹 Вахитовский')
kazan_rayons.row('🔹 Главная')

kazan = telebot.types.ReplyKeyboardMarkup(True)
kazan.row('СК (син.крис) {0.3г/800 RUB}')
kazan.row('СК (син.крис) {0.5г/1200 RUB}')
kazan.row('СК (син.крис) {1г/2000 RUB}')
kazan.row('Гашиш EURO {1г/1100 RUB}')
kazan.row('Гашиш EURO {2г/2000 RUB}')
kazan.row('Гашиш EURO {5г/4000 RUB}')
kazan.row('MEPHEDRONE крис {1г/2100 RUB}')
kazan.row('Амфетамин HQ {1г/1500 RUB}')
kazan.row('Шишки OG Kush {1г/1200 RUB}')
kazan.row('Шишки OG Kush {2г/2200 RUB}')
kazan.row('Шишки OG Kush {5г/4200 RUB}')
kazan.row('РОСС {5г/3000 RUB}')
kazan.row('Героин HQ {0.5г/1700 RUB}')



chelabinsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
chelabinsk_rayons.row('🔹 Ленинский')
chelabinsk_rayons.row('🔹 ЧМЗ')
chelabinsk_rayons.row('🔹 Северо-Запад')
chelabinsk_rayons.row('🔹 АМЗ')
chelabinsk_rayons.row('🔹 Центральный')
chelabinsk_rayons.row('🔹 Ново-Синеглазово')
chelabinsk_rayons.row('🔹 Главная')


chelabinsk = telebot.types.ReplyKeyboardMarkup(True)
chelabinsk.row('СК (син.крис) {0.3г/900 RUB}')
chelabinsk.row('СК (син.крис) {0.5г/1300 RUB}')
chelabinsk.row('СК (син.крис) {1г/2200 RUB}')
chelabinsk.row('Гашиш EURO {1г/1100 RUB}')
chelabinsk.row('Гашиш EURO {2г/2000 RUB}')
chelabinsk.row('Гашиш EURO {5г/4000 RUB}')
chelabinsk.row('MEPHEDRONE крис {1г/2100 RUB}')
chelabinsk.row('Амфетамин HQ {2г/2400 RUB}')
chelabinsk.row('Шишки OG Kush {1г/1200 RUB}')
chelabinsk.row('Шишки OG Kush {2г/2200 RUB}')
chelabinsk.row('Шишки OG Kush {5г/4200 RUB}')
chelabinsk.row('РОСС {5г/3000 RUB}')
chelabinsk.row('Героин HQ {0.5г/1700 RUB}')



omsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
omsk_rayons.row('🔹 Кировский')
omsk_rayons.row('🔹 Ленинский')
omsk_rayons.row('🔹 Октябрьский')
omsk_rayons.row('🔹 Советский')
omsk_rayons.row('🔹 Центральный')
omsk_rayons.row('🔹 Главная')



omsk = telebot.types.ReplyKeyboardMarkup(True)
omsk.row('СК (син.крис) {0.3г/900 RUB}')
omsk.row('СК (син.крис) {0.5г/1300 RUB}')
omsk.row('СК (син.крис) {1г/2200 RUB}')
omsk.row('Гашиш EURO {1г/1100 RUB}')
omsk.row('Гашиш EURO {2г/2000 RUB}')
omsk.row('Гашиш EURO {5г/4000 RUB}')
omsk.row('MEPHEDRONE крис {1г/2100 RUB}')
omsk.row('Амфетамин HQ {2г/2400 RUB}')
omsk.row('Шишки OG Kush {1г/1200 RUB}')
omsk.row('Шишки OG Kush {2г/2200 RUB}')
omsk.row('Шишки OG Kush {5г/4200 RUB}')
omsk.row('РОСС {5г/3000 RUB}')
omsk.row('Героин HQ {0.5г/1700 RUB}')



samara_rayons = telebot.types.ReplyKeyboardMarkup(True)
samara_rayons.row('🔹 Железнодорожный')
samara_rayons.row('🔹 Кировский')
samara_rayons.row('🔹 Красноглинский')
samara_rayons.row('🔹 Куйбышевский')
samara_rayons.row('🔹 Ленинский')
samara_rayons.row('🔹 Октябрьский')
samara_rayons.row('🔹 Главная')



samara = telebot.types.ReplyKeyboardMarkup(True)
samara.row('СК (син.крис) {0.3г/800 RUB}')
samara.row('СК (син.крис) {0.5г/1200 RUB}')
samara.row('СК (син.крис) {1г/2000 RUB}')
samara.row('Гашиш EURO {1г/1100 RUB}')
samara.row('Гашиш EURO {2г/2000 RUB}')
samara.row('Гашиш EURO {5г/4000 RUB}')
samara.row('MEPHEDRONE крис {1г/2100 RUB}')
samara.row('Амфетамин HQ {1г/1500 RUB}')
samara.row('Шишки OG Kush {1г/1200 RUB}')
samara.row('Шишки OG Kush {2г/2200 RUB}')
samara.row('Шишки OG Kush {5г/4200 RUB}')
samara.row('РОСС {5г/3000 RUB}')
samara.row('Героин HQ {0.5г/1700 RUB}')



krasnodar_rayons = telebot.types.ReplyKeyboardMarkup(True)
krasnodar_rayons.row('🔹 Западный')
krasnodar_rayons.row('🔹 Карасунский')
krasnodar_rayons.row('🔹 Прикубанский')
krasnodar_rayons.row('🔹 Центральный')

krasnodar= telebot.types.ReplyKeyboardMarkup(True)
krasnodar.row('СК (син.крис) {0.5г/1300 RUB}')
krasnodar.row('СК (син.крис) {1г/2200 RUB}')
krasnodar.row('Гашиш EURO {1г/1100 RUB}')
krasnodar.row('MEPHEDRONE крис {1г/2100 RUB}')
krasnodar.row('Амфетамин HQ {2г/2400 RUB}')
krasnodar.row('Шишки OG Kush {1г/1200 RUB}')
krasnodar.row('Героин HQ {0.5г/1700 RUB}')



saratov_rayons = telebot.types.ReplyKeyboardMarkup(True)
saratov_rayons.row('🔹 Волжский')
saratov_rayons.row('🔹 Заводской')
saratov_rayons.row('🔹 Кировский')
saratov_rayons.row('🔹 Ленинский')
saratov_rayons.row('🔹 Октябрьский')
saratov_rayons.row('🔹 Фрунзенский')

saratov = telebot.types.ReplyKeyboardMarkup(True)
saratov.row('СК (син.крис) {0.3г/900 RUB}')
saratov.row('СК (син.крис) {0.5г/1300 RUB}')
saratov.row('СК (син.крис) {1г/2200 RUB}')
saratov.row('Гашиш EURO {1г/1100 RUB}')
saratov.row('Гашиш EURO {2г/2000 RUB}')
saratov.row('Гашиш EURO {5г/4000 RUB}')
saratov.row('MEPHEDRONE крис {1г/2100 RUB}')
saratov.row('Амфетамин HQ {2г/2400 RUB}')
saratov.row('Шишки OG Kush {1г/1200 RUB}')
saratov.row('Шишки OG Kush {2г/2200 RUB}')
saratov.row('Шишки OG Kush {5г/4200 RUB}')
saratov.row('РОСС {5г/3000 RUB}')
saratov.row('Героин HQ {0.5г/1700 RUB}')





tymen_rayons = telebot.types.ReplyKeyboardMarkup(True)
tymen_rayons.row('🔹 Восточный')
tymen_rayons.row('🔹 Калининский')
tymen_rayons.row('🔹 Ленинский')
tymen_rayons.row('🔹 Центральный')




tymen = telebot.types.ReplyKeyboardMarkup(True)
tymen.row('СК (син.крис) {0.5г/1300 RUB}')
tymen.row('СК (син.крис) {1г/2200 RUB}')
tymen.row('Гашиш EURO {1г/1100 RUB}')
tymen.row('MEPHEDRONE крис {1г/2100 RUB}')
tymen.row('Амфетамин HQ {2г/2400 RUB}')
tymen.row('Шишки OG Kush {1г/1200 RUB}')
tymen.row('Героин HQ {0.5г/1700 RUB}')

barnaul_rayons = telebot.types.ReplyKeyboardMarkup(True)
barnaul_rayons.row('🔹 Железнодорожный')
barnaul_rayons.row('🔹 Ленинский')
barnaul_rayons.row('🔹 Индустриальный')
barnaul_rayons.row('🔹 Октябрьский')
barnaul_rayons.row('🔹 Центральный')


barnaul = telebot.types.ReplyKeyboardMarkup(True)
barnaul.row('СК (син.крис) {0.3г/900 RUB}')
barnaul.row('СК (син.крис) {0.5г/1300 RUB}')
barnaul.row('СК (син.крис) {1г/2200 RUB}')
barnaul.row('Гашиш EURO {1г/1100 RUB}')
barnaul.row('Гашиш EURO {2г/2000 RUB}')
barnaul.row('Гашиш EURO {5г/4000 RUB}')
barnaul.row('MEPHEDRONE крис {1г/2100 RUB}')
barnaul.row('Амфетамин HQ {2г/2400 RUB}')
barnaul.row('Шишки OG Kush {1г/1200 RUB}')
barnaul.row('Шишки OG Kush {2г/2200 RUB}')
barnaul.row('Шишки OG Kush {5г/4200 RUB}')
barnaul.row('РОСС {5г/3000 RUB}')
barnaul.row('Героин HQ {0.5г/1700 RUB}')


irkytsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
irkytsk_rayons.row('🔹 Ленинский округ')
irkytsk_rayons.row('🔹 Октябрьский округ')
irkytsk_rayons.row('🔹 Правобережный округ')
irkytsk_rayons.row('🔹 Свердловский округ')



irkytsk = telebot.types.ReplyKeyboardMarkup(True)
irkytsk.row('СК (син.крис) {0.5г/1300 RUB}')
irkytsk.row('СК (син.крис) {1г/2200 RUB}')
irkytsk.row('Гашиш EURO {1г/1100 RUB}')
irkytsk.row('MEPHEDRONE крис {1г/2100 RUB}')
irkytsk.row('Амфетамин HQ {2г/2400 RUB}')
irkytsk.row('Шишки OG Kush {1г/1200 RUB}')
irkytsk.row('Героин HQ {0.5г/1700 RUB}')



yaroslavl_rayons = telebot.types.ReplyKeyboardMarkup(True)
yaroslavl_rayons.row('🔹 Дзержинский')
yaroslavl_rayons.row('🔹 Заволжский')
yaroslavl_rayons.row('🔹 Кировский')
yaroslavl_rayons.row('🔹 Красноперекопский')
yaroslavl_rayons.row('🔹 Ленинский')
yaroslavl_rayons.row('🔹 Фрунзенский')

yaroslavl = telebot.types.ReplyKeyboardMarkup(True)
yaroslavl.row('СК (син.крис) {0.3г/900 RUB}')
yaroslavl.row('СК (син.крис) {0.5г/1300 RUB}')
yaroslavl.row('СК (син.крис) {1г/2200 RUB}')
yaroslavl.row('Гашиш EURO {1г/1100 RUB}')
yaroslavl.row('Гашиш EURO {2г/2000 RUB}')
yaroslavl.row('Гашиш EURO {5г/4000 RUB}')
yaroslavl.row('MEPHEDRONE крис {1г/2100 RUB}')
yaroslavl.row('Амфетамин HQ {2г/2400 RUB}')
yaroslavl.row('Шишки OG Kush {1г/1200 RUB}')
yaroslavl.row('Шишки OG Kush {2г/2200 RUB}')
yaroslavl.row('Шишки OG Kush {5г/4200 RUB}')
yaroslavl.row('РОСС {5г/3000 RUB}')
yaroslavl.row('Героин HQ {0.5г/1700 RUB}')


vladivostok_rayons = telebot.types.ReplyKeyboardMarkup(True)
vladivostok_rayons.row('🔹 Ленинский')
vladivostok_rayons.row('🔹 Первомайский')
vladivostok_rayons.row('🔹 Первореченский')
vladivostok_rayons.row('🔹 Советский')
vladivostok_rayons.row('🔹 Фрунзенский')


vladivostok = telebot.types.ReplyKeyboardMarkup(True)
vladivostok.row('СК (син.крис) {0.3г/900 RUB}')
vladivostok.row('СК (син.крис) {0.5г/1300 RUB}')
vladivostok.row('СК (син.крис) {1г/2200 RUB}')
vladivostok.row('Гашиш EURO {1г/1100 RUB}')
vladivostok.row('Гашиш EURO {2г/2000 RUB}')
vladivostok.row('Гашиш EURO {5г/4000 RUB}')
vladivostok.row('MEPHEDRONE крис {1г/2100 RUB}')


orenburb_rayons = telebot.types.ReplyKeyboardMarkup(True)
orenburb_rayons.row('🔹 Дзержинский')
orenburb_rayons.row('🔹 Ленинский')
orenburb_rayons.row('🔹 Промышленный')
orenburb_rayons.row('🔹 Центральный')


orenburb = telebot.types.ReplyKeyboardMarkup(True)
orenburb.row('СК (син.крис) {0.3г/900 RUB}')
orenburb.row('СК (син.крис) {0.5г/1300 RUB}')
orenburb.row('СК (син.крис) {1г/2200 RUB}')
orenburb.row('Гашиш EURO {1г/1100 RUB}')
orenburb.row('Гашиш EURO {2г/2000 RUB}')
orenburb.row('Гашиш EURO {5г/4000 RUB}')
orenburb.row('MEPHEDRONE крис {1г/2100 RUB}')

tomsk_rayons = telebot.types.ReplyKeyboardMarkup(True) 
tomsk_rayons.row('🔹 Кировский')
tomsk_rayons.row('🔹 Ленинский')
tomsk_rayons.row('🔹 Октябрьский')
tomsk_rayons.row('🔹 Советский')


tomsk = telebot.types.ReplyKeyboardMarkup(True) 
tomsk.row('СК (син.крис) {0.3г/900 RUB}')
tomsk.row('СК (син.крис) {0.5г/1300 RUB}')
tomsk.row('СК (син.крис) {1г/2200 RUB}')
tomsk.row('Гашиш EURO {1г/1100 RUB}')
tomsk.row('Гашиш EURO {2г/2000 RUB}')
tomsk.row('Гашиш EURO {5г/4000 RUB}')
tomsk.row('MEPHEDRONE крис {1г/2100 RUB}')
tomsk.row('Амфетамин HQ {2г/2400 RUB}')
tomsk.row('Шишки OG Kush {1г/1200 RUB}')
tomsk.row('Шишки OG Kush {2г/2200 RUB}')
tomsk.row('Шишки OG Kush {5г/4200 RUB}')
tomsk.row('РОСС {5г/3000 RUB}')
tomsk.row('Героин HQ {0.5г/1700 RUB}')





volgograd_rayons = telebot.types.ReplyKeyboardMarkup(True) 
volgograd_rayons.row('🔹 Ворошиловский')
volgograd_rayons.row('🔹 Дзержинский')
volgograd_rayons.row('🔹 Кировский')
volgograd_rayons.row('🔹 Красноармейский')
volgograd_rayons.row('🔹 Краснооктябрьский')
volgograd_rayons.row('🔹 Советский')
volgograd_rayons.row('🔹 Тракторозаводский')
volgograd_rayons.row('🔹 Центральный')


volgograd = telebot.types.ReplyKeyboardMarkup(True) 
volgograd.row('СК (син.крис) {0.3г/800 RUB}')
volgograd.row('СК (син.крис) {0.5г/1200 RUB}')
volgograd.row('СК (син.крис) {1г/2000 RUB}')
volgograd.row('Гашиш EURO {1г/1100 RUB}')
volgograd.row('Гашиш EURO {2г/2000 RUB}')
volgograd.row('Гашиш EURO {5г/4000 RUB}')
volgograd.row('MEPHEDRONE крис {1г/2100 RUB}')
volgograd.row('Амфетамин HQ {1г/1500 RUB}')
volgograd.row('Шишки OG Kush {1г/1200 RUB}')
volgograd.row('Шишки OG Kush {2г/2200 RUB}')
volgograd.row('Шишки OG Kush {5г/4200 RUB}')
volgograd.row('РОСС {5г/3000 RUB}')
volgograd.row('Героин HQ {0.5г/1700 RUB}')


voroneg_rayons = telebot.types.ReplyKeyboardMarkup(True) 
voroneg_rayons.row('🔹 Железнодорожный')
voroneg_rayons.row('🔹 Коминтерновский')
voroneg_rayons.row('🔹 Левобережный')
voroneg_rayons.row('🔹 Ленинский')
voroneg_rayons.row('🔹 Советский')
voroneg_rayons.row('🔹 Центральный')


voroneg = telebot.types.ReplyKeyboardMarkup(True) 
voroneg.row('СК (син.крис) {0.3г/900 RUB}')
voroneg.row('СК (син.крис) {0.5г/1300 RUB}')
voroneg.row('СК (син.крис) {1г/2200 RUB}')
voroneg.row('Гашиш EURO {1г/1100 RUB}')
voroneg.row('Гашиш EURO {2г/2000 RUB}')
voroneg.row('Гашиш EURO {5г/4000 RUB}')
voroneg.row('MEPHEDRONE крис {1г/2100 RUB}')
voroneg.row('Амфетамин HQ {2г/2400 RUB}')
voroneg.row('Шишки OG Kush {1г/1200 RUB}')
voroneg.row('Шишки OG Kush {2г/2200 RUB}')
voroneg.row('Шишки OG Kush {5г/4200 RUB}')
voroneg.row('РОСС {5г/3000 RUB}')
voroneg.row('Героин HQ {0.5г/1700 RUB}')


perm_rayons = telebot.types.ReplyKeyboardMarkup(True)
perm_rayons.row('🔹 Свердловский')
perm_rayons.row('🔹 Орджоникидзевский')
perm_rayons.row('🔹 Кировский')
perm_rayons.row('🔹 Мотовилихинский')
perm_rayons.row('🔹 Индустриальный')
perm_rayons.row('🔹 Дзержинский')
perm_rayons.row('🔹 Ленинский')


perm = telebot.types.ReplyKeyboardMarkup(True) 
perm.row('СК (син.крис) {0.3г/900 RUB}')
perm.row('СК (син.крис) {0.5г/1300 RUB}')
perm.row('СК (син.крис) {1г/2200 RUB}')
perm.row('Гашиш EURO {1г/1100 RUB}')
perm.row('Гашиш EURO {2г/2000 RUB}')
perm.row('Гашиш EURO {5г/4000 RUB}')
perm.row('MEPHEDRONE крис {1г/2100 RUB}')
perm.row('Амфетамин HQ {2г/2400 RUB}')
perm.row('Шишки OG Kush {1г/1200 RUB}')
perm.row('Шишки OG Kush {2г/2200 RUB}')
perm.row('Шишки OG Kush {5г/4200 RUB}')
perm.row('РОСС {5г/3000 RUB}')
perm.row('Героин HQ {0.5г/1700 RUB}')


ufa_rayons = telebot.types.ReplyKeyboardMarkup(True)
ufa_rayons.row('🔹 Кировский')
ufa_rayons.row('🔹 Советский')
ufa_rayons.row('🔹 Ленинский')
ufa_rayons.row('🔹 Демский')
ufa_rayons.row('🔹 Орджоникидзевский')
ufa_rayons.row('🔹 Октябрьский')
ufa_rayons.row('🔹 Калининский')


ufa = telebot.types.ReplyKeyboardMarkup(True)
ufa.row('СК (син.крис) {0.3г/900 RUB}')
ufa.row('СК (син.крис) {0.5г/1300 RUB}')
ufa.row('СК (син.крис) {1г/2200 RUB}')
ufa.row('Гашиш EURO {1г/1100 RUB}')
ufa.row('Гашиш EURO {2г/2000 RUB}')
ufa.row('Гашиш EURO {5г/4000 RUB}')
ufa.row('MEPHEDRONE крис {1г/2100 RUB}')




krasnoyarsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
krasnoyarsk_rayons.row('🔹 Железнодорожный')
krasnoyarsk_rayons.row('🔹 Кировский')
krasnoyarsk_rayons.row('🔹 Ленинский')
krasnoyarsk_rayons.row('🔹 Октябрьский')
krasnoyarsk_rayons.row('🔹 Свердловский')
krasnoyarsk_rayons.row('🔹 Советский')
krasnoyarsk_rayons.row('🔹 Центральный')


krasnoyarsk = telebot.types.ReplyKeyboardMarkup(True)
krasnoyarsk.row('СК (син.крис) {0.3г/900 RUB}')
krasnoyarsk.row('СК (син.крис) {0.5г/1300 RUB}')
krasnoyarsk.row('СК (син.крис) {1г/2200 RUB}')
krasnoyarsk.row('Гашиш EURO {1г/1100 RUB}')
krasnoyarsk.row('Гашиш EURO {2г/2000 RUB}')
krasnoyarsk.row('MEPHEDRONE крис {1г/2100 RUB}')




toliyati_rayons = telebot.types.ReplyKeyboardMarkup(True)
toliyati_rayons.row('🔹 Автозаводский')
toliyati_rayons.row('🔹 Комсомольский')
toliyati_rayons.row('🔹 Центральный')


toliyati = telebot.types.ReplyKeyboardMarkup(True)
toliyati.row('СК (син.крис) {0.3г/900 RUB}')
toliyati.row('СК (син.крис) {0.5г/1300 RUB}')
toliyati.row('СК (син.крис) {1г/2200 RUB}')
toliyati.row('Гашиш EURO {1г/1100 RUB}')
toliyati.row('Гашиш EURO {2г/2000 RUB}')
toliyati.row('MEPHEDRONE крис {1г/2100 RUB}')
toliyati.row('РОСС {5г/3000 RUB}')
toliyati.row('Героин HQ {0.5г/1700 RUB}')


feodisiya_rayons = telebot.types.ReplyKeyboardMarkup(True)
feodisiya_rayons.row('🔹 Береговое')
feodisiya_rayons.row('🔹 Щебетовка')
feodisiya_rayons.row('🔹 Орджоникидзе')


feodisiya = telebot.types.ReplyKeyboardMarkup(True)
feodisiya.row('СК (син.крис) {0.3г/900 RUB}')
feodisiya.row('СК (син.крис) {0.5г/1300 RUB}')
feodisiya.row('СК (син.крис) {1г/2200 RUB}')
feodisiya.row('Гашиш EURO {1г/1100 RUB}')
feodisiya.row('Гашиш EURO {2г/2000 RUB}')
feodisiya.row('MEPHEDRONE крис {1г/2100 RUB}')
feodisiya.row('РОСС {5г/3000 RUB}')
feodisiya.row('Героин HQ {0.5г/1700 RUB}')


timashevsk = telebot.types.ReplyKeyboardMarkup(True)
timashevsk.row('СК (син.крис) {0.3г/900 RUB}')
timashevsk.row('СК (син.крис) {0.5г/1300 RUB}')
timashevsk.row('СК (син.крис) {1г/2200 RUB}')
timashevsk.row('Гашиш EURO {2г/2000 RUB}')
timashevsk.row('MEPHEDRONE крис {1г/2100 RUB}')
timashevsk.row('РОСС {5г/3000 RUB}')




kategor1 = telebot.types.ReplyKeyboardMarkup(True)
kategor1.row('СК (син.крис)','Гашиш')
kategor1.row('MEPHEDRONE крис','РОСС')




oplata = telebot.types.ReplyKeyboardMarkup(True)
oplata.row('Qiwi','Карта')
oplata.row('Bitcoin')

oplata_oplatil = telebot.types.ReplyKeyboardMarkup(True)
oplata_oplatil.row('Оплатил','Отменить')

admin = telebot.types.ReplyKeyboardMarkup(True)
admin.row('Изменить Карту','Изменить Qiwi')
admin.row('Количество пользователей')
admin.row('🔹 Главная')


yes_no = telebot.types.ReplyKeyboardMarkup(True)
yes_no.row('Да','Нет')