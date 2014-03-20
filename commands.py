from user import User
from list import List


index = 1
#users_index = 1
lists = []

def create_list(name):
    global index
    global lists
    mailing_list = List(name)
    file = open(mailing_list.name, 'w')
    file.close()
    file = open('mailing_lists.txt', 'a')
    file.write('[' + str(index) + '] ' + mailing_list.name + '\n')
    file.close()
    lists.append(mailing_list.name)
    index += 1
    return mailing_list.name


def add(identifier):
    file = open(lists[identifier - 1], 'a')
    print(lists)
    name = input('name >>>')
    file.write('[' + users_index + '] ' + name + ' - ')
    email = input('email >>>')
    file.write(email + '\n')
    file.close()


def main():
    add(1)


if __name__ == '__main__':
    main()
