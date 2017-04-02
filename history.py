import time


class History:
    def __init__(self, description):
        self._date = time.asctime(time.localtime(time.time()))
        self._description = description

    def get_date(self):
        return self._date

    def get_description(self):
        return self._description

    def print(self):
        print(str(self._date)+" "+self._description)
