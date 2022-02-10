#!/usr/bin/env python3
#
# Usage: .py
#

from timeit import timeit
import unittest

from bank_account.account import timer
from bank_account.account import Account

class TestTimer(unittest.TestCase):
    def test_timer_decorator(self):
        @timer
        def to_be_decorated(self, amount):
            pass
        to_be_decorated(self, amount=10)

from bank_account.account import AmountError, BalanceError
import bank_account.account as acc

class AmountErrorTest(unittest.TestCase):
    def test_account_amount_error_deposit(self):
        with self.assertRaises(AmountError):
            acc.Account(account_number='123456',
                          account_holder='John Smith',
                          opening_balance=100,
                          account_type='deposit').deposit(amount = -1)

    def test_account_amount_error_withdraw(self):
        with self.assertRaises(AmountError):
            acc.Account(account_number='823456',
                          account_holder='John Smyth',
                          opening_balance=101,
                          account_type='savings').withdraw(amount = -1)

    def test_current_account_amount_error_deposit(self):
        with self.assertRaises(AmountError):
            acc.CurrentAccount(account_number='789123',
                            account_holder='jon smith',
                            opening_balance=106,
                            overdraft_limit = 1000).deposit(amount = -2)

    def test_current_account_amount_error_withdraw(self):
        with self.assertRaises(AmountError):
            acc.CurrentAccount(account_number='889123',
                            account_holder='juan smith',
                            opening_balance=108,
                            overdraft_limit = -1001).withdraw(amount = -3)

class BalanceErrorTest(unittest.TestCase):
    def test_current_account_balance_error(self):
        with self.assertRaises(BalanceError):
            acc.CurrentAccount(account_number='889123',
                            account_holder='juan smith',
                            opening_balance=100,
                            overdraft_limit = -100).withdraw(amount = 500)

from bank_account.account import Account
from bank_account.account import CurrentAccount
from bank_account.account import DepositAccount
from bank_account.account import InvestmentAccount

class AccountTest(unittest.TestCase):
    def test_account_has_account_number(self):
        account = Account(account_number='123456',
                          account_holder='John Smith',
                          opening_balance=100,
                          account_type='deposit')
        self.assertEqual(account.account_number, '123456')

    def test_account_has_account_holder(self):
        account = Account(account_number='234567',
                          account_holder='John Doe',
                          opening_balance=101,
                          account_type='investment')
        self.assertEqual(account.account_holder, 'John Doe')

    def test_account_has_opening_balance(self):
        account = Account(account_number='345678',
                          account_holder='Jane Smith',
                          opening_balance=102,
                          account_type='savings')
        self.assertEqual(account._opening_balance, 102)

    def test_account_has_account_type(self):
        account = Account(account_number='456789',
                          account_holder='bob dole',
                          opening_balance=103,
                          account_type='deposit')
        self.assertEqual(account.account_type, 'deposit')

    def test_account_has_string_representation(self):
        account = Account(account_number='567891',
                        account_holder='jane dole',
                        opening_balance=104,
                        account_type='savings')
        self.assertEqual(str(account), "Account[567891] - jane dole, savings account = 104")

    def test_account_has_technical_representation(self):
        account = Account(account_number='567891',
                        account_holder='jane dole',
                        opening_balance=104,
                        account_type='savings')
        self.assertEqual(repr(account), "Account('567891', 'jane dole', 104, 'savings')")

    def test_account_only_allows_for_account_number_in_string_format(self):
        with self.assertRaises(TypeError):
            Account(567891, 'jane dole', 104, 'savings')

    def test_account_only_allows_for_digits_in_account_number(self):
        with self.assertRaises(ValueError):
            Account('A67891', 'jane dole', 104, 'savings')

    def test_account_only_allows_for_account_number_to_be_of_len_6(self):
        with self.assertRaises(ValueError):
            Account('4678917', 'jane dole', 104, 'savings')

    def test_account_only_allows_for_name_in_correct_format(self):
        with self.assertRaises(ValueError):
            Account('467891', 'jane.dole@gmail.com', 104, 'savings')

    def test_account_only_allows_positive_opening_balance(self):
        with self.assertRaises(ValueError):
            Account('467891', 'sam dole', -102, 'investment')

    def test_account_has_three_account_types(self):
        self.assertEqual(
            Account.TYPES,
            ('current', 'savings', 'deposit', 'investment')
        )

    def test_account_only_allows_for_valid_type(self):
        with self.assertRaises(ValueError):
            Account('567891', 'jane dole', 104, 'practice')

    def test_account_deposit_instance_method(self):
        account = Account(account_number='567891',
                        account_holder='jane dole',
                        opening_balance=104,
                        account_type='savings')
        self.assertIsNone(account.deposit(amount=20))

    def test_account_withdraw_instance_method(self):
        account = Account(account_number='678912',
                        account_holder='james smith',
                        opening_balance=105,
                        account_type='investment')
        self.assertIsNone(account.withdraw(amount=30))

    def test_account_get_balance_instance_method(self):
        account = Account(account_number='789123',
                        account_holder='jon smith',
                        opening_balance=106,
                        account_type='deposit')
        self.assertEqual(account.get_balance, account._opening_balance)

    def test_account_increment_instance_count(cls):
        cls.assertIsNone(Account.increment_instance_count())

    def test_account_static_method(cls):
        cls.assertIsNone(Account.static_function())

