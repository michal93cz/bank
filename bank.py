from bank_account import BankAccount
from client import Client

class Bank:
    def __init__(self):
        self.products = []
        self.history = []
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

    def getUserProducts(self, userId):
        userProducts = []
        for product in self.products:
            if product.getOwner() == userId:
                userProducts.append(product)

        return userProducts

    def getUserAccounts(self, userId):
        userProducts = []
        for product in self.products:
            if product.getOwner() == userId and product.getType() == 'account':
                userProducts.append(product)

        return userProducts

    def getUserProduct(self, userId, id):
        for product in self.products:
            if product.getOwner() == userId and product.getId() == id:
                return product
