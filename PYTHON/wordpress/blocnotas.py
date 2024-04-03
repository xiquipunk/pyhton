from tkinter import *
from tkinter import ttk

class Aplicacion():
    def __init__(self):
        # Crear la ventana principal
        self.raiz = Tk()
        self.raiz.geometry('500x500')  
        self.raiz.resizable(width=False, height=False)  
        self.raiz.title('Informacion sobre el mes') 
        
        # Crear un texto para mostrar la información
        self.tinfo = Text(self.raiz, width=80, height=29)
        self.tinfo.pack(side=TOP)  
        
        # Crear botón para mostrar la información
        self.binfo = ttk.Button(self.raiz, text='Informacion', command=self.verinfo)
        self.binfo.pack(side=LEFT)  
        
        # Crear botón para salir de la aplicación
        self.bsalir = ttk.Button(self.raiz, text='Salir', command=self.raiz.destroy)
        self.bsalir.pack(side=RIGHT)  
        
       self.binfo.focus_set()
        
        # Iniciar el bucle principal de la aplicación
        self.raiz.mainloop()

    def verinfo(self):
        # Limpiar el contenido
        self.tinfo.delete("1.0", END)
        
        # Información sobre cada mes
        info1 = "### Jano, dios de los portales. January en Inglés ###"
        info2 = "### Mes de las hogueras purificatorias (februa) ###"
        info3 = "### Marte, dios de la guerra ###"
        info4 = "### Aprilis o Apertura de flores (primavera) ###"
        info5 = "### Maia, diosa de la abundancia ###"
        info6 = "### Juno, diosa del hogar y la familia ###"
        info7 = "### Por Julio César ###"
        info8 = "### Por Octavio Augusto ###"
        info9 = "### Septimo mes ###"
        info10 = "### Octavo mes ###"
        info11 = "### Noveno mes ###"
        info12 = "### Decimo mes ###"
        
        # Mostrar la información de cada mes
        texto_info = "(Enero:) " + info1 + "\n\n"
        texto_info += "(Febrero:) " + info2 + "\n\n"
        texto_info += "(Marzo:) " + info3 + "\n\n"
        texto_info += "(Abril:) " + info4 + "\n\n"
        texto_info += "(Mayo:) " + info5 + "\n\n"
        texto_info += "(Junio:) " + info6 + "\n\n"
        texto_info += "(Julio:) " + info7 + "\n\n"
        texto_info += "(Agosto:) " + info8 + "\n\n"
        texto_info += "(Septiembre:) " + info9 + "\n\n"
        texto_info += "(Octubre:) " + info10 + "\n\n"
        texto_info += "(Noviembre:) " + info11 + "\n\n"
        texto_info += "(Diciembre:) " + info12 + "\n\n"
        
        # Insertar la información
        self.tinfo.insert("1.0", texto_info)

def main():
        mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
