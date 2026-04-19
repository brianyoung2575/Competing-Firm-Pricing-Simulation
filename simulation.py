class Simulation:
    def __init__(self, engine, strategies):
        self.engine = engine
        self.strategies = strategies  # dict: name -> strategy

        self.history = {
            name: {"profits": [], "prices": []}
            for name in strategies
        }

        self.cumulative_profit = {
            name: 0 for name in strategies
        }

    def step(self, shock_prob=0.1, magnitude=0.1):
        results = {}
        prices = {}
        for name, strat in self.strategies.items():
            state = {
                "last_profit": self.history[name]["profits"][-1]
                if self.history[name]["profits"] else 0
            }
            prices[name] = strat.choose_price(state)

        for name, price in prices.items():
            outcome = self.engine.step(price, shock_prob, magnitude)

            profit = outcome["revenue"]

            self.cumulative_profit[name] += profit

            self.history[name]["profits"].append(profit)
            self.history[name]["prices"].append(price)

            results[name] = {
                "price": price,
                "profit": profit,
                "cumulative": self.cumulative_profit[name]
            }

        return results
