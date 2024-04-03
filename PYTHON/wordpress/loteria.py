#Importar libreria tkkinter para generar formulario
import random
from tkinter import *

def combinacion():
    '''Función que devuelve una cadena de texto con una combinación de
    la lotería de Euromillones.
        Ejemplo: 12, 15, 23, 43, 45  C: 2, 10'''
    numeros = random.sample(range(1, 51), 5)  # Genera 5 números aleatorios entre 1 y 50
    numeros.sort()  # Ordena los números
    complementarios = random.sample(range(1, 12), 2)  # Genera 2 números complementarios entre 1 y 11
    complementarios.sort()  # Ordena los números complementarios
    return (", ".join(map(str, numeros)) + '  C: ' +
            ", ".join(map(str, complementarios)))

def sorteo():
    '''Función que toma una cadena de texto y la presenta en el
    widget label'''
    label.configure(text=combinacion())

# Crear la ventana principal
ventana = Tk()
ventana.title('Euromillones')

# Crear etiquetas para mostrar información y botón para generar combinaciones
etiq_info = Label(winroot, text='Pulsa el botón para generar una combinación.')
etiq_info.pack(side='top')

etiqueta = Label(winroot, text='Número de lotería', width=30)
etiqueta.pack(side='left')

boton = Button(winroot, text="Buscar", command=sorteo)
boton.pack(side='left')

# Iniciar el bucle principal de la aplicación
mainloop()
