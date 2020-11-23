# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:51:26 2020

@author: andrews.alves
"""
#Import libraries
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import locale
from math import sin, cos, sqrt, atan2, radians 
import geopy.distance 
import plotly.graph_objects as go

#Importing databases
url_POSICOES = 'https://raw.githubusercontent.com/andrewsmb7/testemb7/main/Data%20engineer/04%20-%20Data%20engineer/Databases/posicoes.csv'
url_POI = 'https://raw.githubusercontent.com/andrewsmb7/testemb7/main/Data%20engineer/04%20-%20Data%20engineer/Databases/base_pois_def.csv'

Posicoes = pd.read_csv(url_POSICOES, error_bad_lines=False)
POI = pd.read_csv(url_POI, error_bad_lines=False)

#Creating new column to storage car status: Moving or Stopped 
Posicoes['Status'] = ''

#Test if car is moving or stopped
for index, row in Posicoes.iterrows():
    if row['velocidade'] <= 5 or row['ignicao'] == "False":
        Posicoes.loc[index,'Status'] = "Stopped"  
    else: 
        Posicoes.loc[index,'Status'] = "Moving"     

#Slicing only important part of date        
Posicoes["DataHora"] = Posicoes["data_posicao"].str[3:]

#Changing date format
Posicoes['DataHora'] = pd.to_datetime(Posicoes['DataHora'], infer_datetime_format=True)

#Converting 'Raio' meters on 'Raio' Km
POI["raio_km"] = POI["raio"]/1000

#Total stopped hours - by car
Posicoes["StopHour"] = ""

for index, row in df1.iterrows():
    if row["velocidade"] <= 5:
        Posicoes["StopHour"] = Posicoes["DataHora"]
        #df1.loc[index,'Status'] = df1["DataHora"]  
    else: 
        Posicoes["StopHour"] == 0 
        #df1.loc[index,'Status'] = "Moving" 

# Setting coordinates between both dfs
PONTO_CAR = [{Posicoes["latitude"].loc,Posicoes["longitude"].loc}]
PONTO_POI = [{POI["latitude"].loc,POI["longitude"].loc}]
radius = POI['raio_km'] # in kilometer

PONTO_CAR_tuple = (PONTO_CAR[0].values())
PONTO_CAR_tuple = (PONTO_POI[0].values())

#Dropping moving cars
Posicoes_PARADO = Posicoes.loc[Posicoes['Status'] == 'Stopped']

KPI_horas_individuais = pd.pivot_table(Posicoes_PARADO, values='StopHour', index=['placa','DataHora'],
                    aggfunc=np.sum)



KPI_horas_individuais.to_csv('C:/Users/andrews.alves/Desktop/resultados_consolidado_POIs.csv', header=True, index=False, sep=',')