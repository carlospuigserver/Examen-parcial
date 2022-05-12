# Examen-parcial
# Examen-parcial

En este examen parcial de Análisis EDA y Transformación de Users he sido capaz de importar los dos ficheros csv en mi repositorio, posteriormente he realizado un 
profundo análisis de ambos, en los cuales, he calculado diferentes sucesos, como la moda, la varianza, la mediana, acompañados de diversos cálculos estadísticos 
simples. Esto ha sido posible de una manera fácil y eficaz gracias a pandas, cuyo valor es tratar estos diferentes cálculos de una manera rápida, relacionando una
pequeña función a cada uno de ellos. Por si fuera poco, ha sido añadida una gráfica, hay muchos tipos de estas, y he obtado por la simpleza de un diagrama de barras
como mejor campo viual.


El código que he empleado para llevar a cabo el trabajo anterior es el siguiente:


### MAIN.py

```
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

```



### Navegacion.py

```
import pandas as pd
import matplotlib.pyplot as plt
navegacion=pd.read_csv("navegación.csv")


class Grafico:
    
    def __init__(self, dataset, col1, col2):
        self.dataset = dataset
        self.col1 = col1
        self.col2 = col2
    
    def grafico_barras(self, title):
        self.dataset = pd.read_csv("navegación.csv")
        self.dataset.groupby(self.col1)[self.col2].sum().plot(kind="bar")
        plt.title(title)
        plt.xlabel(None)
        plt.show()



#Filas/Columnas
class Columnas:
  def __init__(self,csv):
    self.csv=csv
  def calculo(self):
    print("La cantidad de columnas que hay es de:", self.csv.shape[1])


class Filas:
  def __init__(self,csv):
    self.csv=csv
  def calculo(self):
    print("La cantidad de filas que hay es de:", self.csv.shape[0])


#Media
class media:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv

def calculo(self):
  media=self.csv[self.columna].mean()
  print("La media es la siguiente:")
  print(media)

#Moda
class Moda:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv
  def calculo(self):
    Moda=self.csv[self.columna].mode()
    print("La moda es la siguiente:")
    print(Moda)

#Mediana
class Mediana:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv
  def calculo(self):
    Mediana=self.csv[self.columna].median()
    print("La mediana es la siguiente:")
    print(Mediana)


#desv tipi
class desvia_típica:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def calculo(self):
    Desv=self.csv[self.columna].mad()
    print("La desv típic es :")
    print(Desv)


#varianza

class varianza:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def calculo(self):
    Varianza=self.csv[self.columna].var()
    print("La Varianza es :")
    print(Varianza)


#rango
class Rango:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv
  def calculo(self):
    Rango=self.csv[self.columna].mode()
    print("El rango es el siguiente:")
    print(Rango)


# Min max
class Min:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv
  def calculo(self):
    Min=self.csv[self.columna].min()
    print("El valor min es el siguiente:")
    print(Min)



class Max:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv
  def calculo(self):
    Max=self.csv[self.columna].max()
    print("El valor max es el siguiente:")
    print(Max)


#Cuartiles
class Q1:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def calculo(self):
    Q1=self.csv[self.columna].mad()
    print("El primer cuartil  es :")
    print(Q1)


class Q3:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def calculo(self):
    Q3=self.csv[self.columna].mad()
    print("El tercer cuartil  es :")
    print(Q3)


```



### Conversaciones.py


```

import pandas as pd
import matplotlib.pyplot as plt
conversaciones=pd.read_csv("conversaciones.csv")


class Grafico:
    
    def __init__(self, dataset, col1, col2):
        self.dataset = dataset
        self.col1 = col1
        self.col2 = col2
    
    def grafico_barras(self, title):
        self.dataset = pd.read_csv("conversaciones.csv")
        self.dataset.groupby(self.col1)[self.col2].sum().plot(kind="bar")
        plt.title(title)
        plt.xlabel(None)
        plt.show()



#Filas/Columnas
class columnas:
  def __init__(self,csv):
    self.csv=csv
  def operacion(self):
    print("La cantidad de columnas que hay es de:", self.csv.shape[1])


class filas:
  def __init__(self,csv):
    self.csv=csv
  def operacion(self):
    print("La cantidad de filas que hay es de:", self.csv.shape[0])


#Media
class media:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv

def operacion(self):
  media=self.csv[self.columna].mean()
  print("La media es la siguiente:")
  print(media)

#Moda
class Moda:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv
  def operacion(self):
    moda=self.csv[self.columna].mode()
    print("La moda es la siguiente:")
    print(moda)

#Mediana
class Mediana:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv
  def operacion(self):
    mediana=self.csv[self.columna].median()
    print("La mediana es la siguiente:")
    print(mediana)


#desv tipi
class desvia_típica:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def operacion(self):
    desv=self.csv[self.columna].mad()
    print("La desv típic es :")
    print(desv)


#varianza

class varianza:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def operacion(self):
    varianza=self.csv[self.columna].var()
    print("La Varianza es :")
    print(varianza)


#rango
class Rango:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv
  def operacion(self):
    rango=self.csv[self.columna].mode()
    print("El rango es el siguiente:")
    print(rango)


# Min max
class Min:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv
  def operacion(self):
    min=self.csv[self.columna].min()
    print("El valor min es el siguiente:")
    print(min)



class Max:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv
  def operacion(self):
    max=self.csv[self.columna].max()
    print("El valor max es el siguiente:")
    print(max)


#Cuartiles
class Q1:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def operacion(self):
    q1=self.csv[self.columna].mad()
    print("El primer cuartil  es :")
    print(q1)


class Q3:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def operacion(self):
    q3=self.csv[self.columna].mad()
    print("El tercer cuartil  es :")
    print(q3)


```


