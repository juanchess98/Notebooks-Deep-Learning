import numpy as np
import matplotlib.pyplot as plt

'''
Funcion para crear la base de datos sintetica
'''

def crear_db(fn = lambda x: x, distribucion='normal', ruido=0.5, num_datos=100, rango=(0, 10)):
    t = np.linspace(rango[0], rango[1], num_datos)

    if distribucion == 'normal':
        noise = np.random.normal(0, ruido, t.shape)

    elif distribucion == 'logistic':
        noise = np.random.logistic(0, ruido, t.shape)

    signal = fn(t) + noise

    return (t, signal)

def plot_data(eje_X, eje_Y):
    plt.plot(eje_X, eje_Y, 'o', color='red')
    plt.show() #(block=True)
