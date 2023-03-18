def choice():
   """Запрашивает какое действие хочет выполнить пользователь"""

   choice = int(input("Введите категорию\n1 - импорт данных\n2 - экспорт данных\n3 - выход из опроса\n"))
   return choice

def get_person():
    """Запрашивает у пользователя имя. фамилию и номер телефона"""

    name = input("Имя \t\t- ")
    last_name = input("Фамилия \t- ")
    phone_number = input("Номер телефона \t- ")
    return name + " " + last_name + " " + phone_number
   

def ask_person():
    """Запрашивает у пользователя имя или фамилию для поиска в базе данных"""
    
    return input("Введите имя или фамилия для поиска в базе данных: ")
    
    
def change_menu():
    choice = int(input("Введите категорию\n1 - изменить данные\n2 - удалить данные\n3 - выход\n"))
    return choice
