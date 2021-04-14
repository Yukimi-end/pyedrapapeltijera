
from tkinter import *
import random

root = Tk()
root.title("Piedra, papel o tijera")
root.geometry("555x750")


piedra_img = PhotoImage(file="piedra.gif").subsample(5, 5)
papel_img = PhotoImage(file="papel.gif").subsample(5, 5)
tijera_img = PhotoImage(file="tijera.gif").subsample(5, 5)
seleccion = PhotoImage(file="volteado.gif").subsample(5, 5)


top = Frame(root)
top.pack(side=TOP)
bottom = Frame(root)
bottom.pack(side=BOTTOM)


def es_papel():
    computadora = random.choice(elementos)
    if computadora == "papel":
        computadora_label.configure(image=papel_img)
        usuario_elige.set("Empate.\nTú: PAPEL - Computadora: PAPEL")
    elif computadora == "piedra":
        computadora_label.configure(image=piedra_img)
        usuario_elige.set("Ganaste.\nTú: PAPEL - Computadora: PIEDRA")
        gano_usuario.set(gano_usuario.get() + 1)
    elif computadora == "tijera":
        computadora_label.configure(image=tijera_img)
        usuario_elige.set("Perdiste.\nTú: PAPEL - Computadora: TIJERA")
        gano_computadora.set(gano_computadora.get() + 1)
    resultado_acumulado.set(f"Tú: {str(gano_usuario.get())}\nComputadora: {str(gano_computadora.get())}")

def es_piedra():
    computadora = random.choice(elementos)
    if computadora == "papel":
        computadora_label.configure(image=papel_img)
        usuario_elige.set("Perdiste.\nTú: PIEDRA - Computadora: PAPEL")
        gano_computadora.set(gano_computadora.get() + 1)
    elif computadora == "piedra":
        computadora_label.configure(image=piedra_img)
        usuario_elige.set("Empate.\nTú: PIEDRA - Computadora: PIEDRA")
    elif computadora == "tijera":
        computadora_label.configure(image=tijera_img)
        usuario_elige.set("Ganaste.\nTú: PIEDRA - Computadora: TIJERA")
        gano_usuario.set(gano_usuario.get() + 1)
    resultado_acumulado.set(f"Tú: {str(gano_usuario.get())}\nComputadora: {str(gano_computadora.get())}")

def es_tijera():
    computadora = random.choice(elementos)
    if computadora == "papel":
        computadora_label.configure(image=papel_img)
        usuario_elige.set("Ganaste.\nTú: TIJERA - Computadora: PAPEL")
        gano_usuario.set(gano_usuario.get() + 1)
    elif computadora == "piedra":
        computadora_label.configure(image=piedra_img)
        usuario_elige.set("Perdiste.\nTú: TIJERA - Computadora: PIEDRA")
        gano_computadora.set(gano_computadora.get() + 1)
    elif computadora == "tijera":
        usuario_elige.set("Empate.\nTú: TIJERA - Computadora: TIJERA")
        computadora_label.configure(image=tijera_img)
    resultado_acumulado.set(f"Tú: {str(gano_usuario.get())}\nComputadora: {str(gano_computadora.get())}")


usuario_elige = StringVar(value="\n\n")
gano_usuario = IntVar()
gano_usuario.set(0)
gano_computadora = IntVar()
gano_computadora.set(0)

elementos = ["piedra", "papel", "tijera"]


titulo = Label(top, text='Piedra, papel o tijera', font=('Verdana', 14))
computadora_elige_label = Label(top, text='Computadora elige:', font=('Verdana', 11))
computadora_label = Label(top, image=seleccion)

tu_eliges = Label(top, text='Tú eliges:', font=('Verdana', 11))
papel_boton = Button(top, image=papel_img, command=es_papel)
piedra_boton = Button(top, image=piedra_img, command=es_piedra)
tijera_boton = Button(top, image=tijera_img, command=es_tijera)


titulo.pack(side=TOP, pady=5)
computadora_elige_label.pack(side=TOP, pady=5)
computadora_label.pack(side=TOP, pady=5)


tu_eliges.pack(side=TOP, pady=7)
papel_boton.pack(side=LEFT, padx=10)
piedra_boton.pack(side=LEFT, padx=10)
tijera_boton.pack(side=LEFT, padx=10)


resultado = Label(bottom, textvariable=usuario_elige, font=('Verdana', 11))
resultado.pack(side=TOP, pady=5)

resultado_acumulado = StringVar()
resultado_acumulado.set("Tú: 0\nComputadora: 0")

acumulado = Label(bottom, textvariable=resultado_acumulado, font=('Verdana', 11))
acumulado.pack(side=TOP, pady=5)


def reinicio():
    gano_usuario.set(0)
    gano_computadora.set(0)
    computadora_label.configure(image=seleccion)
    usuario_elige.set("")
    resultado_acumulado.set("")


reiniciar = Button(bottom, text="Reiniciar", command=reinicio)
reiniciar.pack(side=TOP, pady=10)


root.mainloop()

