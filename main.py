from bank import Bank
import time

bank_id=1
newBank = Bank(bank_id)
t = 1

MY_ID = 3
ACCTUAL_ACCOUNT_ID = 5

MY_ID_2 = 5
ACCTUAL_ACCOUNT_ID_2 = 8


myClient = newBank.makeClient(MY_ID)
time.sleep(t)
myAccount = newBank.makeAccount(MY_ID, ACCTUAL_ACCOUNT_ID)

time.sleep(t)
myClient2 = newBank.makeClient(MY_ID_2)
myAccount2 = newBank.makeAccount(MY_ID_2, ACCTUAL_ACCOUNT_ID_2)

myAccount2.deposit(10)
time.sleep(t)
newBank.transfer(myAccount2, myAccount, 30)

time.sleep(t)
val = myAccount.withdraw(35)
time.sleep(t)
val = myAccount.withdraw(25)

time.sleep(t)
print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())
print(newBank.getUserAccounts(MY_ID)[0].getOwner())

# extend debit
val = newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).withdraw(70)
print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())
time.sleep(t)

val = newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).withdraw(70)
print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())
time.sleep(t)

# cut debit
print(newBank.getUserProduct(MY_ID, ACCTUAL_ACCOUNT_ID).current_account_balance())
time.sleep(t)

# print history
hist = newBank.getBankHistory()
#print(hist)
for h in hist:
    h.print()
