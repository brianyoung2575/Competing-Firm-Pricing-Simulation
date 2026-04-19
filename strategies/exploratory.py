import random
from .base import BaseStrategy

class EpsilonGreedyStrategy(BaseStrategy):
    def __init__(self, epsilon=0.1):
        self.prices = list(range(1, 101))

        self.q_values = {p: 0.0 for p in self.prices}
        self.counts = {p: 0 for p in self.prices}

        self.epsilon = epsilon
        self.last_price = None

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)
        
        if self.last_price is not None:
            p = self.last_price
            self.counts[p] += 1
            n = self.counts[p]
            self.q_values[p] += (last_profit - self.q_values[p]) / n

        if random.random() < self.epsilon:
            price = random.choice(self.prices)  # explore
        else:
            price = max(self.q_values, key=self.q_values.get)  # exploit

        self.last_price = price
        return price
