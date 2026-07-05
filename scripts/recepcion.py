import streamlit as st
import pandas as pd
import os

DATA_FILE = "data/recepcion.csv"
COLUMNAS = ["Producto", "Descripcion", "FechaEntrega", "Tratamiento", "Monto", "EstadoPago"]

# Cargar o crear hoja
if os.path.exists(DATA_FILE):
    hoja = pd.read_csv(DATA_FILE)
    for col in COLUMNAS:
        if col not in hoja.columns:
            hoja[col] = ""
else:
    hoja = pd.DataFrame(columns=COLUMNAS)

# Logo + título en la misma fila
col1, col2 = st.columns([1, 4])  # proporción de espacio
with col1:
    st.image("data/logo.png", width=120)  # logo al lado izquierdo
with col2:
    st.title(" Recepción Sneakers Biters")

# Formulario
with st.form("registro_form"):
    producto = st.selectbox("Producto", ["Tenis", "Mochila", "Bolsa", "Gorra"])
    descripcion = st.text_input("Descripción del pedido")
    fecha = st.date_input("Fecha de recepción")
    fechs = st.date_input("fecha de entrega")
    tratamiento = st.text_input("Tratamiento aplicado")
    monto = st.number_input("Monto a pagar", min_value=0.0, step=50.0)
    estado = st.selectbox("Estado de pago", ["Pagado", "Pendiente"])
    submit = st.form_submit_button("Agregar registro")

if submit:
    hoja.loc[len(hoja)] = [producto, descripcion, fecha, tratamiento, monto, estado]
    hoja.to_csv(DATA_FILE, index=False)
    st.success("✅ Registro agregado correctamente")

# Tabla dinámica
st.subheader("Registros actuales")
st.dataframe(hoja)

# Reportes
st.subheader("Reportes")
st.write("Ingresos totales:", hoja["Monto"].sum())
st.write("Pagados:", (hoja["EstadoPago"] == "Pagado").sum())
st.write("Pendientes:", (hoja["EstadoPago"] == "Pendiente").sum())

# Eliminar registros
st.subheader("🗑️ Eliminar registro")

if not hoja.empty:
    opciones = hoja.index.astype(str) + " - " + hoja["Producto"] + " - " + hoja["Descripcion"].fillna("")
    seleccion = st.selectbox("Selecciona el registro a eliminar", opciones)

    if st.button("Borrar registro"):
        idx = int(seleccion.split(" - ")[0])
        hoja = hoja.drop(idx).reset_index(drop=True)
        hoja.to_csv(DATA_FILE, index=False)
        st.success("🗑️ Registro eliminado correctamente")
        st.dataframe(hoja)
else:
    st.info("No hay registros para borrar.")
