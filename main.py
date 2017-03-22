from bank import Bank

newBank = Bank()

MY_ID = 3
ACCTUAL_ACCOUNT_ID = 5

myClient = newBank.makeClient(MY_ID)
myAccount = newBank.makeAccount(myClient.getId(), ACCTUAL_ACCOUNT_ID)

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