import tkinter as tk
import re

def validar_longitud(cadena, limite):
    return len(cadena) <= limite

def validar_datos():
    usuario = entry_usuario.get()
    pass1 = entry_pass1.get()
    pass2 = entry_pass2.get()
    email = entry_email.get()

    if not validar_longitud(usuario, 10):
        resultado_label.config(text="La longitud del nombre de usuario debe ser 10 caracteres", fg="red")
    elif not validar_longitud(pass1, 8) or not validar_longitud(pass2, 8):
        resultado_label.config(text="La longitud de la contraseña debe ser 8 caracteres", fg="red")
    elif not re.search('[0-9]', pass1) or pass1 != pass2:
        resultado_label.config(text="La contraseña es incorrecta", fg="red")
    elif not validar_longitud(email, 15) or not re.search('@', email):
        resultado_label.config(text="El email es incorrecto", fg="red")
    else:
        resultado_label.config(text="Datos Correctos", fg="green")

# Crear ventana
window = tk.Tk()
window.title("Formulario de Registro")
window.geometry("420x250")

# Estilo
bg_color = "#f0f0f0"
entry_bg_color = "white"
button_bg_color = "#4CAF50"
button_fg_color = "white"

from tkinter import font

# Crear una fuente en negrita
bold_font = font.Font(weight="bold")

# Crear y posicionar elementos
label_usuario = tk.Label(window, text="Nombre de usuario:", bg=bg_color, font=bold_font)
label_usuario.grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_usuario = tk.Entry(window, bg=entry_bg_color, width=25)
entry_usuario.grid(row=0, column=1, padx=10, pady=5)

label_pass1 = tk.Label(window, text="Contraseña:", bg=bg_color, font=bold_font)
label_pass1.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_pass1 = tk.Entry(window, show="*", bg=entry_bg_color, width=25)
entry_pass1.grid(row=1, column=1, padx=10, pady=5)

label_pass2 = tk.Label(window, text="Repite contraseña:", bg=bg_color, font=bold_font)
label_pass2.grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_pass2 = tk.Entry(window, show="*", bg=entry_bg_color, width=25)
entry_pass2.grid(row=2, column=1, padx=10, pady=5)

label_email = tk.Label(window, text="E-mail:", bg=bg_color, font=bold_font)
label_email.grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_email = tk.Entry(window, bg=entry_bg_color, width=25)
entry_email.grid(row=3, column=1, padx=10, pady=5)

# Limitar la longitud de los campos de entrada
entry_usuario.config(validate="key", validatecommand=(window.register(lambda text: validar_longitud(text, 10)), "%P"))
entry_pass1.config(validate="key", validatecommand=(window.register(lambda text: validar_longitud(text, 8)), "%P"))
entry_pass2.config(validate="key", validatecommand=(window.register(lambda text: validar_longitud(text, 8)), "%P"))
entry_email.config(validate="key", validatecommand=(window.register(lambda text: validar_longitud(text, 25)), "%P"))

validar_button = tk.Button(window, text="Validar Datos", command=validar_datos, bg=button_bg_color, fg=button_fg_color)
validar_button.grid(row=4, columnspan=2, pady=10)

resultado_label = tk.Label(window, text="", bg=bg_color)
resultado_label.grid(row=5, columnspan=2, pady=5)

# Ejecutar la ventana
window.mainloop()
