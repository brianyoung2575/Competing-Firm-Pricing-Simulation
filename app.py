import streamlit as st
import matplotlib.pyplot as plt
from engine import MarketEngine
from simulation import Simulation
from strategies.simple import SimpleStrategy
from strategies.greedy import GreedyStrategy
from strategies.exploratory import ExploratoryStrategy

st.title("Pricing Simulation")

if "sim" not in st.session_state:
    engine = MarketEngine(100, 1)

    strategies = {
        "Simple": SimpleStrategy(10),
        "Greedy": GreedyStrategy(10),
        "Exploratory": ExploratoryStrategy(10)
    }

    st.session_state.sim = Simulation(engine, strategies)

sim = st.session_state.sim

shock_prob = st.sidebar.slider("Shock Probability", 0.0, 1.0, 0.1)
magnitude = st.sidebar.slider("Shock Magnitude", 0.0, 1.0, 0.1)

steps = st.sidebar.slider("Steps per run", 1, 50, 10)

if st.sidebar.button("Run Simulation"):
    for _ in range(steps):
        sim.step(shock_prob, magnitude)
        
fig, ax = plt.subplots(figsize=(6, 3))

for name, data in sim.history.items():
    ax.plot(data["profits"], label=name)

ax.set_title("Profit over time")
ax.legend()

st.pyplot(fig)

st.subheader("Cumulative Profit")

for name, total in sim.cumulative_profit.items():
    st.write(f"{name}: {total:.2f}")
