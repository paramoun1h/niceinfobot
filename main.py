import telebot
from telebot import types
bot = telebot.TeleBot('1118328891:AAHCxHI0AQlnPLtVSGnlMFJzLSzX5lQ-bRU')
after_city = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
glav_knopka = types.KeyboardButton("🏡На главную🏡")
after_city.add(glav_knopka)
main_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
main_markup_1 = types.KeyboardButton('📞Контакты в телеграмм')
main_markup_2 = types.KeyboardButton('✍️ Отзывы')
main_markup_3 = types.KeyboardButton('🌐 Форумы')
main_markup_4 = types.KeyboardButton('❗️Лучший чат с рулетками!')
main_markup_5 = types.KeyboardButton('🍭 Наш ассортимент')
main_markup.add(main_markup_1, main_markup_2, main_markup_3, main_markup_4, main_markup_5)
city_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
city_1 = types.KeyboardButton('Харьков')
city_2 = types.KeyboardButton('Киев')
city_3 = types.KeyboardButton('Одесса')
city_markup.add(city_1, city_2, city_3)
forum_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
forum_markup_1 = types.KeyboardButton('BigBro.biz')
forum_markup_2 = types.KeyboardButton('Legalizer')
forum_markup.add(forum_markup_1, forum_markup_2)
@bot.message_handler(content_types=['text'])
def send_text(message):
    global username
    username = message.chat.id
    global first_name
    first_name = message.chat.first_name
    if message.text.lower() == '/start':
        bot.send_message(907939709, 'Пользователь с юзерайди ' + str(username) + ' вызвал команду /start')
        bot.send_message(1118953092, str(username))
        bot.send_message(message.from_user.id, '*Добрый день ' + first_name + '!*\n*Вас приветствует инфобот N1ce Shop!*\n\n_Я бот с актуальными контактами и ассортиментом._\n*Тут вы найдёте всё что хотели!*',
                         reply_markup=main_markup, parse_mode="Markdown")
    if message.text.lower() == '🏡на главную🏡':
        bot.send_message(message.from_user.id, '*Добрый день ' + first_name + '!*\n*Вас приветствует инфобот N1ce Shop!*\n\n_Я бот с актуальными контактами и ассортиментом._\n*Тут вы найдёте всё что хотели!*',
                         reply_markup=main_markup, parse_mode="Markdown")
    if message.text.lower() == '📞контакты в телеграмм':
        bot.send_message(message.from_user.id, '*Круглосуточный сайт автопродаж:\nhttps://nicebro.top\nБот автопродаж в телеграмм:\n@newbroN1ce_bot\nГлавный босс:\n@n1ceShop\nСаппорт:\n@TonyScarface*', parse_mode="Markdown")
    if message.text.lower() == '✍️ отзывы':
        bot.send_message(message.from_user.id, '*Канал с отзывами о нашем магазине* 👇🏾\nhttps://t.me/joinchat/AAAAAFaMfWcVWtS0Af7pRw\n_Тут ты можешь увидеть фото нашего товара, а также ознакомиться с нашим сервисом , благодаря отзывам от довольных клиентов._', parse_mode="Markdown")
    if message.text.lower() == '❗️лучший чат с рулетками!':
        bot.send_message(message.from_user.id, '*Лучший чат во всём телеграмме!*\n\n_Постоянный актив даже ночью!\n\nРулетки на _*много-много* _призов!_\n*👇Будь с лучшими!👇*\nhttps://t.me/joinchat/MPlXFRcUxO5bG6w8meBvHA', parse_mode="Markdown")
    if message.text.lower() == '🍭 наш ассортимент':
        bot.send_message(message.from_user.id, 'Выберите нужный город:', reply_markup=city_markup)
        bot.register_next_step_handler(message, send_city)
    if message.text.lower() == '🌐 форумы':
        bot.send_message(message.from_user.id, '_Мы есть на многих_ *RC форумах*.\n_Выберите нужный форум из списка что бы получить ссылку на ветку:_',parse_mode="Markdown", reply_markup=forum_markup)
        bot.register_next_step_handler(message, send_forum)
def send_forum(message):
    global forum
    forum = message.text
    if forum == "BigBro.biz":
        bot.send_message(message.from_user.id, "Ссылка на ветку на бигбро:\nhttps://bigbro.biz/forums/nicebro-top-%D0%9A%D0%B8%D0%B5%D0%B2-%D0%A5%D0%B0%D1%80%D1%8C%D0%BA%D0%BE%D0%B2-bot-24-7-newbron1ce_bot.263/", reply_markup=after_city)
    elif forum == "Legalizer":
        bot.send_message(message.from_user.id, "Ссылка на ветку на легалайзере:\nhttps://m.legalizer.cc/forums/n1ceshop-%D0%A1%D0%B5%D1%80%D0%B2%D0%B8%D1%81-%D0%93%D0%BE%D1%82%D0%BE%D0%B2%D1%8B%D1%85-%D0%9A%D0%BB%D0%B0%D0%B4%D0%BE%D0%B2-%D0%BF%D0%BE-%D0%A5%D0%B0%D1%80%D1%8C%D0%BA%D0%BE%D0%B2%D1%83-%D0%9A%D0%B8%D0%B5%D0%B2%D1%83-%D0%B8-%D0%9E%D0%B4%D0%B5%D1%81%D1%81%D0%B5-%D0%90%D0%BC%D1%84-%D0%A8%D0%B8%D1%88-enzo-%D0%A2%D0%B0%D0%B1%D0%BB%D1%8B-%D0%9C%D0%B5%D1%84.2152/", reply_markup=after_city)
def send_city(message):
 global city
 city = message.text
 if city == 'Харьков':
     bot.send_message(message.from_user.id, '''*По Харькову доступно в кладах:* 
    _- 🌳Шишки в ассортименте 
    - 🐟Соль 
    -☄️Амфетамин 
    -✨Ешки Etherium 300mdma✨
    - 👽Space X 300mg MDMA👽
    - 🍯 Мёд для любителей сладкого. 
    - 🌞Мефедрон HQ_\n*В ХАРЬКОВЕ забиты даже дальние районы такие как ЗАЛЮТИНО чтобы вы далеко не бегали пешком!!! Все районы практически забомблены!!!!*''', reply_markup=after_city, parse_mode="Markdown")
 elif city == 'Одесса':
     bot.send_message(message.from_user.id, '''*По Одессе доступно в кладах :* 
    _- 🌳Шишки 
    ✨- EA7 300 mdma 
    ☄- Фен
     - 🧟‍♂️Соль
     -🤠Мефедрон HQ 
     -🍯 Мёд _''', reply_markup=after_city, parse_mode="Markdown")
 elif city == 'Киев':
     bot.send_message(message.from_user.id, '''*По Киеву доступно в кладах :*
    _-☄️Amphetamine HQ
     - 🌞Мефедрон HQ
    ✨- EA7 300 mdma_✨''', reply_markup=after_city, parse_mode="Markdown")

bot.polling()