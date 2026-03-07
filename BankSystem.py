# Project Rules 
# 1. All decisions must be documented. 
# 2. Code without explanation will receive low marks. 
# 3. Plagiarism or AI-generated answers without understanding will be penalized. (Meaning, you can use AI but you must have a proper understanding of what you are doing)
# Challenge Description
# You are to design a system for a financial institution that manages multiple account types and a public transport card. Part A: Banking System - Accounts include Savings, Current, and Interest Accounts. - Some accounts allow overdraft, some do not. - Interest is calculated differently depending on account type
# Deliverables
# 1. Class design (what your code contains and how you came about it). 
# 2. Explanation of how each OOP pillar is used. 
# 3. Final Python implementation. 
# 4. A written reflection explaining key design decisions.


from abc import ABC, abstractmethod
 
 
class BankAccount(ABC):
    """
    This is the abstract base class for all bank accounts.
    It defines common behavior and enforces interest calculation.
    """
 
    def __init__(self, balance, name, number):
        # ENCAPSULATION: protected attributes
        self._balance = balance      # account balance (protected)
        self.name = name             # account holder name
        self._number = number        # account number (protected)
 
    def deposit(self, amount):
        """Adds money to the account balance"""
        if amount > 0:
            self._balance += amount
            print("Deposit successful. New balance:", self._balance)
        else:
            print("Invalid deposit amount")
 
    def withdraw(self, amount):
        """Withdraws money from the account if sufficient balance exists"""
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print("Withdrawal successful. New balance:", self._balance)
 
    def get_balance(self):
        """Displays the current account balance"""
        print("Current balance:", self._balance)
 
    @abstractmethod
    def apply_interest(self):
        """
        ABSTRACTION:
        Every account type must define how interest is applied.
        """
        pass
 
class SavingsAccount(BankAccount):
    """
    Savings account earns a basic interest.
    """
 
    def apply_interest(self):
        # POLYMORPHISM: specific implementation for savings account
        self._balance += self._balance * 0.01
        print("Savings interest applied. New balance:", self._balance)
 
 
class CurrentAccount(BankAccount):
    """
    Current account allows overdraft but earns no interest.
    """
 
    def withdraw(self, amount):
        # POLYMORPHISM: overridden withdraw method
        overdraft_limit = 1000
        if amount > (self._balance + overdraft_limit):
            print("Withdrawal exceeds overdraft limit")
        else:
            self._balance -= amount
            print("Withdrawal successful. New balance:", self._balance)
 
    def apply_interest(self):
        # POLYMORPHISM: different behavior from savings
        print("Current accounts do not earn interest")
 
 
class InterestAccount(SavingsAccount):
    """
    Interest account earns higher interest than savings account.
    """
 
    def apply_interest(self):
        # POLYMORPHISM: overridden interest calculation
        self._balance += self._balance * 0.05
        print("High interest applied. New balance:", self._balance)
 
 
# Savings Account
savings = SavingsAccount(50000, "Duaa", 4241235)
savings.apply_interest()
savings.get_balance()
 
# Current Account
current = CurrentAccount(5000, "Mercy", 55342)
current.withdraw(200)
current.withdraw(3000)
current.get_balance()
 
# Interest Account
interest = InterestAccount(500000, "Duaa", 46654)
interest.apply_interest()
interest.get_balance() 
