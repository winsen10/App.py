import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Material & Kayu", layout="centered")
st.title("📐 Kalkulator Material & Kubikasi Kayu")

# Tab navigasi
tab1, tab2 = st.tabs(["🔹 Material Bangunan", "🔸 Kubikasi Kayu"])

# --- TAB 1: Kalkulator Material Bangunan ---
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
        else:  # Batako
            bata = 30 * luas
            semen = 1.3 * luas
            pasir = 0.028 * luas

        st.success("Estimasi Material:")
        st.write(f"🔸 Bata: {int(bata)} buah")
        st.write(f"🔸 Semen: {semen:.1f} sak")
        st.write(f"🔸 Pasir: {pasir:.2f} m³")

# --- TAB 2: Kalkulator Kubikasi Kayu ---
with tab2:
    st.subheader("Hitung Kubikasi Kayu (dalam feet)")

    panjang_ft = st.number_input("Panjang (ft):", min_value=0.0, step=0.1)
    lebar_ft = st.number_input("Lebar (ft):", min_value=0.0, step=0.1)
    tinggi_ft = st.number_input("Tinggi/Tebal (ft):", min_value=0.0, step=0.1)
    jumlah = st.number_input("Jumlah Batang:", min_value=0, step=1)

    if st.button("Hitung Kubikasi"):
        # 1 ft³ = 0.0283168 m³
        volume_per_batang_m3 = panjang_ft * lebar_ft * tinggi_ft * 0.0283168
        total_volume = volume_per_batang_m3 * jumlah
        st.success(f"📦 Total Kubikasi: {total_volume:.3f} m³")
