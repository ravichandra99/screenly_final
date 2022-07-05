import time

class Watcher:
    """ A simple class, set to watch its variable. """
    def __init__(self, value):
        self.variable = value
    

    def check_value(self, new):
        self.variable = new


class TimeLimit:
    def __init__(self,value = int(time.time())):
        self.variable = value

    def check_value(self):
        return int(time.time()) - self.variable
#check