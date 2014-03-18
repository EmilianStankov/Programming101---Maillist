class ListInput():
    def __init__(self, list_name):
        new_list = []
        self.list_name = list_name
        self.new_list = new_list
        self.all_lists = []

    def create(self, name):
        self.list_name = name
        if self.list_name in self.all_lists:
            print ('A list with name ' + self.list_name + ' already exists!') # if name of list is taken
        else:
            print ('new list ' + self.list_name + ' was created.') # prints message if create is successful
            self.all_lists.append(self.list_name)
            print (self.all_lists)
            return self.new_list

    def add(self):
        pass

