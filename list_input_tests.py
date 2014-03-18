from list_input import ListInput
import unittest


class ListInputTests(unittest.TestCase):
    def test_create(self):
        self.Mylist = ListInput('People')
        #self.assertEqual(('new list People was created.'), ListInput.create('People'))
        self.assertEqual([], self.Mylist.create('name_of_list'))


if __name__ == '__main__':
    unittest.main()