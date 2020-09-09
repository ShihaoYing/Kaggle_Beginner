import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from subprocess import check_output
import os

def initialization():
    print(check_output(["ls","./input/"]).decode(encoding='UTF-8'))

    for dirname, _, filenames in os.walk("./input/"):
        for filename in filenames:
            print(os.path.join(dirname,filename))

data = pd.read_csv('./input/pokemon.csv')

# print(data.head())
# print(data.info())
# print(data.corr())

def heatmap():
    f,ax = plt.subplots(figsize = (18,18))
    sns.heatmap(data.corr(), annot = True, linewidth = 5, fmt = '.1f', ax=ax)
    plt.show()


heatmap()