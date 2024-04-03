import tkinter as tk

def letraDNI(dni):
    """
    Recibe el DNI en formato numérico
    """
    letras = "TRWAGMYFPDXBNJZSQVHLCKEO"
    valor = dni % 23
    return letras[valor]

def calcular_letra():
    try:
        dni = int(entry_dni.get())
        letra = letraDNI(dni)
        resultado_label.config(text=f"La letra del DNI {dni} es: {letra}")
    except ValueError:
        resultado_label.config(text="Por favor, ingrese un número válido.")

def validate_input(new_value):
    return new_value.isdigit() and len(new_value) <= 8

# Crear ventana
window = tk.Tk()
window.title("Calculadora de letra DNI")

# Configurar tamaño de la ventana
window.geometry("200x150")  # Anchura x Altura

# Crear y posicionar elementos
label_dni = tk.Label(window, text="Ingrese su DNI (máx. 8 dígitos):")
label_dni.pack()

validate_input_cmd = window.register(validate_input)
entry_dni = tk.Entry(window, validate="key", validatecommand=(validate_input_cmd, "%P"))
entry_dni.pack()

calcular_button = tk.Button(window, text="Calcular letra", command=calcular_letra)
calcular_button.pack()

resultado_label = tk.Label(window, text="")
resultado_label.pack()

# Ejecutar la ventana
window.mainloop()
