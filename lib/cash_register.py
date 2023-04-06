#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.last_transaction = 0
    self.items = []

  def add_item(self, title, price, quantity = 1):
    self.last_transaction = price * quantity
    self.total += self.last_transaction
    for groceries in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if (self.discount > 0):
      self.total = int(self.total * (100 - float(self.discount)) / 100)
      print(f"After the discount, the total comes to ${self.total}.")
      return self.total
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction

  # def apply_discount(self):
  #   if (self.discount > 0):
  #     self.total = self.total * (1 - self.discount / 100)
  #     print(f"After the discount, the total comes to ${self.total}.")
  #     return self.total
  #   else:
  #     print("There is no discount to apply.")

  # def void_last_transaction(self):
  #   self.total -= self.last_transaction
  
test = CashRegister(0)
print(test.apply_discount())