from bank import Bank

newBank = Bank()

myClient = newBank.makeClient(1)
myAccount = newBank.makeAccount(myClient.getId(), 4)

myAccount.deposit_money(100)
myAccount.withdraw(120)
