import time


class HistoricalOperation:
    def __init__(self, product_type, operation_type, account_id, money, second_account_id=-1):
        self._product_type = product_type
        self._operation_type = operation_type
        self._account_id = account_id
        self._money = money
        self._date = time.asctime(time.localtime(time.time()))
        if operation_type == "transfer":
            self._second_account_id = second_account_id
            if second_account_id == -1:
                print("Invalid second account")

    def __str__(self):
        value = "Product type: " + self._product_type
        value += ", Operation type: " + self._operation_type
        value += ", AccountID: " + str(self._account_id)
        value += ", Money: " + str(self._money)
        value += ", date: " + self._date
        if self._operation_type == "transfer":
            if self._money > 0:
                value += ", SenderID: "
            else:
                value += ", ReceiverID: "
            value += self._second_account_id

        return value

    def get_product_type(self):
        return self._product_type

    def get_operation_type(self):
        return self._operation_type

    def get_account_id(self):
        return self._account_id

    def get_money(self):
        return self._money

    def get_date(self):
        return self._date

    def get_second_account_id(self):
        return self._second_account_id