class CurrentAccountTest(unittest.TestCase):
    def test_current_account_has_string_representation(self):
        current_account = CurrentAccount(account_number='789123',
                                        account_holder='jon smith',
                                        opening_balance=106,
                                        overdraft_limit = 1000)
        self.assertEqual(str(current_account), "CurrentAccount[789123] - jon smith, account = 106, overdraft limit = 1000")

    def test_current_account_has_technical_respresentation(self):
        current_account = CurrentAccount(account_number='891237',
                                        account_holder='jon jones',
                                        opening_balance=115,
                                        overdraft_limit = 1500)
        self.assertEqual(repr(current_account), "CurrentAccount('891237', 'jon jones', 115, 1500)")

    def test_current_account_withdraw_instance_method(self):
        current_account = CurrentAccount(account_number='123796',
                                        account_holder='sam jones',
                                        opening_balance=179,
                                        overdraft_limit = -100)
        
        self.assertIsNone(current_account.withdraw(100))
            
class DepositAccountTest(unittest.TestCase):
    def test_deposit_account_has_string_representation(self):
        deposit_account = DepositAccount(account_number='891234',
                                        account_holder='jony smith',
                                        opening_balance=109,
                                        interest_rate = 0.5)
        self.assertEqual(str(deposit_account), "DepositAccount[891234] - jony smith, account = 109, interest rate = 0.5")

    def test_deposit_account_has_technical_respresentation(self):
        deposit_account = DepositAccount(account_number='912372',
                                        account_holder='jon ellis',
                                        opening_balance=120,
                                        interest_rate = 0.6)
        self.assertEqual(repr(deposit_account), "DepositAccount('912372', 'jon ellis', 120, 0.6)")    

    def test_deposit_account_interest_method(self):
        deposit_account = DepositAccount(account_number='123729',
                                        account_holder='jony ellis',
                                        opening_balance=132,
                                        interest_rate = 0.7)
        self.assertEqual(deposit_account.interest(), deposit_account._opening_balance * deposit_account.interest_rate)

class InvestmentAccountTest(unittest.TestCase):
    def test_investment_account_has_string_representation(self):
        investment_account = InvestmentAccount(account_number='912347',
                                        account_holder='jonny jones',
                                        opening_balance=115,
                                        risk_level = 'high')
        self.assertEqual(str(investment_account), "InvestmentAccount[912347] - jonny jones, account = 115, risk level = high")

    def test_investment_account_has_technical_respresentation(self):
        investment_account = InvestmentAccount(account_number='123729',
                                        account_holder='jonny ellis',
                                        opening_balance=121,
                                        risk_level = 'low')
        self.assertEqual(repr(investment_account), "InvestmentAccount('123729', 'jonny ellis', 121, low)")

    def test_investment_account_has_risk_type(self):
        investment_account = InvestmentAccount(account_number='237298',
                                        account_holder='jim ellis',
                                        opening_balance=127,
                                        risk_level = 'high')
        self.assertEqual(investment_account.risk_level, 'high')

    def test_investment_account_has_three_risk_types(self):
        self.assertEqual(
            InvestmentAccount.RISK_TYPES,
            ('low', 'medium', 'high')
        )

    def test_investment_account_only_allows_for_valid_risk_type(self):
        with self.assertRaises(ValueError):
            InvestmentAccount('767891', 'jonathan dole', 94, 'super high')


    
              
            


    


    



    




    





    



        




