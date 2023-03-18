import ask

def write_data(user):
    """Записывает данные в базу данных"""
    with open("data.txt", "a", encoding="utf8" ) as file:
        file.write(user + "\n")

def read_data():
    """Считывет всю информацию в базе данных"""
    with open("data.txt", "r", encoding="utf8") as file:
        content = file.readlines()
        return content

def find_person(persons, name):
    """По имени или фамилии ищет человека в базе данных"""
    for person in persons:
        if name.lower() in person.lower():
            print(person)
    print("--------------------------")
    while True:
        request = ask.change_menu()
        if request == 1:
            print("Введите новые данные")
            person = ask.get_person()
            change_person(name, person)
            print("--------------------------")
            print("Данные обновленны")
            print(f"Добавлен: {person}")
            print("--------------------------")
        elif request == 2:
            delete_person(name)
            print("--------------------------")
            print("Пользователь удален")
            print("--------------------------")
        else:
            break

def delete_person(name):
    """Удаляет данные"""
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name.lower()  not in person.lower():
                file.write(person)

def change_person(name, new_name):
    """Изменяет данные"""
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name.lower()  not in person.lower():
                file.write(person)
            else:
                file.write(new_name + "\n")