import random
from random import randint
import telebot
from telebot import types

from read import a, b, c  # чтение из файлов

raz4 = len(a)
raz7 = len(b)

# хранение данных пользователя и статистики его ответов по 4 задаиню
d = {-1: [0, 0, 0, 0,
          0]}  # 0-выбор слова 1-предыдущее слово 2-флаг выбора задания 3-флаг удаления статистики 4-флаг обработки даблклика

# данные об ошибках в ударениях (4 номер)
mis4 = {-1: [[], 0, 0]}  # 0-массив ошибок 1-число верных ответов 2-число всех ответов

# данные об ошибках в лексических нормах (7 номер)
mis7 = {-1: [[], 0, 0]}  # 0-массив ошибок 1-число верных ответов 2-число всех ответов
z = 0
bot = telebot.TeleBot("YOUR_TOKEN")  # сюда нужно вписать ваш токен


# вывод всех команд бота
@bot.message_handler(commands=['help', 'помощь'])
def ask_(message):
    bot.send_message(message.chat.id, "Список команд бота: \n" +
                     "/start - начало работы бота \n" +
                     "/clas - вывести классификацию важных ударений \n" +
                     "/mistakes - вывести cписок ваших ошибок \n" +
                     "/stat - вывести статистику (число верных ответов, процент верных) \n" +
                     "/deletestat4 - удалить статистику ответов и ошибок в 4 задании \n" +
                     "/deletestat7 - удалить статистику ответов и ошибок в 7 задании \n" +
                     "/number4 - выбрать 4 задание ЕГЭ задание для выполнения (нажать только после /start) \n" +
                     "/number7 - выбрать 7 задание ЕГЭ задание для выполнения (нажать только после /start) \n" +
                     "/help - вывести cписок команд бота \n")


# вывод классификацию ударений
@bot.message_handler(commands=['clas', 'классификация'])
def clas(message):
    bot.send_message(message.chat.id, '\n'.join(c))


# вывод статистики правильных/всех ответов
@bot.message_handler(commands=['stat', 'statistics', 'статистика'])
def stat(message):
    if (not message.chat.id in d):
        bot.send_message(message.chat.id,
                         "Вы еще не отвечали, используйте /start для начала работы или посмотрите список всех команд в /help")
        return

    if (mis4[message.chat.id][2]):
        p = mis4[message.chat.id][1]  # количество верных ответов
        o = mis4[message.chat.id][2]  # количество всех ответов
        bot.send_message(message.chat.id,
                         "Количество верных ответов в 4 задании: " + str(p) +
                         "\nКоличество всех ответов: " + str(o) +
                         "\nПроцент верных: " + str(100 * p / o) + " %\n")
    else:
        bot.send_message(message.chat.id, "Вы еще не отвечали на задание с ударениями\n")

    if (mis7[message.chat.id][2]):
        p = mis7[message.chat.id][1]  # количество верных ответов
        o = mis7[message.chat.id][2]  # количество всех ответов
        bot.send_message(message.chat.id,
                         "Количество верных ответов в 7 задании : " + str(p) +
                         "\nКоличество всех ответов: " + str(o) +
                         "\nПроцент верных: " + str(100 * p / o) + " %\n")
    else:
        bot.send_message(message.chat.id, "Вы еще не отвечали на задание с лексическими нормами\n")


# вывод слов, в которых ошибался пользователь
@bot.message_handler(commands=['mistakes', 'mist', 'ошибки'])
def mistake(message):
    if (not message.chat.id in d):
        bot.send_message(message.chat.id,
                         "Вы еще не отвечали, используйте /start для начала работы или посмотрите список всех команд в /help")
        return

    if (len(mis4[message.chat.id][0])):
        bot.send_message(message.chat.id,
                         "В этих ударениях вы допускали ошибки:\n" + '\n'.join(mis4[message.chat.id][0]))
    if (len(mis7[message.chat.id][0])):
        bot.send_message(message.chat.id,
                         "В этих словах вы допускали ошибки:\n" + '\n'.join(mis7[message.chat.id][0]))
    if (len(mis4[message.chat.id][0]) + len(mis7[message.chat.id][0]) == 0):
        bot.send_message(message.chat.id, "Вы еще не ошибались")


# удаление статистики 4 задания
@bot.message_handler(commands=['deletestat4'])
def deletestat_4(message):
    if (message.chat.id in d and mis4[message.chat.id][2]):
        bot.send_message(message.chat.id,
                         "Вы действительно хотите удалить свою статистику? Напишите ДА, чтобы подтвердить выбор.")
        d[message.chat.id][3] = 4
    else:
        bot.send_message(message.chat.id,
                         "Вы еще не отвечали, используйте  /start для начала работы или посмотрите список всех команд в  /help")


# удаление статистики 7 задания
@bot.message_handler(commands=['deletestat7'])
def deletestat_7(message):
    if (message.chat.id in d and mis7[message.chat.id][2]):
        bot.send_message(message.chat.id,
                         "Вы действительно хотите удалить свою статистику? Напишите ДА, чтобы подтвердить выбор.")
        d[message.chat.id][3] = 7
    else:
        bot.send_message(message.chat.id,
                         "Вы еще не отвечали, используйте  /start для начала работы или посмотрите список всех команд в  /help")


