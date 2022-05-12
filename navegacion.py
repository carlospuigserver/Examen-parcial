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


