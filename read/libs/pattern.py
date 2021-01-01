# Модуль запускается только импортируясь.
if __name__ == "__main__": # выход если не внутри программы.
    exit()


# Пустая основная функция:
def main_m(args): # Запускаемая часть модуля:
  # your code goes here
  pass


# Пустая аварийная функция:
def error_m(args): # если main_m дала сбой, запускаем ее:
  # your code goes here
  pass


 # Функция для вывода слов-команд которые ожидаються в args:
def info_m(): # функция также может выводить описание этих команд.
  print("""command:
  -my_command_1   -my_command_2""")
  pass


def help_m():
  print("""Hi I'm a module template.
I'm here to show you what the module should look like.
Creator Timofey Boskor""")
  pass


"""
текущее время: 02.01.21 01:21
текущая версия терминала: 0
"""
