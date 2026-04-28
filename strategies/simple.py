class SimpleStrategy(BaseStrategy): def __init__(self, price=10): self.price = price def choose_price(self, state): return self.price
