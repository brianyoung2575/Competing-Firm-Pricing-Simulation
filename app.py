import streamlit as st
from engine import MarketEngine

st.title("Market Simulation")

if "engine" not in st.session_state:
    st.session_state.engine = MarketEngine(100, 1)

engine = st.session_state.engine

price = st.slider("Price", 0.0, 100.0, 1.0)
shock_prob = st.slider("Shock Probability", 0.0, 1.0, 0.1)
magnitude = st.slider("Shock Magnitude", 0.0, 1.0, 0.1)

if st.button("Next Time Step"):
    revenue, quantity, shock = engine.step(price, shock_prob, magnitude)

    st.write(f"Round: {engine.round}")
    st.write(f"Quantity: {quantity:.2f}")
    st.write(f"Revenue: {revenue:.2f}")
    st.write(f"Intercept: {engine.intercept:.2f}")
    st.write(f"Slope: {engine.slope:.2f}")

    if shock:
        st.warning("Shock occurred!")