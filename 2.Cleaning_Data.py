import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from subprocess import check_output
import os


def data_poke():
    data = pd.read_csv('./input/pokemon.csv')
    return(data)

def print_check():
    data = data_poke()
    print(data.head())
    print(data.tail())
    print(data.columns)
    print(data.shape)
    print(data.info())

def freq():
    data = data_poke()
    print(data['Type 1'].value_counts(dropna =False))

def desc():
    data = data_poke()
    print(data.describe())

def boxplot_pokemon():
    data = data_poke()
    data.boxplot(column = 'Attack', by = 'Legendary')
    plt.show()


# Tidy data

def melt_pokemon():
    data = data_poke()
    data_new = data.head()
    melted = pd.melt(frame = data_new, id_vars = 'Name', value_vars = ['Attack','Defense'])
    return(melted)


def pivot_pokemon():
    melted = melt_pokemon()
    pivot = melted.pivot(index = 'Name', columns = 'variable', values = 'value')
    print(pivot)

def concat_pokemon():
    data = data_poke()
    data1 = data.head()
    data2 = data.tail()
    con_data_row = pd.concat([data1, data2], axis = 0, ignore_index = True)
    print(con_data_row)


