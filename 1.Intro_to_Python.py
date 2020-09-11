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

def data_read():
    data = pd.read_csv('./input/pokemon.csv')
    return data

# print(data.head())
# print(data.info())
# print(data.corr())
# print(data.columns)

#HeatMap
# def heatmap():
#     data = data_read()
#     f,ax = plt.subplots(figsize = (18,18))
#     sns.heatmap(data.corr(), annot = True, linewidth = 5, fmt = '.1f', ax=ax)
#     plt.show()

# heatmap()

# Matplotlib 

#Line Plot
def line_plot():
    data = data_read()
    data.Speed.plot(kind = 'line', color = 'g', label = 'Speed', linewidth = 1,
                    alpha = 0.5, grid = True, linestyle = ':')
    data.Defense.plot(color = 'r', label = 'Defense', linewidth = 1,
                    alpha = 0.5, grid = True, linestyle = '-.')
    plt.legend(loc = 'upper right')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('Line Plot')
    plt.show()

# line_plot()

#Scatter Plot
def scatter_plot():
    data = data_read()
    data.plot(kind = 'scatter', x = 'Attack', y = 'Defense', alpha = 0.5, color = 'r')
    plt.xlabel('Attack')
    plt.ylabel('Defense')
    plt.title('Attack Defense Scatter Plot')
    plt.show()

# scatter_plot()

#Histogram
def histogram():
    data = data_read()
    data.Speed.plot(kind = 'hist', bins = 50, figsize = (12,12))
    plt.show()

# histogram()

#Dictionary
def dictionary_sample():
    dictionary = {'Spain':'Madrid','USA':'Vegas'}
    print(dictionary.keys())
    print(dictionary.values())

    # Keys have to be immutable objects like string, boolean, float, integer or tubles
    # List is not immutable
    # Keys are unique
    dictionary['Spain'] = "Barcelona"    # update existing entry
    print(dictionary)
    dictionary['France'] = "Paris"       # Add new entry
    print(dictionary)
    del dictionary['Spain']              # remove entry with key 'spain'
    print(dictionary)
    print('France' in dictionary)        # check include or not
    dictionary.clear()                   # remove all entries in dict
    print(dictionary)


#Pandas
def pandas_sample():
    data = data_read()
    series = data['Defense']
    data_frame = data[['Defense']]

    print(type(series))
    print(type(data_frame))
    
    #filter pandas data frame
    x = data['Defense']>200
    print(data[x])

    #filter pandas with logic
    y1 = data[np.logical_and(data['Defense']>200, data['Attack']>100 )]
    print(y1)

    y2 = data[(data['Defense']>200) & (data['Attack']>100)]
    print(y2)

#Scope

import builtins
print(dir(builtins))

