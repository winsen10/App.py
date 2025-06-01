import streamlit as st

st.set_page_config(page_title="Kalkulator Material & Kayu", layout="centered")
st.title("📐 Kalkulator Material & Kubikasi Kayu")

tab1, tab2 = st.tabs(["🔹 Material Bangunan", "🔸 Kubikasi Kayu"])

with tab1:
    st.subheader("Hitung Kebutuhan Material Bangunan")
    luas = st.number_input("Luas Dinding/Lantai (m²):", min_value=0.0, step=1.0)
    jenis_bata = st.selectbox("Jenis Bata:", ["Bata Merah", "Hebel", "Batako"])

    if st.button("Hitung Material"):
        if jenis_bata == "Bata Merah":
            bata = 70 * luas
            semen = 1.5 * luas
            pasir = 0.03 * luas
        elif jenis_bata == "Hebel":
            bata = 25 * luas
            semen = 1.2 * luas
            pasir = 0.025 * luas
        else:
            bata = 30 * luas
            semen = 1.3 * luas
            pasir = 0.028 * luas

        st.success("Estimasi Material:")
        st.write(f"🔸 Bata: {int(bata)} buah")
        st.write(f"🔸 Semen: {semen:.1f} sak")
        st.write(f"🔸 Pasir: {pasir:.2f} m³")

with tab2:
    st.subheader("Hitung Kubikasi Kayu")
    panjang = st.number_input("Panjang (cm):", min_value=0.0, step=1.0)
    lebar = st.number_input("Lebar (cm):", min_value=0.0, step=1.0)
    tinggi = st.number_input("Tinggi/Tebal (cm):", min_value=0.0, step=1.0)
    jumlah = st.number_input("Jumlah Batang:", min_value=0, step=1)

    if st.button("Hitung Kubikasi"):
        vol_m3 = ((panjang / 100) * (lebar / 100) * (tinggi / 100)) * jumlah
        st.success(f"📦 Total Kubikasi: {vol_m3:.3f} m³")
