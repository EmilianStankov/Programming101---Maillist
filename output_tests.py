import unittest
import output


class TestOutput(unittest.TestCase):
    def setUp(self):
        self.out = output.Output()
        self.file = open("lists_names.txt", 'r')
        self.lists = self.file.read()
        self.file.close()
        self.list = open("list1.txt", 'r')
        self.list_contents = self.list.read()
        self.list.close()

    def test_help(self):
        self.assertEqual("Here is a full list of commands:\n* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier\n* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>\n* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.\n* create <list_name> - Creates a new empty list, with the given name.\n* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.\n* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.\n* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.\n* exit - this will quit the program\n", self.out.help())

    def test_show_lists(self):
        self.assertEqual("[1] Hack Bulgaria\n[2] HackFMI",
            self.out.show_lists())

    def test_show_list_contents(self):
        self.assertEqual("[1] Radoslav Georgeiv - radorado@hackbulgaria.com\n[2] Ivaylo Bachvaroff - ivo@hackbulgaria.com\n[3] Daniel Taskoff - dani@dani.com", self.out.show_list(2))

    def test_show_list_contents(self):
        self.assertEqual("[1] Radoslav Georgeiv - radorado@hackbulgaria.com\n[2] Ivaylo Bachvaroff - ivo@hackbulgaria.com", self.out.show_list(1))

if __name__ == '__main__':
    unittest.main()
