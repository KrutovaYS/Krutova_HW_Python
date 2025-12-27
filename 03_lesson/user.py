class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printFirst_name(self):
        print(self.first_name)

    def printLast_name(self):
        print(self.last_name)

    def printFull_name(self):
        print(self.first_name +' ' + self.last_name)