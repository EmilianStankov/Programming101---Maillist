from list_input import ListInput
import unittest


class ListInputTests(unittest.TestCase):
    def setUp(self):
        self.Mylist = ListInput('People')
        self.Mylist.create('first')
    def test_create(self):
        self.assertEqual([], self.Mylist.create('name_of_list'))
    def test_create_when_name_is_taken(self):
        self.assertEqual(None, self.Mylist.create('first'))


if __name__ == '__main__':
    unittest.main()