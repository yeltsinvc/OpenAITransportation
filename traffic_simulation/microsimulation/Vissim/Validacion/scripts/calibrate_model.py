# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 18:52:27 2023

@author: User
"""

import pandas as pd
import scipy.stats as stats
import win32com.client

# Crear una instancia de Vissim
vissim = win32com.client.Dispatch("Vissim.Vissim")

# Cargar el archivo de mapa
map_file = "..\\model\\network.inpx"
vissim.LoadNet(map_file)

# Cargar el archivo de demanda de tráfico
demand_file = "..\\model\\data.fzp"
vissim.LoadVehicleTypes(demand_file)
vissim.LoadDemand(demand_file)

# Configurar los parámetros de la simulación
sim_params = vissim.Simulation.SetAttValue("SimPeriod", 3600)
vissim.Simulation.SetAttValue("UseMaxSimSpeed", True)

# Realizar una simulación y guardar los resultados
results_file = "C:..\\results\\results.fzp"
vissim.Simulation.RunContinuous()
vissim.SaveResult(results_file)

# Leer los resultados de la simulación y crear un DataFrame
results = pd.read_csv(results_file, sep='\t', skiprows=1, names=['Time', 'Link', 'Flow'])

# Cargar los datos reales de flujo vehicular desde un archivo Excel
real_data_file = "data\\real_data.xlsx"
real_data = pd.read_excel(real_data_file, sheet_name='Flujo vehicular')

# Calcular los valores medios de flujo vehicular para cada enlace en el modelo
model_data = results.groupby('Link')['Flow'].mean().reset_index()

# Unir los datos reales y los datos del modelo por enlace
merged_data = pd.merge(real_data, model_data, on='Link', suffixes=['_real', '_model'])

# Calcular la diferencia entre los valores reales y los valores del modelo
merged_data['Diff'] = merged_data['Flow_real'] - merged_data['Flow_model']

# Calcular la prueba t de Student para la diferencia de valores
t_statistic, p_value = stats.ttest_1samp(merged_data['Diff'], 0)

# Imprimir el resultado de la prueba t de Student
if p_value < 0.05:
    print("El modelo no está calibrado (p-value = {})".format(p_value))
else:
    print("El modelo está calibrado (p-value = {})".format(p_value))

# Cerrar Vissim
vissim = None

