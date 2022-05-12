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


