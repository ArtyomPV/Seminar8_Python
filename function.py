def write_data(user):
    with open("data.txt", "a") as file:
        file.write(user + "\n")



def read_data():
    with open("data.txt", "r") as file:
        content = file.readlines()
        return content

def find_user(lst, str):
    for value in lst:
        if str in value:
            print(value)


        


