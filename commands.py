from user import User
from list import List
import os
import json


def create_list(list_name):
    global lists
    lists = []
    file = open('mailing_lists.txt', 'r')
    content = file.readlines()
    file.close()
    for line in content:
        lists.append(line.split('] ')[1].strip())

    mailing_list = List(list_name)
    if mailing_list.name not in lists:
        print(mailing_list.name)
        file = open(mailing_list.name, 'w')
        file.close()
        if len(content) >= 1:
            index = int(content.pop().split()[0].strip('[]')) + 1
        else:
            index = 1
        file.close()
        file = open('mailing_lists.txt', 'a')
        file.write('[' + str(index) + '] ' + mailing_list.name + '\n')
        file.close()
        lists.append(mailing_list.name)
        return mailing_list.name
    else:
        print("A list with the name {} exists.".format(mailing_list.name))


def add(identifier):
    users_index = 1
    file = open(lists[identifier - 1], 'r')
    content = file.readlines()
    if len(content) >= 1:
        users_index = int(content.pop().split()[0].strip('[]')) + 1
    else:
        users_index = 1
    file.close()
    file = open(lists[identifier - 1], 'a')
    name = input('name >>>')
    file.write('[' + str(users_index) + '] ' + name + ' - ')
    email = input('email >>>')
    file.write(email + '\n')
    file.close()

lists = ['first', 'second'] # a test list, needs to be implemented for the program to work

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


def mail_is_in_file(mail, filename):
    file = open(filename, 'r')
    contents = file.read()
    contents = contents.split(' ')
    file.close()
    for line in contents:
        if mail in line:
                return True
    return False

def search_email(mail):
    email_list = []
    for item in lists:
        if mail_is_in_file(mail, item):
            email_list.append(item)
    if email_list != []:
        print (mail + ' was foind in:')
        for item in email_list:
            print (item)
    else:
        print(mail + ' is not present in the current maillists')


def remove_subscriber(list_identifier, name_identifier):
    name_of_file = lists[list_identifier - 1]
    file = open(name_of_file, 'r')
    content = file.read().split('\n')
    file.close()
    for i in range(len(content) - 1):
        exists = False
        if content[i].startswith('[' + str(name_identifier)):
            del content[i]
            print('Subscriber with identifider {} was removed from {}'.format(name_identifier, name_of_file))
            exists = True
            break
    if exists == False:
        print('Subscriber with identifider {} does not exist in list {}'.format(name_identifier, name_of_file))
    file = open(name_of_file, 'w')
    file.write('\n'.join(content))
    file.close()


def delete(list_identifier):
    print('Are you sure you want to delete {}'.format(lists[list_identifier - 1]))
    answer = input('(Y\\N) >')
    file = open('mailing_lists.txt', 'r')
    content = file.readlines()
    file.close()
    for i in range(len(content) - 1):
        exists = False
        if content[i].startswith('[' + str(list_identifier)):
            del content[i]
            exists = True
            break
    file = open('mailing_lists.txt', 'w')
    file.write(''.join(content))
    file.close()
    if exists == False:
        print('There is no list with identifier {}'.format(list_identifier))
    if answer == 'Y' and exists:
        os.remove(lists[list_identifier - 1])
    else:
        print('You crazy bastard. Stop playing with fire!')


def export(identifier):
    file = open(lists[identifier - 1], 'r')
    content = file.readlines()
    print(content)
    file.close()
    file = open(lists[identifier - 1] + '.json', 'w')
    file.write('[\n')
    for line in content:
        file.write('\t{\n\t\t\"name\" : \"' + line.split()[1] + '\",\n' +
                   '\t\t\"email\" : \"' + line.split()[3] + '\"\n\t},\n')
    file.write(']')
    file.close()


def import_json(filename):
    file = open(filename, 'r')
    content = file.read()
    for char in ' \t\",][{}':
        content = content.replace(char, '')
    content = content.split('\n\n')
    content = content[1:len(content) - 1]
    file.close()
    print(content)
    create_list(filename[:-5].replace('_', ' '))
    file = open(filename[:-5].replace('_', ' '), 'w')
    for i in range(len(content)):
        file.write('[' + str(i + 1) + '] ' +
            content[i].replace('\n', ' ').split()[0][5:] + ' - ' +
            content[i].replace('\n', ' ').split()[1][6:] + '\n')
    file.close()


def main():
    import_json('Fools_and_Fools.json')


if __name__ == '__main__':
    main()
