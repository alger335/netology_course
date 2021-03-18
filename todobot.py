# ДЗ 
# 1 Выводить ошибку при добавлении задачи, в которой меньше 3х символов.
# 2 Печатать задачи на несколько дат: принимать в команде print не одну дату, а произвольное количество.
# 3 При добавлении задачи учитывать отдельным параметром ее категорию. При выводе печатать категории задач со знаком @: Помыть посуду @Домашние дела.


# * Выводить ошибку, если команда введе на некорректно, например /print без даты или /todo без даты и/или задачи



from random import choice

import telebot

token = '1442000602:AAFZIVvq9POyh1ZPu3DxeG1IMh-AtAe3UNI'

bot = telebot.TeleBot(token)

RANDOM_TASK = ['Выучить Python', 'Поработать', 'Покормить ребенка', 'Потупить', 'Убраться', 'Сходить в магазин']

todos = dict()


HELP = '''Доступные команды:
    * /help - напечатать справку
    * /todo date task - добавить задачу в список, пример: /todo 4-02 Сходить в магазин
    * /print date date ... - напечатать все задачи из списка, пример: /print 4-02 завтра послезавтра
    * /random - добавить случайную задачу на заданую дату'''

def add_todo(date, task, category):             # функция "add_todo", принимает параметры date, task
  if todos.get(date) is not None:     # если в словаре todos есть дата
    todos[date].append(task)          # добавляем в словать todos на введенную дату введенную задачу
  else:                               # если в словаре нет такой даты                          
    todos[date] = [task]              # добавляем в словарь дату и задачу

#bot.send_message(message.chat.id, HELP)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, HELP)

#команда начинается с /
@bot.message_handler(commands=['help']) # Обработчик, для всех команд help выполнить функцию
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['random'])
def random_task(message):
    task = choice(RANDOM_TASK)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f"Задача {task} добавлена на сегодня")

@bot.message_handler(commands=['print'])
def print_tasks(message):
    """
    /print date date
    """
    # message text содержит в себе команду /print date date date date ... ... ...
    date = message.text.split()
    date = date[1:] # ['сегодня', 'завтра']
    #print(date)
    for d in date:
        d = d.lower()
        if d in todos:
            tasks = todos[d]
            text = d
            for task in tasks:
                text = text + f'\n[ ]{task}'
            bot.send_message(message.chat.id, text)
        else:
            text = f'На дату {date} задач нет'

@bot.message_handler(commands=['todo'])
def todo(message):
    """
    /todo date task
    """
    command = message.text.split(maxsplit=2)
    date = command[1]
    date = date.lower()
    task = command[2]
    if len(task) >= 3:
        add_todo(date, task)
        bot.send_message(message.chat.id, f'Задача {task} добавлена на {date}!')
    else:
        bot.send_message(message.chat.id, f'Ошибка! Задача {task} меньше 3-х символов!')
    

bot.polling(none_stop=True)