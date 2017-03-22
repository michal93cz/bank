from historical_operation import HistoricalOperation


class History:
    def __init__(self):
        self._logs = []

    def add_log(self, product_type, operation_type, money, account_id, second_account_id=-1):
        historical_info = HistoricalOperation(product_type, operation_type, account_id, money, second_account_id)
        self._logs.append(historical_info)

    def get_all_history(self):
        return self._logs

    def get_account_history(self, account_id):
        account_history = []
        for log in self._logs:
            if log.get_account_id() == account_id:
                account_history.append(log)
        return account_history

    def get_product_history(self, product_type):
        product_history = []
        for log in self._logs:
            if log.get_product_type() == product_type:
                product_history.append(log)
        return product_history
