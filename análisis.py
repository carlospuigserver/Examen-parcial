import pandas as pd
import numpys as 
conversaciones=pd.read_csv("conversaciones.csv")
navegacion=pd.read_csv("conversaciones.csv")

file=open("conversaciones.csv","w")
file.write("date","hour","id_lead","id_user","gclid","lead_type","result")

file=open("navegación.csv","w")
file.write("ts","uuid","id_user","gclid","user_recurrent","url_landing")


