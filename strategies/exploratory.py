import random
from .base import BaseStrategy

class FullRangeExploratoryStrategy(BaseStrategy):
    def __init__(self):
        self.prices = list(range(1, 101))
        self.index = 0

        self.q_values = {p: 0 for p in self.prices}
        self.counts = {p: 0 for p in self.prices}

        self.last_price = 10
        self.exploit = False
        self.lock = 0

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)

        if self.last_price is not None:
            p = self.last_price
            self.counts[p] += 1
            n = self.counts[p]
            self.q_values[p] += (last_profit - self.q_values[p]) / n

        if self.lock > 0:
            self.lock -= 1

            if last_profit < self.q_values[self.last_price] * 0.5:
                self.lock = 0

            return self.last_price

        if not self.exploit:
            price = self.prices[self.index]
            self.index = (self.index + 1) % len(self.prices)

            if self.index == 0:
                self.exploit = True
        else:
            best_price = max(self.q_values, key=self.q_values.get)
            price = best_price + random.randint(-2, 2)

            if random.random() < 0.05:
                self.exploit = False

        self.last_price = max(1, min(100, price))
        self.lock = 5

        return self.last_price
