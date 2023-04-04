# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 22:29:45 2023

@author: User
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

"""# Read CSV file in chunks of 100,000 rows each
chunk_size = 100000
i = 0
for chunk in pd.read_csv('data/Shared_Micromobility_Vehicle_Trips.csv', chunksize=chunk_size):
    i += 1
    break"""

# Read CSV file
df = pd.read_csv('data/Shared_Micromobility_Vehicle_Trips.csv')

# Convert 'Start Time' column to datetime object
df['Start Time'] = pd.to_datetime(df['Start Time'])

# Extract date from each trip and store it in a new 'Date' column
df['Date'] = df['Start Time'].dt.date

# Create an origin-destination matrix per day
for date, group in df.groupby('Date'):
    # Create origin-destination matrix
    trips = group.groupby(['Council District (Start)', 'Council District (End)']).size().reset_index(name='counts')
    matrix = pd.pivot_table(trips, values='counts', index=['Council District (Start)'], columns=['Council District (End)'], fill_value=0)

    # Create a heatmap of the origin-destination matrix
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
    ax.set_title('Origin-Destination Matrix on {}'.format(date))
    plt.savefig('Results/{}.png'.format(date))
    plt.close(fig)

    # Create a histogram of trip distances
    fig, ax = plt.subplots()
    ax.hist(group['Trip Distance'], bins=20, range=(0,20))
    ax.set_xlabel('Trip Distance (miles)')
    ax.set_ylabel('Frequency')
    ax.set_title('Distance Distribution on {}'.format(date))
    plt.savefig('Distance/{}.png'.format(date))
    plt.close(fig)

    # Crear un gráfico de histograma de distancia recorrida
    fig, ax = plt.subplots()
    ax.hist(group['Trip Distance'], bins=20, range=(0,20))
    ax.set_xlabel('Distancia recorrida (millas)')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Distribución de distancias el {}'.format(date))
    plt.savefig('Distance/{}.png'.format(date))
    plt.close(fig)