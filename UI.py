import time

def main():
    while True:
        val = input("Please input a username: ")
        val2 = input("Please input a password: ")

        var = open("username.txt", 'w')
        var.write(val)
        var.close()

        var = open("password.txt", 'w')
        var.write(val2)
        var.close()
        time.sleep(4)

        print('\n')
        var2 = open('status.txt', 'r')
        value = var2.readline()
        var2.close()

        print(f'Status: {value}')
        print('\n')

if __name__ == '__main__':
    main()