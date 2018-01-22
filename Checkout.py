class Checkout:

    class Discount:
        def __init__(self, numberItems, price):
            self.numberItems = numberItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addDiscount(self, item, numberOfItems, price):
        discount = self.Discount(numberOfItems, price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculateItemTotal(item, count)
        return total

    def calculateItemTotal(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.numberItems:
                total += self.calculateItemDiscountedTotal(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count

        return total

    def calculateItemDiscountedTotal(self, item, count, discount):
        total = 0
        nbrOfDiscounts = count / discount.numberItems
        total += nbrOfDiscounts * discount.price
        remaining = count % discount.numberItems
        total += remaining * self.prices[item]
        return total