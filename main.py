from bank import Bank

newBank = Bank()

MY_ID = 3
ACCTUAL_ACCOUNT_ID = 5

myClient = newBank.makeClient(MY_ID)
myAccount = newBank.makeAccount(myClient.getId(), ACCTUAL_ACCOUNT_ID)

myAccount.deposit_money(100)
myAccount.withdraw(35)

newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).withdraw(25)
print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())
print(newBank.getUserProducts(MY_ID, 'account')[0].getOwner())
