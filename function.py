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



