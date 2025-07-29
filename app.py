import streamlit as st
import random

st.title("Lanzar una moneda")
st.write("Haz clic en el botón para lanzar la moneda.")

if st.button("Lanzar"):
    resultado = random.choice(["Cara", "Cruz"])
    st.success(f"¡Salió {resultado}!")

