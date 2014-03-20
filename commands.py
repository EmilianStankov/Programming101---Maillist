from user import User
from list import List


def create_list(name):
    global lists
    lists = []
    print(lists)
    file = open('mailing_lists.txt', 'r')
    content = file.readlines()
    file.close
    for line in content:
        print(line)
        lists.append(''.join(c for c in line if c not in '1234567890\n[] '))

    mailing_list = List(name)
    if mailing_list.name not in lists:
        file = open(mailing_list.name, 'w')
        file.close()
        file = open('mailing_lists.txt', 'r')
        index = len(file.readlines()) + 1
        file.close()
        file = open('mailing_lists.txt', 'a')
        file.write('[' + str(index) + '] ' + mailing_list.name + '\n')
        file.close()
        lists.append(mailing_list.name)
        index += 1
        return mailing_list.name
    else:
        print("A list with the name {} exists.".format(mailing_list.name))


def add(identifier):
    file = open(lists[identifier - 1], 'r')
    users_index = len(file.readlines())
    file.close()
    file = open(lists[identifier - 1], 'a')
    name = input('name >>>')
    file.write('[' + str(users_index + 1) + '] ' + name + ' - ')
    email = input('email >>>')
    file.write(email + '\n')
    file.close()


def welcome_massage():
    print('Hello Stranger! This is a cutting-edge, console-based mail-list!\nType help, to see a list of commands.')
#prints describtion of each commands

def help():
    print ("Here is a full list of commands:\n* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier\n* show_list <unique_list_identifier>- Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>\n* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.\n* update_subscriber <unique_list_identifier> <unique_name_identifier> - updates the information for the given subscriber in the given list\n* remove_subscriber <unique_list_identifier> <unique_name_identifier> - Removes the given subscriber from the given list\n* create <list_name> - Creates a new empty list, with the given name.\n* update <unique_list_identifier>  <new_list_name> - Updates the given list with a new name.\n* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.\n* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.\n* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.\n* exit - this will quit the program")


def show_lists(): #displays all lists
    file = open('mailing_lists.txt', 'r')
    content = file.readlines()
    file.close()
    for line in content:
        print(line)


def show_list(identifier): #displays the content of a list
    name_of_file = lists[identifier - 1]
    file = open(name_of_file, 'r')
    content = file.read()
    content = content.split('\n')
    for item in content:
        print(item)
    file.close()


def main():
    create_list('Test_List')
    add(1)
    show_lists()
    show_list(1)


if __name__ == '__main__':
    main()
