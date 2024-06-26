from sys import displayhook
from tkinter.tix import DisplayStyle
import pandas as pd
import plotly.express as px
import streamlit as st

data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Exploración de Datos de Vehículos de EEUU")

#Botón para construir histograma
hist_button = st.button('Construir Histograma')

#Acción
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de autos')
    
#Crear histograma 
fig = px.histogram(data, x="odometer")

#Mostrar gráfico
st.plotly_chart(fig, use_container_width=True)

    
    
#Crear dispersión 

disper_button = st.button('Crear gráfico de Dispersión') 

#Acción
if disper_button:
    st.write('Creación de gráfico de dispersión')
    
#crear dispersión
fig_scatter = px.scatter(data, x='model_year', y='price', color='fuel')

#Mostrar gráfico
st.plotly_chart(fig_scatter, use_container_width=True)