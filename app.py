import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Torta di Compleanno!", page_icon="🎂", layout="centered")

st.title("Buon Compleanno!")
st.subheader("Ecco la tua torta digitale interattiva!")

name = st.text_input("Scrivi il tuo nome o quello del festeggiato:", "Amico Speciale")
candles = st.slider("Numero di candeline", 1, 10, 5)
color = st.color_picker("Scegli il colore della glassa", "#ff66cc")

fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

ax.fill_between([2, 8], 2, 4, color=color)

for i in range(candles):
    x = 2.5 + i * (5.5 / (candles - 1))
    ax.plot([x, x], [4, 5], color="orange", linewidth=3)
    ax.plot(x, 5.1, marker="*", color="yellow", markersize=10)

ax.text(5, 1, f"Auguri, {name}!", fontsize=12, ha='center', color="purple")

st.pyplot(fig)

if st.button("Soffia le candeline!"):
    st.balloons()
    st.success(f"Tutte le candeline sono spente! Tanti auguri, {name}!")
