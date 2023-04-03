# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 22:29:45 2023

@author: User
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
"""
# leer archivo CSV en fragmentos de 100,000 filas cada uno
chunk_size = 100000
i=0
for chunk in pd.read_csv('data/Shared_Micromobility_Vehicle_Trips.csv', chunksize=chunk_size):
    i+=1
    break"""

# Leer el archivo CSV
df = pd.read_csv('data/Shared_Micromobility_Vehicle_Trips.csv')

# Convertir la columna 'Start Time' en un objeto de tipo fecha y hora
df['Start Time'] = pd.to_datetime(df['Start Time'])

# Extraer la fecha de cada viaje y guardarla en una nueva columna 'Date'
df['Date'] = df['Start Time'].dt.date

# Crear una matriz origen-destino por día
for date, group in df.groupby('Date'):
    # Crear la matriz origen-destino
    trips = group.groupby(['Council District (Start)', 'Council District (End)']).size().reset_index(name='counts')
    matrix = pd.pivot_table(trips, values='counts', index=['Council District (Start)'], columns=['Council District (End)'], fill_value=0)

    # Crear un gráfico de la matriz origen-destino
    fig, ax = plt.subplots()
    im = ax.imshow(matrix, cmap='Blues', interpolation='nearest')
    ax.set_xticks(np.arange(len(matrix.columns)))
    ax.set_yticks(np.arange(len(matrix.index)))
    ax.set_xticklabels(matrix.columns)
    ax.set_yticklabels(matrix.index)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    for i in range(len(matrix.index)):
        for j in range(len(matrix.columns)):
            text = ax.text(j, i, matrix.iloc[i, j], ha="center", va="center", color="w")
    ax.set_title('Matriz origen-destino el {}'.format(date))
    plt.savefig('Resultados/{}.png'.format(date))
    plt.close(fig)

    # Crear un gráfico de histograma de distancia recorrida
    fig, ax = plt.subplots()
    ax.hist(group['Trip Distance'], bins=20, range=(0,20))
    ax.set_xlabel('Distancia recorrida (millas)')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Distribución de distancias el {}'.format(date))
    plt.savefig('Distance/{}.png'.format(date))
    plt.close(fig)