# forward reference used for class Sale
# ProductSale.py
from __future__ import annotations
from typing import List

class Product:
    __lastSale: Sale = None
    __inventory: int = 0  # Attribute to keep track of the inventory

    def __init__(self, sale: Sale, initial_inventory: int = 0):
        self.__lastSale = sale
        self.__inventory = initial_inventory  # Initialize inventory with given quantity

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    def __getitem__(self, item):
        return self

    def update_inventory(self, quantity: int):
        if quantity > self.__inventory:
            raise ValueError("Not enough inventory to complete the sale.")
        self.__inventory -= quantity
        print(f"Inventory updated to {quantity}")

    # Method to get the current inventory
    @property
    def get_inventory(self) -> int:
        return self.__inventory


# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, product: List[Product], quantities: List[int]):
        Sale.__saleTimes += 1
        self.__product = product
        self.__saleNumber = Sale.__saleTimes

        # Check the length of products and quantities match
        if len(product) != len(quantities):
            raise ValueError("The number of products and quantities must match.")

        # Set last sale and decrease inventory for each product
        for index, product in enumerate(product):
            product.setLastSale(self)
            product.update_inventory(quantities[index])  # Decrease inventory

    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber



# Create Product instances with initial inventory
productOne = Product(sale=None, initial_inventory=10)
productTwo = Product(sale=None, initial_inventory=5)

# Create Sale instances and track inventory changes
saleOne = Sale([productOne, productTwo], [2, 3])  # Reduces inventory of productOne by 2 and productTwo by 3
saleTwo = Sale([productOne], [1])  # Reduces inventory of productOne by 1
saleThree = Sale([productTwo], [2])  # Reduces inventory of productTwo by 2

print(f"Product One - Last Sale Number: {productOne.getLastSale.getSaleNumber}, Inventory: {productOne.get_inventory}")
print(f"Product Two - Last Sale Number: {productTwo.getLastSale.getSaleNumber}, Inventory: {productTwo.get_inventory}")