import random

class MarketEngine:
    def __init__(self, intercept, slope):
        self.round = 0
        self.intercept = intercept
        self.slope = slope

    def demand(self, price):
        return max(self.intercept - self.slope * price, 0)

    def shock(self, magnitude):
        shock = random.uniform(-magnitude, magnitude)
        self.intercept *= 1 + shock
        self.slope *= 1 - shock

    def step(self, price, shock_prob, magnitude):
        self.round += 1

        shock_occurred = False

        if random.random() < shock_prob:
            self.shock(magnitude)
            shock_occurred = True

        quantity = self.demand(price)
        revenue = price * quantity

        return revenue, quantity, shock_occurred