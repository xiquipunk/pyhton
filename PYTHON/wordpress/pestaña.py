# Importar librería tkinter 
from tkinter import *
from tkinter import ttk  

# Crear ventana 
# Definir tamaño de la ventana

ventana = Tk()
ventana.geometry("560x300")  

tab_control = ttk.Notebook(window)

# Lista de nombres
nombres = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Lista de textos
etiquetas = [
    '### Jano, dios de los portales. January en Inglés ###',
    '### Mes de las hogueras purificatorias (februa) ###',
    '### Marte, dios de la guerra ###',
    '### Aprilis o Apertura de flores(primavera) ###',
    '### Maia, diosa de la abundancia ###',
    '### Juno, diosa del hogar y la familia ###',
    '### Por Julio cesar ###',
    '### Por Octavio Augusto ###',
    '### Septimo mes ###',
    '### Octavo mes ###',
    '### Noveno mes ###',
    '### Undecimo mes ###'
]

formulario = []  
etiqueta = [] 

# Crear un nuevo formulario

for i, tab in enumerate(tabs):
    marco = ttk.Frame(tab_control)  
    formulario.append(marco)  
    tab_control.add(marco text=tab)  

    lbl = Label(marco, text=labels_text[i])  #
    lbl.pack(padx=10, pady=10) 
    etiqueta.append(lbl) 

tab_control.pack(expand=1, fill='both')

window.mainloop()


