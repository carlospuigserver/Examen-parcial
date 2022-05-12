from conversaciones import filas
from conversaciones import columnas
from conversaciones import moda
from conversaciones import media
from conversaciones import varianza
from conversaciones import rango
from conversaciones import min
from conversaciones import max
from conversaciones import q1
from conversaciones import q3
from conversaciones import desv
from conversaciones import mediana
import pandas as pd

conversaciones=pd.read_csv("conversaciones.csv")
navegacion=pd.read_csv("navegación.csv")

# Numero filas
filasC=filas(conversaciones)
filasC.operacion()

#Num column
columnasC=columnas(conversaciones)
columnasC.operacion()

#Valores max
max_C = max(conversaciones,"id_lead")
max.operacion()

#Valores min
min_C = min(conversaciones,"id_lead")
min.operacion()


#Media
media_C = media(conversaciones,"id_lead")
media.operacion()

#Moda 
moda_C = moda(conversaciones,"id_lead")
moda.operacion()

#Mediana
mediana_C = mediana(conversaciones,"id_lead")
mediana.operacion()

#Desviación típica
desv_típ_C = desv(conversaciones,"id_lead")
desv.operacion()


#Varianza
varianza_C = varianza(conversaciones,"id_lead")
varianza.operacion()

#Rango
Rango_C = rango(conversaciones,"id_lead")
rango.operacion()


#Q1
q1_C = q1(conversaciones,"id_lead")
q1.operacion()

#Q3
q3_C = q3(conversaciones,"id_lead")
q3.operacion()

# Rango intercuartílico
a= conversaciones["id_lead"].quantile(0.25)
b= conversaciones["id_lead"].quantile(0.75)
rango_int= b-a
print("El rango intercuartílico es {}".format(rango_int))