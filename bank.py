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

    def getAccounts(self):
        return self.products

    def makeAccount(self, userId, productId):
        account = BankAccount(userId, productId)
        self.products.append(account)
        return account