from ex_18 import *

santander = Bank()

santander.new_customers('Gustavo', 21, 'Both')

c1 = santander.customers_['Gustavo']

print(c1.get_name)
print(c1.savings_account_.__dict__)
print(c1.checking_account_.__dict__)
print(santander.accounts_['Gustavo'][0].__dict__)
print(santander.accounts_['Gustavo'][1].__dict__)

c1_sav_acc = c1.savings_account_

c1_sav_acc.withdraw(100000, santander)

print(c1_sav_acc.balance_)

c1_chk_acc = c1.checking_account_

c1_chk_acc.withdraw(10010, santander)

print(c1_chk_acc.balance_)
print(c1_chk_acc.extra_limit_)