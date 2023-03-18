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
    simillar_person = list()
    for person in persons:
        if name.lower() in person.lower():
            simillar_person.append(person)
    for i in range(len(simillar_person)):
        print(f"{i + 1} {simillar_person[i]}")
    print("--------------------------")
    while True:
        request = ask.change_menu()
        if request == 1:
            if len(simillar_person) > 1:
                choice = int(input("Введите позицию, которую необходимо заменить - "))
            else:
                choice = 1
            print("Введите новые данные")
            new_person = ask.get_person()
            change_person(new_person, simillar_person[choice - 1])
            print("--------------------------")
            print("Данные обновленны")
            print(f"Добавлен: {new_person}")
            print("--------------------------")
        elif request == 2:
            if len(simillar_person) > 1:
                choice = int(input("Введите позицию, которую необходимо удалить - "))
            else:
                choice = 1
            delete_person(simillar_person[choice - 1])
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
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
    """Изменяет данные"""
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")