from bank_account import BankAccount
from bank_account_component import BankAccountComponent
from debit_bank_account import DebitBankAccount
from investment import Investment
from credit import Credit
from history import History
from cashLimitVisitor import CashLimitVisitor
from Operations.deposit import Deposit
from Operations.withdraw import Withdraw
from Operations.invest import Invest
from Operations.borrow import Borrow
from Operations.between_account_transfer import BetweenAccountTransfer


class Bank:
    def __init__(self, bank_id):
        self.bank_id = bank_id
        self.products = []
        self.raports = []
        self.operations = []
        self.clients = []
        self._historical_products = []

    def set_kir(self, kir):
        self.kir = kir

    def makeClient(self, id):
        self.clients.append(id)

    def getClients(self):
        return self.clients

    def getProducts(self):
        return self.products

    def getRaports(self):
        return self.raports

    def getHistory(self):
        return self.history

    def deposit(self, account_to, amount):
        operation = Deposit(account_to, amount)
        account_to.doOperation(operation)

    def withdraw(self, account_from, amount):
        operation = Withdraw(account_from, amount)
        account_from.doOperation(operation)

    def invest(self, account_from, amount):
        operation = Invest(account_from, amount)
        account_from.doOperation(operation)

    def borrow(self, account_to, amount):
        operation = Borrow(account_to, amount)
        account_to.doOperation(operation)

    def accountTransfer(self, account_from, account_to, amount):
        operation = BetweenAccountTransfer(account_from, account_to, amount)
        account_from.doOperation(operation)

    def makeAccount(self, userId, productId):
        account = BankAccount(self.bank_id, userId, productId)
        self.products.append(account)
        return account

    def makeDebitAccount(self, userId, productId):
        account = BankAccount(self.bank_id, userId, productId)
        debit_account = DebitBankAccount(account)
        self.products.append(debit_account)
        return debit_account

    def makeInvestment(self, date, amount, account, interest, userId, productId):
        if amount <= 0:
            raise ValueError("Investment value must be greater than zero!")
        investment = Investment(date, amount, account, interest, userId, productId)
        self.products.append(investment)
        self.invest(account, amount)
        return investment

    def makeCredit(self, money, account, end_date, userId, productId, number_of_installment):
        if money <= 0:
            raise ValueError("Credit value must be greater than zero!")
        credit = Credit(money, account, end_date, userId, productId, number_of_installment)
        self.products.append(credit)
        self.borrow(account, money)
        return credit

    def getUserProducts(self, userId):
        userProducts = []
        for product in self.products:
            if product.getOwner() == userId:
                userProducts.append(product)

        return userProducts

    def getUserAccounts(self, userId):
        userProducts = []
        for product in self.products:
            if product.getOwner() == userId and isinstance(product, BankAccountComponent):
                userProducts.append(product)

        return userProducts

    def getUserInvestments(self, userId):
        userProducts = []
        for product in self.products:
            if product.getOwner() == userId and type(product) == Investment:
                userProducts.append(product)

        return userProducts

    def getUserCredits(self, userId):
        userProducts = []
        for product in self.products:
            if product.getOwner() == userId and type(product) == Credit:
                userProducts.append(product)

        return userProducts

    def getUserProduct(self, userId, productId):
        for product in self.products:
            if product.getOwner() == userId and product.getId() == productId:
                return product

    def transfer(self, accountFrom, accountTo, amount):

        if accountFrom.get_bank_id() != accountTo.get_bank_id():
            print("Przelew miedzy bankowy")
            if accountFrom.get_account_balance() < amount:
                return False
            result = self.kir.make_transfer(accountTo.get_bank_id(), amount, accountTo.getId())
            if result == False:
                return result

            accountFrom.withdraw(amount, True)
            accountTo.deposit(amount, True)
            h_from = History("Outgoing transfer to " + str(accountTo.getId()) + ", value: "+str(amount), accountFrom.getId())
            h_to = History("Incoming transfer from " + str(accountFrom.getId()) + ", value: " + str(amount), accountTo.getId())
            accountFrom.getHistory().append(h_from)
            accountTo.getHistory().append(h_to)
            return True

        elif accountFrom.withdraw(amount, True):
            accountTo.deposit(amount, True)
            h_from = History("Outgoing transfer to " + str(accountTo.getId()) + ", value: "+str(amount), accountFrom.getId())
            h_to = History("Incoming transfer from " + str(accountFrom.getId()) + ", value: " + str(amount), accountTo.getId())
            accountFrom.getHistory().append(h_from)
            accountTo.getHistory().append(h_to)
            return True
        return False

    def outgoing_transfer(self, accountTo, amount):
        # todo: dopisać historie
        product = self.getProductById(accountTo)
        if product == False:
            return False
        product.deposit(amount, True)
        return True

    def getProductById(self, productId):
        for product in self.products:
            if product.getId() == productId:
                return product
        return False

    def closeProduct(self, id):
        product = self.getProductById(id)
        product.closeProduct()
        self.products.remove(product)
        self._historical_products.append(product)

    def getBankHistory(self):
        history = []
        for product in self.products:
            product_history = product.getHistory()
            for historical_operation in product_history:
                history.append(historical_operation)
        for product in self._historical_products:
            product_history = product.getHistory()
            for historical_operation in product_history:
                history.append(historical_operation)

        # source: https://stackoverflow.com/questions/5055812/sort-python-list-of-objects-by-date
        history.sort(key=lambda r: r.get_date())
        return history

    def doReport(self, report: CashLimitVisitor):
        result = []
        for product in self.products:
            result.append(product.accept(report))

        return result


