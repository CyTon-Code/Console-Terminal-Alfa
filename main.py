# Код программы, а не модуля:
if __name__ != "__main__": # выход если внутри.
    exit()


# Проверить есть ли файл:
def check_file(address_file = "libs/modul.txt"):
    try:
        f = open(address_file, 'r') # если ошибка, то: файла нет или
        # его нельзя читать.
        return True # ответ: файл есть.
    except:
        print("Module not defined. modul:", address_file)
        return False # ответ: файла нет.
    finally:
        try:
            f.close() # обьязательно нужно закрыть файл, если не
            # закрыли.
        except:
            pass
