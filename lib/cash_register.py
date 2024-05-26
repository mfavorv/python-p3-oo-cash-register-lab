#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.items_bought = []

    def add_item(self,title, price, quantity=1):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.total += price * quantity
        for a in range(quantity):
            self.items.append(title)
            self.items_bought.append({"title": title, "quantity": quantity , "price": price})
        
    def apply_discount(self): 
        if self.discount > 0:
            new_total_decimal= 1 - (self.discount / 100)  
            self.total *=new_total_decimal 
            self.total = int(self.total)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
              if self.items_bought:
                  last_transaction = self.items_bought.pop()
                  last_total = last_transaction["quantity"] * last_transaction["price"]
                  self.total -= last_total
            
    pass
