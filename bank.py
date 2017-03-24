from bank_account import BankAccount
from investment import Investment
from credit import Credit
from client import Client
from history import History

class Bank:
    def __init__(self):
        self.products = []
        self.history = History()
        self.raports = []
        self.operations = []
        self.clients = []

    def makeClient(self, id):
        client = Client(id)
        self.clients.append(client)
        return client

    def getClients(self):
        return self.clients

    def getProducts(self):
        return self.products

    def getRaports(self):
        return self.raports

    def getHistory(self):
        return self.history

    def makeAccount(self, userId, productId):
        account = BankAccount(userId, productId)
        self.products.append(account)
        return account

    def makeInvestment(self, date, amount, interest, userId, productId):
        investment = Investment(date, amount, interest, userId, productId)
        self.products.append(investment)
        return investment

    def makeCredit(self, money, account, end_date, userId, productId):
        credit = Credit(money, account, end_date, userId, productId)
        self.products.append(credit)
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
            if product.getOwner() == userId and type(product) == BankAccount:
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
        if accountFrom.withdraw(amount):
            accountTo.deposit_money(amount)
            return True
        return False
