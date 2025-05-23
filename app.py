import streamlit as st
import matplotlib.pyplot as plt

# 🎵 Musica di sottofondo
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

# Impostazioni pagina
st.set_page_config(page_title="Torta per la Mamma", page_icon="🌸", layout="centered")

# Titolo
st.markdown("""
    <div style="text-align:center">
        <h1 style="color:#d6336c;">🎂 Torta di Compleanno per la Mamma 🎂</h1>
        <h3 style="color:#6c757d;">Clicca per soffiare le candeline e ascoltare la musica 🎶</h3>
    </div>
""", unsafe_allow_html=True)

# ✨ Dati predefiniti (non modificabili)
name = "Mamma, ti voglio bene"
candles = st.slider("Numero di candeline", 1, 10, 5)
color_top = st.color_picker("Colore glassa in cima", "#ffb3c6")
color_mid = st.color_picker("Colore glassa centrale", "#ff8fab")
color_bottom = st.color_picker("Colore glassa base", "#fb6f92")

# Disegno torta
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 15)
ax.axis("off")

# Tre piani
ax.fill_between([2, 8], 2, 4, color=color_bottom)
ax.fill_between([3, 7], 4, 6, color=color_mid)
ax.fill_between([4, 6], 6, 7.5, color=color_top)

# Candeline
for i in range(candles):
    x = 4.2 + i * (1.6 / max(1, candles - 1))
    ax.plot([x, x], [7.5, 8.5], color="orange", linewidth=3)
    ax.plot(x, 8.7, marker="*", color="yellow", markersize=10)

# Scritta
ax.text(5, 1, f"{name}", fontsize=14, ha='center', color="purple", weight='bold')

# Mostra torta
st.pyplot(fig)

# Bottone con musica
if st.button("💗 Soffia le candeline! 💗"):
    st.balloons()
    st.success(f"Tanti auguri, {name} 🎁")
    st.audio(audio_url)
