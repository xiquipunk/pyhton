#Calcular mes
#Importar libreria tkkinter para generar formulario
#Importar librearia datetime para poder trabajar fechas

from tkinter import *
from datetime import datetime


#Definir colecciones

meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
diaSemana = { 0: "Domingo", 1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6: "Sábado"}

#Declarar variables

ahora = datetime.now()
numero_mes = ahora.month
numero_dia = ahora.weekday()  # usar weekday como nombre del dia de la semmana.
dia = diaSemana.get(numero_dia)
mes = meses.get(numero_mes)

fecha = "{}, {} de {} del {}".format(dia, ahora.day, mes, ahora.year)

#Declarar formulario

ventana = Tk()
ventana.geometry("300x155")
ventana.title("Fecha Actual")
etiq_fecha = Label(ventana, text=fecha, font=("Arial", 14))
etiq_fecha.pack()

#Declarar procediemiento

def mostrar_mes():
    opcion = int(entrar_mes.get())
    if 1 <= opcion <= 12:
        mes_seleccionado = meses[opcion]
        etiq_mes.config(text=f"********* {mes_seleccionado} *********")
    else:
        etiq_mes.config(text="Introduce un número entre 1 y 12")
        

#Busqueda del nuemro de mes

etiq_instruccion = Label(ventana, text="Introduce el número de mes:")
etiq_instruccion.pack()

entrar_mes = Entry(ventana, width=10)
entrar_mes.pack()

button_mostrar_mes = Button(ventana, text="Mostrar Mes", command=mostrar_mes)
button_mostrar_mes.pack()

etiq_mes = Label(ventana, text="")
etiq_mes.pack()

ventana.mainloop()
