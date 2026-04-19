import random
import math
from .base import BaseStrategy

class AdaptiveExploratoryStrategy(BaseStrategy):
    def __init__(self):
        self.q_values = {}
        self.last_price = 10
        self.temperature = 5.0
        self.best_price = 10
        self.best_value = float("-inf")

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)
        
        if self.last_price not in self.q_values:
            self.q_values[self.last_price] = last_profit
        else:
            self.q_values[self.last_price] = (
                0.85 * self.q_values[self.last_price]
                + 0.15 * last_profit
            )

        if last_profit > self.best_value:
            self.best_value = last_profit
            self.best_price = self.last_price

        self.temperature *= 0.995

        if random.random() < 0.02:
            self.temperature = 5.0

        prices = list(self.q_values.keys())

        if len(prices) < 5 or random.random() < self.temperature / 10:
            price = random.uniform(1, 100)
        else:
            weights = []
            for p in prices:
                q = self.q_values[p]
                weights.append(math.exp(q / max(self.temperature, 0.1)))

            total = sum(weights)
            probs = [w / total for w in weights]

            price = random.choices(prices, weights=probs, k=1)[0]
            price += random.uniform(-3, 3)

        self.last_price = max(0.1, price)
        return self.last_price