# начало работы бота
@bot.message_handler(commands=['start', 'старт'])
def start(message):
    if (not message.chat.id in d):
        d[message.chat.id] = [0, 0, 0, 0, 0]
        mis4[message.chat.id] = [[], 0, 0]
        mis7[message.chat.id] = [[], 0, 0]
    bot.send_message(message.chat.id, "Для повторения 4 задания (ударения) нажмите /number4. \n" +
                     "Для повторения 7 задания (лексические нормы: веера-вееры) нажмите /number7.",
                     reply_markup=types.ReplyKeyboardRemove())


# начало работы с 4 заданием
@bot.message_handler(commands=['number4', 'номер4', '4', 'ударения', 'ударение', 'четыре'])
def number4(message):
    if (not message.chat.id in d):
        bot.send_message(message.chat.id,
                         "Для начала работы напишите /start или /help, чтобы посмотреть на все команды бота")
        return
    d[message.chat.id][2] = 4
    keyboard = buttons_4(message.chat.id)
    bot.send_message(message.chat.id, " Выберите из 2 варинтов", reply_markup=keyboard)


# начало работы с 7 заданием
@bot.message_handler(commands=['number7', 'номер7', '7', '7номер', 'семь'])
def number7(message):
    if (not message.chat.id in d):
        bot.send_message(message.chat.id,
                         "Для начала работы напишите /start или /help, чтобы посмотреть на все команды бота")
        return
    d[message.chat.id][2] = 7
    keyboard = buttons_7(message.chat.id)
    bot.send_message(message.chat.id, "Выберите из 2 варинтов", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def ask(message):
    if (d[message.chat.id][4]):  # обработка даблклика
        return
    d[message.chat.id][4] = 1
    if (not message.chat.id in d):  # обработка текста перед нажатым /start
        bot.send_message(message.chat.id,
                         "Для начала работы напишите /start или /help, чтобы посмотреть на все команды бота")
        return

    # подтверждение удаления статистики
    if (message.text == "ДА"):
        if (d[message.chat.id][3] == 4):
            mis4[message.chat.id][0].clear()
            mis4[message.chat.id][1] = 0
            mis4[message.chat.id][2] = 0
        else:
            mis7[message.chat.id][0].clear()
            mis7[message.chat.id][1] = 0
            mis7[message.chat.id][2] = 0
        bot.send_message(message.chat.id, "Ваша статистика удалена")
        return
    d[message.chat.id][3] = 0

    s = message.text
    x = d[message.chat.id][0]

    if (d[message.chat.id][2] == 4):  # если выбрано 4 задание
        if (s == a[x][0]):  # если ответ верен
            keyboard = buttons_4(message.chat.id)
            bot.send_message(message.chat.id, a[x][0] + " -  ВЕРНО! ✅", reply_markup=keyboard)
            mis4[message.chat.id][1] += 1  # увеличываем число верных ответов
            mis4[message.chat.id][2] += 1  # увеличываем число всех ответов
        elif (s == a[x][1]):  # если ответ неверен
            mistakes_4(x, message.chat.id)
            keyboard = buttons_4(message.chat.id)
            bot.send_message(message.chat.id, a[x][1] + " - НЕВЕРНО! ❌", reply_markup=keyboard)
            mis4[message.chat.id][2] += 1  # увеличываем число всех ответов
    else:  # если выбрано 7 задание
        if (s == b[x][0]):  # если ответ верен
            keyboard = buttons_7(message.chat.id)
            bot.send_message(message.chat.id, b[x][0] + " -  ВЕРНО! ✅", reply_markup=keyboard)
            mis7[message.chat.id][1] += 1  # увеличываем число верных ответов
            mis7[message.chat.id][2] += 1  # увеличываем число всех ответов
        elif (s == b[x][1]):  # если ответ неверен
            keyboard = buttons_7(message.chat.id)
            mistakes_7(x, message.chat.id)
            bot.send_message(message.chat.id, b[x][1] + " - НЕВЕРНО! ❌", reply_markup=keyboard)
            mis7[message.chat.id][2] += 1  # увеличываем число всех ответов
    d[message.chat.id][4] = 0


# добавление слова, в котором ошибся пользователь, в массив mis4
def mistakes_4(x, id):
    if (not a[x][0] in mis4[id][0]):
        mis4[id][0].append(a[x][0])


# добавление слова, в котором ошибся пользователь, в массив mis7
def mistakes_7(x, id):
    if (not b[x][0] in mis7[id][0]):
        mis7[id][0].append(b[x][0])


#  клавиатуры с перемешыванием слов и рандомом из 2 вариантов
def buttons_4(id):
    d[id][1] = d[id][0]
    m = randint(0, 1)
    k = randint(0, raz4 - 1)
    r = d[id][1]
    if (r == k):
        k = (k + 1) % raz4
    d[id][0] = k
    keyboard = types.ReplyKeyboardMarkup(True)
    key_1 = types.KeyboardButton(text=a[k][m])
    key_2 = types.KeyboardButton(text=a[k][(m + 1) % 2])
    keyboard.add(key_1, key_2)
    return keyboard


def buttons_7(id):
    d[id][1] = d[id][0]
    m = randint(0, 1)
    k = randint(0, raz7 - 1)
    r = d[id][1]
    if (r == k):
        k = (k + 1) % raz7
    d[id][0] = k
    keyboard = types.ReplyKeyboardMarkup(True)
    key_1 = types.KeyboardButton(text=b[k][m])
    key_2 = types.KeyboardButton(text=b[k][(m + 1) % 2])
    keyboard.add(key_1, key_2)
    return keyboard


bot.polling()
