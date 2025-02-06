#!/usr/bin/python3

# The Single-Responsibility Principle (SRP) is one of the SOLID principles in software development.

#################################################
# A class should have only one reason to change #
#################################################

# In simpler terms, a class or module should only be responsible for one thing or behavior. This principle ensures that each class is focused, cohesive, and easier to maintain or modify without affecting unrelated functionality

# A Class Violating SRP

class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def print_order(self):
        for item in self.items:
            print(f"{item['name']}: {item['quantity']} x {item['price']}")

    def save_to_database(self):
        print("Order saved to Database")

# Here, the Order class has multiple responsibilities:
# - Calculating the total price (calculate_total).
# - Printing the order (print_order).
# - Persisting the order (save_to_database).
# If any of these responsibilities change (e.g., a change in how orders are stored), the Order class will need to be modified, which violates SRP.

# Refactored Code Following SRP

class OrderSRP:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

class OrderPrinter:
    @staticmethod
    def print_order(self):
        for item in self.items:
            print(f"{item['name']}: {item['quantity']} x {item['price']}")

class OrderRepository:
    @staticmethod
    def save(order):
        print("Order saved to the database")

# Here’s how the refactored code adheres to SRP:
# - Order: Handles only the core order logic (e.g., calculate_total).
# - OrderPrinter: Responsible for printing the order.
# - OrderRepository: Handles order persistence (e.g., saving to the database).

items = [
    {"name": "Apple", "price": 1.0, "quantity": 5},
    {"name": "Banana", "price": 0.5, "quantity": 10},
]

print(items)

order = OrderSRP(items)
print("Total:", order.calculate_total())

OrderPrinter.print_order(order)
OrderRepository.save(order)

# Benefits of SRP

# - Better Maintainability: Changes in one responsibility don’t affect others.
# - Improved Testability: Each responsibility can be tested independently.
# - Clear Separation of Concerns: Code is easier to understand and modify.

# By applying SRP, your code will be more modular, extensible, and easier to debug.







