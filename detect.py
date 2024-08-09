import time

dictionary = {}

while True:
    time.sleep(3)

    var = open("username.txt", 'r')
    username = var.readline()
    var.close()

    var = open("password.txt", 'r')
    password = var.readline()
    var.close()
    time.sleep(2)

    if dictionary == {}:
        dictionary[username] = password

    try:
        if username in dictionary:
            var = open("status.txt", 'w')
            var.write('Username taken')
            var.close()

        if dictionary[username] == password:
            var = open("status.txt", 'w')
            var.write('Entry exists')
            var.close()

    except:
            dictionary[username] = password
            var = open("status.txt", 'w')
            var.write('New Entry')
            var.close()

    str1 = str(dictionary)
    var = open("database.txt", 'w')
    var.write(str1)
    var.close()         

    print(dictionary)
