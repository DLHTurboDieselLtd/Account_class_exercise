#!/usr/bin/env python3
#
# Usage: .py
#

import re
from functools import wraps
from timeit import default_timer

def timer(func):
        @wraps(func)
        def method_wrapper(self, amount):
            print(f"Calling {func} on {amount}")
            start = default_timer()
            func(self, amount)
            end = default_timer()
            print(f"Returned from {func} it took {start - end} seconds")
              
        return method_wrapper

class AmountError(Exception):
    """Valid amounts must be greater than zero."""

    def __init__(self, account, msg) -> None:
        self.account = account
        self.msg     = msg

    def __str__(self) -> str:
        return f"AmountError(Cannot deposit/withdraw negative amounts) {self.account} {self.msg})"

class BalanceError(Exception):
    """Withdrawals should not exceed overdraft limit."""

    def __init__(self, account, msg) -> None:
        self.account = account
        self.msg     = msg

    def __str__(self) -> str:
        return f"BalanceError({self.account} {self.msg})"

class Account:

    """A class to represent a bank account."""

    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1

    @staticmethod
    def static_function():
        print('Static method')

    TYPES = ('current', 'savings', 'deposit', 'investment')

    def __init__(self,
                account_number, 
                account_holder, 
                opening_balance, 
                account_type) -> None:

        if not isinstance(account_number, str):
            raise TypeError(f"Invalid account number. Account number must of type string.")

        if not account_number.isdigit():
            raise ValueError(f"Invalid account number. Account number must contain only digits.")

        if len(account_number) != 6:
            raise ValueError(f"Invalid account number. Account number must only be of length 6.")

        resObj = re.search("^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)", account_holder)
        if not resObj: 
            raise ValueError(f"Invalid account name. Account name must be first name followed by last name.")

        if opening_balance < 0:
            raise ValueError(f"Opening balance must be positive!")

        if account_type not in self.TYPES:
            raise ValueError(f"Invalid account type. Account must be one of the following: {self.TYPES}")
                
        Account.increment_instance_count()
        self.account_number   = account_number
        self.account_holder   = account_holder
        self._opening_balance = opening_balance
        self.account_type     = account_type

    def __str__(self) -> str:
        return f"Account[{self.account_number}] - {self.account_holder}, {self.account_type} account = {self._opening_balance}"

    def __repr__(self) -> str:
        return f"Account('{self.account_number}', '{self.account_holder}', {self._opening_balance}, '{self.account_type}')"

    @timer
    def deposit(self, amount: int) -> None:
        if isinstance(amount, int) & (amount > 0):
            self._opening_balance += amount
        else:
            raise AmountError(self, "Cannot deposit negative amounts")
    @timer
    def withdraw(self, amount: int) -> None:
        if isinstance(amount, int) & (amount > 0):
            self._opening_balance -= amount
        else:
            raise AmountError(self, "Cannot withdraw negative amounts")

    @property  
    def get_balance(self):
        return self._opening_balance

    @get_balance.setter
    def get_balance(self, value):
        if isinstance(value, int) & (value > 0):
            self._opening_balance = value

class CurrentAccount(Account):

    """A subclass to represent a current account"""

    def __init__(self, account_number, account_holder, opening_balance, overdraft_limit) -> None:
        super().__init__(account_number, account_holder, opening_balance, 'current')
        self.overdraft_limit = overdraft_limit

    def __str__(self) -> str:
        return f"CurrentAccount[{self.account_number}] - {self.account_holder}, account = {self._opening_balance}, overdraft limit = {self.overdraft_limit}"

    def __repr__(self) -> str:
        return f"CurrentAccount('{self.account_number}', '{self.account_holder}', {self._opening_balance}, {self.overdraft_limit})"

    @timer
    def deposit(self, amount: int) -> None:
        if isinstance(amount, int) & (amount > 0):
            self._opening_balance += amount
        else:
            raise AmountError(self, "Cannot deposit negative amounts")

    @timer
    def withdraw(self, amount: int) -> None:
        if self._opening_balance - amount < self.overdraft_limit:
            raise BalanceError(self, "Cannot excced your overdraft limit!")
        else:
            if isinstance(amount, int) & (amount > 0):
                self._opening_balance -= amount
            else:
                raise AmountError(self, "Cannot withdraw negative amounts")

class DepositAccount(Account):

    """A subclass to represent a deposit account"""

    def __init__(self, account_number, account_holder, opening_balance, interest_rate) -> None:
        super().__init__(account_number, account_holder, opening_balance, 'deposit')
        self.interest_rate = interest_rate

    def __str__(self) -> str:
        return f"DepositAccount[{self.account_number}] - {self.account_holder}, account = {self._opening_balance}, interest rate = {self.interest_rate}"

    def __repr__(self) -> str:
        return f"DepositAccount('{self.account_number}', '{self.account_holder}', {self._opening_balance}, {self.interest_rate})"
        
    def interest(self):
        return self._opening_balance * self.interest_rate

class InvestmentAccount(Account):

    """A subclass to represent an investment account"""

    RISK_TYPES = ('low', 'medium', 'high')

    def __init__(self, account_number, account_holder, opening_balance, risk_level) -> None:
        super().__init__(account_number, account_holder, opening_balance, 'investment')
        self.risk_level = risk_level

        if risk_level not in self.RISK_TYPES:
            raise ValueError(f"Invalid risk type. Account must be one of the following: {self.RISK_TYPES}")

    def __str__(self) -> str:
        return f"InvestmentAccount[{self.account_number}] - {self.account_holder}, account = {self._opening_balance}, risk level = {self.risk_level}"

    def __repr__(self) -> str:
        return f"InvestmentAccount('{self.account_number}', '{self.account_holder}', {self._opening_balance}, {self.risk_level})"


      





    
    




    
