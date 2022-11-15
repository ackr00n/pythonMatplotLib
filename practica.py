

# consume los datos del archivo de inversiones
# almacena en un dataframe el NOM_EMS, la superficie y el TIPUSSOL
# giráfico de dspersión de los importes de inversiones por TIPUSSOL
# gráfico de barras de la inversión media de los 10 primeros NOM_ENS
# grafico circular de las inversiones de 10 TIPUSSOL

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("cataluña.csv")

df = datos[["NOM_ENS", "SUPERFICIE", "TIPUSSOL"]]

def graficoDispersion ():
    df.plot.scatter(x="NOM_ENS", y= "SUPERFICIE", alpha=0.2)
    plt.show()

#graficoDispersion()

def barras():
    valores = df.groupby("NOM_ENS").mean()
    valores.head(10).plot.barh()
    plt.show()
barras()