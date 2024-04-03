import tkinter

# Crear la ventana principal
principal = tkinter.Tk()
principal.title('Formulario')

# Crear etiquetas i marcos
etiqueta1 = tkinter.Label(principal, text="FORMULARIO DE REGISTRO")
marco1 = tkinter.Frame(principal, bd=8, relief="groove")

etiqueta2 = tkinter.Label(marco1, text="Nombre:")
marco2 = tkinter.Entry(marco1, width=18)

etiqueta3 = tkinter.Label(marco1, text="Contraseña:")
marco3 = tkinter.Entry(marco1, width=18)

etiqueta4 = tkinter.Label(marco1, text="Repite Contraseña:")
marco4 = tkinter.Entry(marco1, width=18)

etiqueta5 = tkinter.Label(marco1, text="Email:")
marco5 = tkinter.Entry(marco1, width=18)

etiqueta6 = tkinter.Label(marco1, text="DNI:")
marco6 = tkinter.Entry(marco1, width=18)

etiqueta7 = tkinter.Label(marco1, text="Población:")
marco7 = tkinter.Entry(marco1, width=18)

etiqueta8 = tkinter.Label(marco1, text="Codigo Postal:")
marco8 = tkinter.Entry(marco1, width=18)

# Crear botones 
enviar = tkinter.Button(marco1, text="Registro")
borrar = tkinter.Button(marco1, text="Borrar")
salir = tkinter.Button(marco1, text="Salir")

# Organizar los elementos
etiqueta1.grid(row=0, column=1, pady=10)
marco1.grid(padx=10, pady=10, row=1, column=1)

etiqueta2.grid(row=0, column=0)
marco2.grid(row=0, column=1, padx=10)

etiqueta3.grid(row=1, column=0)
marco3.grid(row=1, column=1, padx=10)

etiqueta4.grid(row=2, column=0)
marco4.grid(row=2, column=1, padx=10)

etiqueta5.grid(row=3, column=0)
marco5.grid(row=3, column=1, padx=10)

etiqueta6.grid(row=4, column=0)
marco6.grid(row=4, column=1, padx=10)

etiqueta7.grid(row=5, column=0)
marco7.grid(row=5, column=1, padx=10)

etiqueta8.grid(row=6, column=0)
marco8.grid(row=6, column=1, padx=10)

enviar.grid(row=7, column=2)
salir.grid(row=7, column=3)
borrar.grid(row=7, column=4)

principal.mainloop()
