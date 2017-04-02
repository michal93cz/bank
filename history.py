import time


class History:
    def __init__(self, description, id):
        self._date = time.asctime(time.localtime(time.time()))
        self._description = description
        self._product_id = id

    def get_date(self):
        return self._date

    def get_description(self):
        return self._description

    def print(self):
        print(str(self._date)+", Product ID: "+str(self._product_id)+", "+self._description)
