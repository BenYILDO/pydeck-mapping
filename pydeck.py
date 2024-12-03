import streamlit as st
import pandas as pd
import pydeck as pdk

# Streamlit başlat
st.title("İstanbul Elektrikli Şarj İstasyonu Lokasyon Analizi")

# Veri seti oluşturma
data = {
    "İlçe": ["Kadıköy", "Ümraniye", "Beşiktaş", "Esenyurt", "Pendik"],
    "Trafik": [9, 8, 10, 6, 7],
    "Nüfus": [8, 7, 9, 10, 6],
    "Arazi_Maliyeti": [7, 5, 8, 4, 6],
    "Enlem": [40.9917, 41.0153, 41.0420, 41.0432, 40.8803],
    "Boylam": [29.1244, 29.1245, 29.0071, 28.6758, 29.2379],
}

df = pd.DataFrame(data)

# Veri işleme
st.write("Veri Tablosu:")
st.dataframe(df)

# Harita için konum sütunu ekleme
df["Konum"] = df[["Enlem", "Boylam"]].values.tolist()

# Pydeck harita katmanı
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
r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{İlçe}"})
st.pydeck_chart(r)

# Dinamik seçim
selected_ilce = st.selectbox("Bir ilçe seçin:", df["İlçe"])
selected_data = df[df["İlçe"] == selected_ilce]

if not selected_data.empty:
    st.write(f"Seçilen İlçe: {selected_ilce}")
    st.write(selected_data[["Trafik", "Nüfus", "Arazi_Maliyeti"]])
