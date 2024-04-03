from tkinter import Tk, Label, Button, Frame

proceso = 0

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def iniciar(contador=0):
    global proceso

    time['text'] = format_time(contador)

    proceso = root.after(1000, iniciar, (contador + 1))

def parar():
    global proceso
    root.after_cancel(proceso)

root = Tk()
root.title('Cronometro')

time = Label(root, fg='black', width=20, font=("", 18))
time.pack()

frame = Frame(root)
btnIniciar = Button(frame, fg='blue', text='Iniciar', command=iniciar)
btnIniciar.grid(row=1, column=1)
btnParar = Button(frame, fg='blue', text='Parar', command=parar)
btnParar.grid(row=1, column=2)
frame.pack()

root.mainloop()
