class Output():
    def __init__(self):
        self.__help_prompt = "Here is a full list of commands:\n* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier\n* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>\n* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.\n* create <list_name> - Creates a new empty list, with the given name.\n* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.\n* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.\n* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.\n* exit - this will quit the program\n"
        self.file = open("lists_names.txt", 'r')
        self.lists = self.file.readlines()
        print(self.lists)
        self.file.close()
        self.file = open("lists_names.txt", 'r')
        self.content = self.file.read()
        print(self.content)
        self.file.close()

    def help(self):
        return self.__help_prompt

    def show_lists(self):

        return self.content

    def show_list(self, index):
        self.index = index
        filename = self.lists[index][4:].replace(' ', '_').lower() + '.txt'
        print (filename)
        file = open(filename, 'r')
        list_contents = file.read()
        file.close()
        return list_contents
