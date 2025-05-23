import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Musica "Tanti Auguri" (strumentale royalty-free)
audio_url = "https://cdn.pixabay.com/audio/2022/10/07/audio_7e5f9c8b47.mp3"

# Configura pagina
st.set_page_config(page_title="Torta realistica per la Mamma", page_icon="🎂", layout="centered")

# Titolo
st.markdown("""
    <div style="text-align:center">
        <h1 style="color:#e63946;">🎂 Torta Speciale per la Mamma 🎂</h1>
        <h3 style="color:#555;">Con amore, musica e dolcezza 💕</h3>
    </div>
""", unsafe_allow_html=True)

# Dati predefiniti
name = "Mamma, ti voglio bene"
age = st.slider("Quanti anni compie?", 1, 45, 5)
color_bottom = st.color_picker("Colore base torta", "#ffb3c6")
color_middle = st.color_picker("Colore centro torta", "#ff8fab")
color_top = st.color_picker("Colore glassa superiore", "#fb6f92")

# Disegna torta realistica
fig, ax = plt.subplots(figsize=(5, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 15)
ax.axis("off")

# Disegna tre piani arrotondati
def draw_cake_layer(y_base, height, width, color):
    x = np.linspace(5 - width/2, 5 + width/2, 100)
    y_top = y_base + height
    ax.fill_between(x, y_base, y_top, color=color, edgecolor="black", linewidth=1.5)
    ellipse = plt.Circle((5, y_top), width/2, color=color, ec="black")
    ax.add_patch(ellipse)

draw_cake_layer(2, 2, 6, color_bottom)
draw_cake_layer(4, 2, 5, color_middle)
draw_cake_layer(6, 1.5, 3.5, color_top)

# Candeline
for i in range(age):
    if age > 1:
        x = 5 - 1.6 + i * (3.2 / (age - 1))
    else:
        x = 5
    ax.plot([x, x], [7.5, 8.5], color="orange", linewidth=2)
    ax.plot(x, 8.7, marker="*", color="yellow", markersize=8)

# Scritta sotto
ax.text(5, 1, name, fontsize=15, ha='center', color="darkmagenta", weight='bold')

# Mostra la torta
st.pyplot(fig)

# Bottone per soffiare candeline e musica
if st.button("🎶 Soffia le candeline 🎶"):
    st.balloons()
    st.success(f"Tanti auguri, {name}! 🥳")
    st.audio(audio_url)
