from bank import Bank
from BankOperations import BankOperations

newBank = Bank()

MY_ID = 3
ACCTUAL_ACCOUNT_ID = 5

MY_ID_2 = 5
ACCTUAL_ACCOUNT_ID_2 = 8

myClient = newBank.makeClient(MY_ID)
myAccount = newBank.makeAccount(myClient.getId(), ACCTUAL_ACCOUNT_ID)

myClient2 = newBank.makeClient(MY_ID_2)
myAccount2 = newBank.makeAccount(myClient.getId(), ACCTUAL_ACCOUNT_ID_2)

myAccount2.deposit_money(10)
BankOperations.transfer(myAccount2, myAccount, 30)

newBank.history.add_log('account', 'deposit', myAccount.deposit_money(100), ACCTUAL_ACCOUNT_ID)

val = myAccount.withdraw(35)
if val is not None:
    newBank.history.add_log('account', 'withdraw', val, ACCTUAL_ACCOUNT_ID)

val = myAccount.withdraw(25)
if val is not None:
    newBank.history.add_log('account', 'withdraw', val, ACCTUAL_ACCOUNT_ID)

print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())
print(newBank.getUserAccounts(MY_ID)[0].getOwner())

# extend debit
val = newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).withdraw(70)
if val is not None:
    newBank.history.add_log('account', 'withdraw', val, ACCTUAL_ACCOUNT_ID)
print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())

val = newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).withdraw(70)
if val is not None:
    newBank.history.add_log('account', 'withdraw', val, ACCTUAL_ACCOUNT_ID)
print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())

# cut debit
newBank.history.add_log('account', 'deposit', myAccount.deposit_money(100), ACCTUAL_ACCOUNT_ID)
print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())

# print history
hist = newBank.history.get_all_history()
for element in hist:
    print(element)
