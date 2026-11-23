# Program to demonstrate encapsulation and abstraction

from abc import ABC, abstractmethod

# Abstraction
class Bank:
    @abstractmethod
    def interest(self):
        pass

# Encapsulation
class Account(Bank):
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def display_balance(self):
        print("Balance:", self.__balance)

    def interest(self):
        print("Interest rate is 5%")

# Creating object
a1 = Account(1000)

a1.display_balance()

a1.deposit(500)

a1.display_balance()

a1.interest()

OUTPUT
Balance: 1000
Balance: 1500
Interest rate is 5%
