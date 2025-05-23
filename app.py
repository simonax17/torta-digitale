import streamlit as st
import matplotlib.pyplot as plt

# 🎶 Musica "Tanti Auguri" (royalty-free, testata per Streamlit)
audio_url = "https://cdn.pixabay.com/audio/2022/10/07/audio_7e5f9c8b47.mp3"

# 🎈 Configura la pagina
st.set_page_config(page_title="Torta per la Mamma", page_icon="🎂", layout="centered")

# 💖 Titolo
st.markdown("""
<div style="text-align: center;">
    <h1 style="color: #e63946;">🎂 Torta per la Mamma 🎂</h1>
    <h3 style="color: #6c757d;">Con amore, candeline e una canzone speciale 💕</h3>
</div>
""", unsafe_allow_html=True)

# 🎁 Dati fissi
name = "Mamma, ti voglio bene"
age = st.slider("Età (numero di candeline):", 1, 45, 5)
color_top = st.color_picker("Colore glassa superiore", "#ffb3c6")
color_middle = st.color_picker("Colore centrale", "#ff8fab")
color_base = st.color_picker("Colore base", "#fb6f92")

# 📊 Disegno della torta frontale
fig, ax = plt.subplots(figsize=(5, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 15)
ax.axis("off")

# 🧁 Tre piani della torta (rettangoli)
def draw_layer(x0, x1, y0, y1, color):
    ax.fill_between([x0, x1], y0, y1, color=color, edgecolor="black", linewidth=1.5)

draw_layer(3, 7, 2, 4, color_base)     # base
draw_layer(3.5, 6.5, 4, 6, color_middle)  # centro
draw_layer(4, 6, 6, 7.5, color_top)    # cima

# 🕯️ Candeline
spacing = (6 - 4) / max(age - 1, 1)
for i in range(age):
    x = 4 + i * spacing
    ax.plot([x, x], [7.5, 8.5], color="orange", linewidth=2)
    ax.plot(x, 8.7, marker="*", color="yellow", markersize=10)

# 💌 Testo in basso
ax.text(5, 1, name, fontsize=15, ha='center', color="darkmagenta", weight='bold')

# 🎂 Mostra torta
st.pyplot(fig)

# 🎶 Bottone per attivare auguri
if st.button("🎉 Soffia le candeline e ascolta 🎶"):
    st.balloons()
    st.success(f"Tanti auguri, {name}! 🎁")
    st.audio(audio_url, format="audio/mp3")
