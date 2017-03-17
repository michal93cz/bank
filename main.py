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
print(newBank.getUserAccounts(MY_ID)[0].getOwner())

# extend debit
newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).withdraw(70)
print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())
newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).withdraw(70)
print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())

# cut debit
myAccount.deposit_money(100)
print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())