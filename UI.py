import time

def main():
    while True:
        val = input("Please input a username: ")
        val2 = input("Please input a password: ")

        var = open("username.txt", 'w')
        var.write(val)
        var.close()
        time.sleep(2)

        var = open("password.txt", 'w')
        var.write(val2)
        var.close()
        time.sleep(2)

if __name__ == '__main__':
    main()