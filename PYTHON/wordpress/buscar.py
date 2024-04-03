import tkinter as tk
from tkinter import messagebox, ttk
import openpyxl
from tkhtmlview import HTMLLabel


# Función para buscar por ID
def buscar_id():
    buscar_por_campo("ID")

# Función para buscar por Usuario
def buscar_usuario():
    buscar_por_campo("Usuario")

# Función para buscar por Contraseña
def buscar_contraseña():
    buscar_por_campo("Contraseña")

# Función para buscar por Email
def buscar_email():
    buscar_por_campo("Email")

# Función para buscar por Fecha de Registro
def buscar_fecha_registro():
    buscar_por_campo("Fecha de Registro")

# Función principal para buscar por un campo específico
def buscar_por_campo(campo):
    try:
        workbook = openpyxl.load_workbook('datos_usuarios.xlsx')
        sheet = workbook['Usuarios']
    except FileNotFoundError:
        # Mostrar un mensaje de error si el archivo de datos no se encuentra
        messagebox.showerror("Error", "Archivo de datos no encontrado")
        return

    # Obtener el valor de búsqueda del Entry
    valor_buscar = entry_busqueda.get()
    resultados = []

    # Iterar sobre las filas de la hoja de cálculo y buscar según el campo especificado
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if campo == "ID" and str(row[0]) == valor_buscar:
            resultados.append(row)
        elif campo == "Usuario" and row[1] == valor_buscar:
            resultados.append(row)
        elif campo == "Contraseña" and row[2] == valor_buscar:
            resultados.append(row)
        elif campo == "Email" and row[3] == valor_buscar:
            resultados.append(row)
        elif campo == "Fecha de Registro" and row[4] == valor_buscar:
            resultados.append(row)

    # Si se encuentran resultados, mostrarlos; de lo contrario, mostrar un mensaje de información
    if resultados:
        mostrar_resultados(resultados)
    else:
        messagebox.showinfo("Info", "Ningún resultado encontrado")

# Función para mostrar los resultados en el HTMLLabel
def mostrar_resultados(resultados):
    formatted_results = ""
    for resultado in resultados:
        formatted_result = f"<span style='font-size: 10px;'><b>ID:</b> {resultado[0]}, <b>Usuario:</b> {resultado[1]}, <b>Contraseña:</b> {resultado[2]}, <b>Email:</b> {resultado[3]}, <b>Fecha de Registro:</b> {resultado[4]}</span><br><br>"
        formatted_results += formatted_result

    # Establecer los resultados formateados en el HTMLLabel
    result_listbox.set_html(formatted_results)

# Crear la ventana principal y configurarla
window = tk.Tk()
window.title("Buscar Usuario")
window.geometry("800x300")

# Crear etiqueta y campo de entrada para el valor de búsqueda
label_busqueda = tk.Label(window, text="Valor de búsqueda:", font=("Arial", 12, "bold"))
label_busqueda.pack(pady=5)
entry_busqueda = tk.Entry(window, width=30)
entry_busqueda.pack()

# Crear un Frame para contener los botones de búsqueda
button_frame = tk.Frame(window)
button_frame.pack()

# Crear botones de búsqueda para cada campo
buscar_id_button = tk.Button(button_frame, text="Buscar por ID", command=buscar_id)
buscar_id_button.pack(side=tk.LEFT, padx=5, pady=5)
buscar_usuario_button = tk.Button(button_frame, text="Buscar por Usuario", command=buscar_usuario)
buscar_usuario_button.pack(side=tk.LEFT, padx=5, pady=5)
buscar_contraseña_button = tk.Button(button_frame, text="Buscar por Contraseña", command=buscar_contraseña)
buscar_contraseña_button.pack(side=tk.LEFT, padx=5, pady=5)
buscar_email_button = tk.Button(button_frame, text="Buscar por Email", command=buscar_email)
buscar_email_button.pack(side=tk.LEFT, padx=5, pady=5)
buscar_fecha_registro_button = tk.Button(button_frame, text="Buscar por Fecha de Registro", command=buscar_fecha_registro)
buscar_fecha_registro_button.pack(side=tk.LEFT, padx=5, pady=5)

# Crear un Frame contenedor para la barra de desplazamiento y el HTMLLabel
scrollable_frame = tk.Frame(window)
scrollable_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Crear el Canvas
canvas = tk.Canvas(scrollable_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Añadir la barra de desplazamiento
scrollbar = ttk.Scrollbar(scrollable_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Crear el HTMLLabel dentro del Canvas
result_listbox = HTMLLabel(canvas, width=3000, height=15)
result_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Configurar el Canvas para que expanda según sea necesario
canvas.create_window((0, 0), window=result_listbox, anchor="nw")
result_listbox.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Iniciar el bucle principal de la ventana
window.mainloop()
