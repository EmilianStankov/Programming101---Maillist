from user import User
from list import List


def create_list(name):
    mailing_list = List(name)
    file = open(mailing_list.name, 'w')
    file.close()
    return mailing_list.name


#def add(identifier):
#   file = open(lists[identifier], 'w')
#    name = input('name >>>')
#    file.write(name)
