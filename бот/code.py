import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный для вашей методы.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# Обработчик для текстовых сообщений
@bot.message_handler(content_types=['text'])
def butms(message):
    if message.chat.type == 'private':  # Если сообщение отправлено в личном чате
        if message.text == '🎲 Рандомное число':  # Если текст сообщения - '🎲 Рандомное число'
            bot.send_message(message.chat.id, str(random.randint(0, 100)))  # Отправить случайное число от 0 до 100
        elif message.text == '😊 Как дела?':  # Если текст сообщения - '😊 Как дела?'

            # Создание интерактивной клавиатуры с кнопками "Хорошо" и "Не очень"
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)  # Добавление кнопок в клавиатуру

            # Отправка сообщения с клавиатурой
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id,
                             'Я не знаю что ответить 😢')  # Если текст не совпадает с предыдущими условиями, отправить сообщение


# Обработчик для встроенных кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:  # Если присутствует сообщение
            if call.data == 'good':  # Если пользователь выбрал кнопку 'Хорошо'
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')  # Отправить сообщение
            elif call.data == 'bad':  # Если пользователь выбрал кнопку 'Не очень'
                bot.send_message(call.message.chat.id,
                                 'Не расстраивайся, ты делаешь лучшую лабу в мире!')  # Отправить сообщение

                # Удаление встроенных кнопок
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="😊 Как дела?",
                                      reply_markup=None)  # Редактирование сообщения, убирая клавиатуру

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)

