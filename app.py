import streamlit as st
import matplotlib.pyplot as plt

# Musica "Tanti Auguri" (royalty-free)
audio_url = "https://cdn.pixabay.com/download/audio/2022/10/07/audio_7e5f9c8b47.mp3?filename=happy-birthday-to-you-piano-122163.mp3"


# Configura pagina
st.set_page_config(page_title="Torta per la Mamma", page_icon="🎂", layout="centered")

# Titolo
st.markdown("""
<div style="text-align: center;">
    <h1 style="color: #e63946;">🎂 Torta per la Mamma 🎂</h1>
    <h3 style="color: #6c757d;">Con amore, candeline distribuite e musica 💕</h3>
</div>
""", unsafe_allow_html=True)

# Dati
name = "Mamma, ti voglio bene"
age = st.slider("Età (numero di candeline):", 1, 45, 5)
color_top = st.color_picker("Colore glassa superiore", "#6ec1e4")
color_middle = st.color_picker("Colore centrale", "#5da3c3")
color_base = st.color_picker("Colore base", "#4682b4")
# Disegno torta
fig, ax = plt.subplots(figsize=(5, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 15)
ax.axis("off")

def draw_layer(x0, x1, y0, y1, color):
    ax.fill_between([x0, x1], y0, y1, color=color, edgecolor="black", linewidth=1.5)

# Tre piani
draw_layer(3, 7, 2, 4, color_base)       # base
draw_layer(3.5, 6.5, 4, 6, color_middle) # centro
draw_layer(4, 6, 6, 7.5, color_top)      # cima

# Calcolo candeline per piano
if age <= 15:
    top = age
    middle = base = 0
elif age <= 30:
    top = age // 2
    middle = age - top
    base = 0
else:
    top = age // 3
    middle = age // 3
    base = age - top - middle

# Funzione per disegnare candeline su un piano
def draw_candles(start_x, end_x, y_base, y_height, count):
    if count == 0:
        return
    spacing = (end_x - start_x) / max(count - 1, 1)
    for i in range(count):
        x = start_x + i * spacing
        ax.plot([x, x], [y_base, y_base + y_height], color="orange", linewidth=2)
        ax.plot(x, y_base + y_height + 0.2, marker="*", color="yellow", markersize=8)

# Candeline su ogni piano
draw_candles(4, 6, 7.5, 1, top)          # cima
draw_candles(3.7, 6.3, 6, 1, middle)     # centro
draw_candles(3.2, 6.8, 4, 1, base)       # base

# Scritta
ax.text(5, 1, name, fontsize=15, ha='center', color="darkmagenta", weight='bold')

# Mostra torta
st.pyplot(fig)

# Bottone
if st.button("🎉 Soffia le candeline 🎉"):
    st.balloons()
    st.success(f"Tanti auguri, {name} 🎁")
    st.audio(audio_url, format="audio/mp3")

