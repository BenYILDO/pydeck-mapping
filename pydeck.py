import streamlit as st
import pydeck as pdk
import pandas as pd

# Test verisi
data = {
    "İlçe": ["Kadıköy", "Ümraniye", "Beşiktaş"],
    "Enlem": [40.9917, 41.0153, 41.0420],
    "Boylam": [29.1244, 29.1245, 29.0071],
}

df = pd.DataFrame(data)
df["Konum"] = df[["Enlem", "Boylam"]].values.tolist()

# Harita katmanı
layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position="Konum",
    get_radius=500,  # Nokta büyüklüğü
    get_color="[200, 30, 0, 160]",  # Kırmızı ton
    pickable=True,
)

# Harita görünümü
view_state = pdk.ViewState(latitude=41.0082, longitude=28.9784, zoom=10)

# Pydeck haritası
st.title("Basit Harita Görselleştirmesi")
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
st.pydeck_chart(r)
