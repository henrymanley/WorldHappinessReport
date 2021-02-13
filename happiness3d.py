"""
Script to visualize World Happiness Data.

Henry Manley - Last Modified 2/13/2021
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import  axes3d, Axes3D

plt.rc('font',family='Karla')
cwd = os.getcwd()


def loader():
    """
    Loads local data and sets global df to reference.

    Returns unique list of regions of the world.
    """
    input = cwd + '/Data/happy_reportt.csv'

    global df
    df = pd.read_csv(input)
    df = df.dropna()
    print(df.head())
    colors = df.REGION.unique()
    return colors

def colorMaker(colorList):
    """
    Generates contrasting hex colors for n categories

    Returns a dictionairy
    """
    accum = {}
    for color in colorList:
        random_number = random.randint(0,16777215)
        hex_number = format(random_number,'x')
        hex_number = '#'+hex_number

        accum[color] = hex_number
    return accum

# Scatter  < Happy ~ GDP + Life Expectancy >

def vis(colorDict):
    """
    Visualizes the df.
    """
    my_dpi=96

    for angle in range(70,210,2):
        threedee = plt.figure(figsize=(940/my_dpi, 840/my_dpi), dpi=my_dpi).gca(projection='3d')
        threedee.set_facecolor('#242131')
        threedee.tick_params(colors="#FFFFFF")
        threedee.grid(color='#FFFFFF', linestyle='-', linewidth=0.5)

        for region in colorDict.keys():
            threedee.scatter(df['LOGDP'], df['HLE'], df['HAPPY'], c=colorDict[region], marker='o', label = region)
            threedee.scatter(df['LOGDP'], df['HLE'], df['HAPPY'], c=df['REGION'].map(colorDict))
            threedee.set_xlabel('GDP per Capita (Log Scale)', c = '#FFFFFF')
            threedee.set_ylabel('Healthy Life Expectancy', c = '#FFFFFF')
            threedee.set_zlabel('Happiness Score', c = '#FFFFFF')
            threedee.legend()

        threedee.view_init(30,angle)
        filename= cwd +  '/Images/3DScatter'+str(angle)+'.png'
        plt.savefig(filename, dpi=96)
        plt.gca()

def compileGif():
    bashCommand = "convert -delay 50 3DScatter*.png animated_scatter.gif"
    os.system(bashCommand)

if __name__ == "__main__":
    colorList = loader()
    colors = colorMaker(colorList)
    vis(colors)
    os.chdir(cwd + '/Images/')
    compileGif()
