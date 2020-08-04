# telegram_bot
Телеграм бот для изучения повторения ударений для ЕГЭ (4 задание) и лексических норм для 7 задания (актуально на 2019-2020).  
Запуск происходит через main.py.
Для работы с ботом нужно написать токен телеграм бота взамен YOUR_TOKEN.
Нужно подключить pip install pyTelegramBotAPI для работы с телеграм API.
В файле clas.txt находится классификация ударений, в файле words1.txt находятся слова, которые спрашиваются в разделе 4 номера, в файле words2.txt для 7 номера, чтение этих файлов происходит в read.py.

В боте рализованы команды:
/start - начало работы бота (ей продублирована /старт),
/number4 - начало работы с 4 номером (ей продублированы /номер4 , /4 , /4номер , /четыре , /ударения , ударение),
/number7 - начало работы с 4 номером (ей продублированы /номер7 , /7 , /7номер , /семь),
/clas - вывести классификацию важных ударений  (ей продублирована /классификация),
/mistakes - вывести cписок ваших ошибок (ей продублированы /ошибки , /mist),
/stat - вывести статистику (число верных ответов, процент верных)  (ей продублированы /статистика , /statistics),
/deletestat4 - удалить статистику ответов и ошибок по 4 заданию, 
/deletestat7 - удалить статистику ответов и ошибок по 7 заданию, 
/help - вывести cписок команд бота (ей продублирована /помощь). 