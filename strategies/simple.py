from strategies.base import BaseStrategy

class SimpleStrategy(BaseStrategy):
    def __init__(self, price=10):
        self.price = float(price)

    def choose_price(self, state):
        return self.price
