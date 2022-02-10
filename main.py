#!/usr/bin/env python3
#
# Usage: .py
#

from bank_account.account import Account, CurrentAccount, DepositAccount, InvestmentAccount, AmountError, BalanceError
import fintech.accounts as accounts

acc1 = Account('567891', 'jane dole', 104, 'savings')
acc2 = Account('567892', 'John dole', 105, 'deposit')
acc3 = Account('567893', 'james dole', 106, 'investment')

# from main import acc1, acc2, acc3

acc4 = CurrentAccount(account_number='912379',
                    account_holder='sally jones',
                    opening_balance=117,
                    overdraft_limit = 50)

acc5 = CurrentAccount(account_number='891237',
                    account_holder='jon jones',
                    opening_balance=115,
                    overdraft_limit = 1500)

acc6 = CurrentAccount(account_number='789123',
                    account_holder='jon smith',
                    opening_balance=106,
                    overdraft_limit = 1000)

# from main import acc4, acc5, acc6

acc7 = DepositAccount(account_number='891234',
                    account_holder='jony smith',
                    opening_balance=109,
                    interest_rate = 1.05)
        
acc8 = DepositAccount(account_number='912372',
                    account_holder='jon ellis',
                    opening_balance=120,
                    interest_rate = 1.06)
    
acc9 = DepositAccount(account_number='123729',
                    account_holder='jony ellis',
                    opening_balance=132,
                    interest_rate = 1.07)

# from main import acc7, acc8, acc9

acc10 = InvestmentAccount(account_number='891234',
                    account_holder='jony smith',
                    opening_balance=109,
                    risk_level='high')
        
acc11 = InvestmentAccount(account_number='912372',
                    account_holder='jon ellis',
                    opening_balance=120,
                    risk_level='medium')
    
acc12 = InvestmentAccount(account_number='123729',
                    account_holder='jony ellis',
                    opening_balance=132,
                    risk_level='low')

# from main import acc10, acc11, acc12
          
acc13 = accounts.CurrentAccount(account_number='912379',
                    account_holder='sally jones',
                    opening_balance=117,
                    overdraft_limit = 50)

acc14 = accounts.CurrentAccount(account_number='891237',
                    account_holder='jon jones',
                    opening_balance=115,
                    overdraft_limit = 1500)

acc15 = accounts.CurrentAccount(account_number='789123',
                    account_holder='jon smith',
                    opening_balance=106,
                    overdraft_limit = 1000)

# from main import acc13, acc14, acc15

try:
    acc1 = Account('567891', 'jane dole', 104, 'savings')
    acc1.deposit(amount= -10)
except AmountError as e:
    print(e)

try:
    acc1 = Account('567891', 'jane dole', 104, 'savings')
    acc1.withdraw(amount= -10)
except AmountError as e:
    print(e)

try:
    acc4 = CurrentAccount(account_number='912379',
                    account_holder='sally jones',
                    opening_balance=117,
                    overdraft_limit = -50)
    print('Balance:', acc4.get_balance)
    acc4.withdraw(1000)
    print('Balance:', acc4.get_balance)
except BalanceError as e:
    print('Exception Handling!')
    print(e)

acc1 = accounts.CurrentAccount('123123', 'John smith', 10.05, -100.0)
acc2 = accounts.DepositAccount('345123', 'John saul', 23.55, 0.5)
acc3 = accounts.InvestmentAccount('567123', 'Phoebe jones', 12.45, 'high')

print(acc1)
print(acc2)
print(acc3)

# acc1.deposit(200.45)
# acc1.withdraw(12.33)
# print('balance:', acc1.get_balance)

print('Number of Account instances created:', accounts.Account.instance_count)

try:
    print('balance:', acc1.get_balance)
    acc1.deposit(500)
    print('balance:', acc1.get_balance)
except accounts.BalanceError as e:
    print('Handling Exception')
    print(e)    


# with accounts.CurrentAccount('123123', 'John smith', 10.05, -100.0) as acc:
#     acc.deposit(200.45)
#     acc.withdraw(12.33)
#     print('balance:', acc.get_balance)

print('acc1.branch:', acc1.branch)




