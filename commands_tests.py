import commands
import unittest


class TestCommands(unittest.TestCase):
    def test_create_list(self):
        self.assertEqual('Test_List', commands.create_list('Test_List'))
        self.assertEqual('Test_List 2', commands.create_list('Test_List 2'))

    #def test_add_user(self):
     #   self.assertEqual('Test_List', commands.create_list('Test_List'))
     #   self.assertEqual('Test_List 2', commands.create_list('Test_List 2'))
     #   self.assertEqual('[1] User - email@mail.com',commands.add(1))


if __name__ == '__main__':
    unittest.main()
