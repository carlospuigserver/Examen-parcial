import pandas as pd
conversaciones=pd.read_csv("conversaciones.csv")
navegacion=pd.read_csv("navegación.csv")


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

from navegacion import Filas
from navegacion import Columnas
from navegacion import Moda
from navegacion import Media
from navegacion import Varianza
from navegacion import Rango
from navegacion import in
from navegacion import Max
from navegacion import Q1
from navegacion import Q3
from navegacion import Desv
from navegacion import Mediana



#CONVERSACIONES

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








#NAVEGACIÓN


# Numero filas
filasN=filas(navegacion)
filasN.calculo()

#Num column
columnasN=columnas(navegacion)
columnasN.calculo()

#Valores max
max_N = max(navegacion,"user_recurrent")
max.calculo()

#Valores min
min_N = min(navegacion,"user_recurrent")
min.calculo()


#Media
media_N = media(navegacion,"user_recurrent")
media.calculo()

#Moda 
moda_N = moda(navegacion,"user_recurrent")
moda.calculo()

#Mediana
mediana_N = mediana(navegacion,"user_recurrent")
mediana.calculo()

#Desviación típica
desv_típ_N = desv(navegacion,"user_recurrent")
desv.calculo()


#Varianza
varianza_N = varianza(navegacion,"user_recurrent")
varianza.calculo()

#Rango
Rango_N = rango(navegacion,"user_recurrent")
rango.calculo()


#Q1
q1_N = q1(navegacion,"user_recurrent")
q1.calculo()

#Q3
q3_N = q3(navegacion,"user_recurrent")
q3.calculo()

# Rango intercuartílico
a= navegacion["user_recurrent"].quantile(0.25)
b= navegacion["user_recurrent"].quantile(0.75)
rango_int= b-a
print("El rango intercuartílico es {}".format(rango_int))

