import commands
import unittest


class TestCommands(unittest.TestCase):
    def test_create_list(self):
        self.assertEqual('Test_List', commands.create_list('Test_List'))


if __name__ == '__main__':
    unittest.main()
