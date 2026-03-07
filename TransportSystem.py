# Project Rules 
# 1. All decisions must be documented. 
# 2. Code without explanation will receive low marks. 
# 3. Plagiarism or AI-generated answers without understanding will be penalized. (Meaning, you can use AI but you must have a proper understanding of what you are doing)
# Challenge Description
# You are to design a system for a financial institution that manages multiple account types and a public transport card. 
# Part B: Transport Card System - A single card works on buses, trains, and ferries. - Each transport type has different fare rules. - Discounts apply differently depending on transport.
# Deliverables
# 1. Class design (what your code contains and how you came about it). 
# 2. Explanation of how each OOP pillar is used. 
# 3. Final Python implementation. 
# 4. A written reflection explaining key design decisions.


from abc import ABC, abstractmethod
 
class TransportCard(ABC):
    def __init__(self, balance):
        self._balance = balance  # Encapsulation
 
    def top_up(self, amount):
        if amount > 0:
            self._balance += amount
            print("New card balance:", self._balance)
        else:
            print("Invalid top-up amount")
 
    @abstractmethod
    def calculate_fare(self):
        pass
 
    def pay_fare(self):
        fare = self.calculate_fare()
        if fare > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= fare
            print("Fare paid:", fare)
            print("Remaining balance:", self._balance)
 
 
class Bus(TransportCard):
    def calculate_fare(self):
        fare = 1000
        discount = fare * 0.1  # 10% discount
        return fare - discount
 
 
class Train(TransportCard):  
    def calculate_fare(self):
        distance_fare = 200
        discount = distance_fare * 0.15  # 15% discount
        return distance_fare - discount
 
 
class Ferry(TransportCard):
    def calculate_fare(self):
        fare = 300  # premium transport
        return fare  # no discount
 
 
card1 = Bus(500)
card1.pay_fare()
 
card2 = Train(500)
card2.pay_fare()
 
card3 = Ferry(500)
card3.pay_fare()