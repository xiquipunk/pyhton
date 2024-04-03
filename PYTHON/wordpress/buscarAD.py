import tkinter as tk
from tkinter import messagebox, ttk
import openpyxl
from tkhtmlview import HTMLLabel

# Variable global para almacenar el campo de orden y la dirección de orden
campo_orden = "ID"
orden_ascendente = True

# Función para cambiar la dirección de orden de búsqueda y ejecutar la búsqueda correspondiente
def cambiar_direccion_orden(campo):
    global campo_orden, orden_ascendente
    if campo_orden != campo:
        # Si se cambia el campo de orden, por defecto ordenar de forma ascendente
        orden_ascendente = True
    else:
        # Si se mantiene el mismo campo de orden, cambiar la dirección de orden
        orden_ascendente = not orden_ascendente
    campo_orden = campo
    # Ejecutar la búsqueda después de cambiar la dirección de orden
    buscar_por_campo(campo_orden)
    # Actualizar las etiquetas de los botones ascendentes y descendentes
    actualizar_etiqueta_botones()

# Función para buscar por un campo específico
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
    # Ordenar los resultados según la dirección de orden
    resultados_ordenados = sorted(resultados, key=lambda x: x[0], reverse=not orden_ascendente)

    formatted_results = ""
    for resultado in resultados_ordenados:
        formatted_result = f"<span style='font-size: 10px;'><b>ID:</b> {resultado[0]}, <b>Usuario:</b> {resultado[1]}, <b>Contraseña:</b> {resultado[2]}, <b>Email:</b> {resultado[3]}, <b>Fecha de Registro:</b> {resultado[4]}</span><br><br>"
        formatted_results += formatted_result

    # Establecer los resultados formateados en el HTMLLabel
    result_listbox.set_html(formatted_results)

# Función para actualizar las etiquetas de los botones ascendentes y descendentes
def actualizar_etiqueta_botones():
    # Obtener el texto de las flechas
    ascendente_texto = "\u25B2" if orden_ascendente else ""
    descendente_texto = "\u25BC" if not orden_ascendente else ""
    
    # Actualizar las etiquetas de los botones
    buscar_ascendente_button.config(text=f"Ascendente {ascendente_texto}")
    buscar_descendente_button.config(text=f"Descendente {descendente_texto}")

# Función para ordenar ascendente
def ordenar_ascendente():
    cambiar_direccion_orden(campo_orden)

# Función para ordenar descendente
def ordenar_descendente():
    cambiar_direccion_orden(campo_orden)

# Crear la ventana principal y configurarla
window = tk.Tk()
window.title("Buscar Usuario")
window.geometry("800x300")

# Crear etiqueta y campo de entrada para el valor de búsqueda
label_busqueda = tk.Label(window, text="Valor de búsqueda:", font=("Arial", 12, "bold"))
label_busqueda.pack(pady=5)
entry_busqueda = tk.Entry(window, width=30)
entry_busqueda.pack()

# Crear un Frame para contener los botones de búsqueda y orden
button_frame = tk.Frame(window)
button_frame.pack()

# Crear botones de búsqueda para cada campo
buscar_id_button = tk.Button(button_frame, text="Buscar por ID", command=lambda: cambiar_direccion_orden("ID"))
buscar_id_button.pack(side=tk.LEFT, padx=5, pady=5)
buscar_usuario_button = tk.Button(button_frame, text="Buscar por Usuario", command=lambda: cambiar_direccion_orden("Usuario"))
buscar_usuario_button.pack(side=tk.LEFT, padx=5, pady=5)
buscar_contraseña_button = tk.Button(button_frame, text="Buscar por Contraseña", command=lambda: cambiar_direccion_orden("Contraseña"))
buscar_contraseña_button.pack(side=tk.LEFT, padx=5, pady=5)
buscar_email_button = tk.Button(button_frame, text="Buscar por Email", command=lambda: cambiar_direccion_orden("Email"))
buscar_email_button.pack(side=tk.LEFT, padx=5, pady=5)
buscar_fecha_registro_button = tk.Button(button_frame, text="Buscar por Fecha de Registro", command=lambda: cambiar_direccion_orden("Fecha de Registro"))
buscar_fecha_registro_button.pack(side=tk.LEFT, padx=5, pady=5)

# Crear botones para ordenar ascendente y descendente
orden_button_frame = tk.Frame(window)
orden_button_frame.pack()
buscar_ascendente_button = tk.Button(orden_button_frame, text="Ascendente", command=ordenar_ascendente)
buscar_ascendente_button.pack(side=tk.LEFT, padx=5, pady=5)
buscar_descendente_button = tk.Button(orden_button_frame, text="Descendente", command=ordenar_descendente)
buscar_descendente_button.pack(side=tk.LEFT, padx=5, pady=5)

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
