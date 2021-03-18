from random import choice

# ToDo list program
HELP = '''Доступные команды:
* help - напечатать справку
* todo - добавить задачу в список
* print - напечатать все задачи из списка
* exit - выход
* random - добавить случайную задачу на заданую дату'''

RANDOM_TASK = ['Написать письмо Гвидо', 'Выучить Python']
print(HELP)

# Инициализируем списки задач
#Список задач на дату 
#Дата -> [задачи]
tasks = dict() # tasks = {}

today = []
tomorrow = []
other = []

def add_todo(date, task):
  '''Эта функция добавляет в словарь задачуу task по ключу date'''
  # добавляем задачу в список date из словаря tasks(если дата уже есть в словаре)
  if date in tasks:
    tasks[date].append(task)
  # если даты в словаре нет, созаем дату в словаре и помещаем в список задачу
  else:
    tasks[date] = [task]
  print(f'Задача {task} добавлена на {date}')


# Флаг
stop = False
while not stop:
  # будет выполняться всегда пока не встретит break(предлагать ввести команду)
  command = input('Введите команду: ')
  # обрезать пробелы и привести к нижнему регистру
  command = command.strip().lower()

  # блок help
  if command == 'help':
    print(HELP)

  # блок add
  elif command == 'todo':
    #запрашиваем дату, задачу
    date = input('Введите дату: ')
    date = date.strip().lower()
    task = input('Введите задачу: ')
    add_todo(date, task)
  
  # блок print
  elif command == 'print':
    #запрос даты
    date = input('Введите дату: ')
    if date in tasks:
    #вывести задачи на дату, если датаесть
      print(f'{date}:')
      for t in tasks[date]:
        print(f'[ ] {t}')
    else:
      print('Нету ¯\_(ツ)_/¯')

  # блок exit
  elif command == 'exit':
    print('До встречи!')
    stop = True

  # блок random
  elif command == 'random':
    # запрашиваем дату, задачу
    date = input('Введите дату: ')
    date = date.strip().lower()
    add_todo(date, choice(RANDOM_TASK))
    


  # блок неизвестная команда 
  else:
    print('Неизвестная команда! Попробуйте еще раз')
    print(HELP)
