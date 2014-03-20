from user import User
from list import List

list_of_lists = ['first', 'second'] # a test list, needs to be implemented for the program to work

def welcome_massage():
	print('Hello Stranger! This is a cutting-edge, console-based mail-list!\nType help, to see a list of commands.')
#prints describtion of each commands
def help():
	print ("Here is a full list of commands:\n* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier\n* show_list <unique_list_identifier>- Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>\n* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.\n* update_subscriber <unique_list_identifier> <unique_name_identifier> - updates the information for the given subscriber in the given list\n* remove_subscriber <unique_list_identifier> <unique_name_identifier> - Removes the given subscriber from the given list\n* create <list_name> - Creates a new empty list, with the given name.\n* update <unique_list_identifier>  <new_list_name> - Updates the given list with a new name.\n* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.\n* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.\n* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.\n* exit - this will quit the program")

def show_lists(): #displays all lists
	list_counter = 1
	for item in list_of_lists: #a list of all lists that have been created
		print('[' + str(list_counter) + '] ' + item)
		list_counter = list_counter + 1

def show_list(identifier): #displays the content of a list
	member_counter = 1
	name_of_file = list_of_lists[identifier - 1] + '.txt'
	file = open(name_of_file, 'r')
	content = file.read()
	content = content.split('\n')
	for item in content:
		print('[' + str(member_counter) + '] ' + item)
		member_counter = member_counter + 1
	file.close()










