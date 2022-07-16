
import tkinter as tk
import random
import time

root = tk.Tk()
root.title("Piedra, papel o tijera")
root.geometry("555x720")


piedra_img = tk.PhotoImage(file="piedra.gif").subsample(5, 5)
papel_img = tk.PhotoImage(file="papel.gif").subsample(5, 5)
tijera_img = tk.PhotoImage(file="tijera.gif").subsample(5, 5)
seleccion = tk.PhotoImage(file="volteado.gif").subsample(5, 5)


top = tk.Frame(root)
top.pack(side=tk.TOP)
bottom = tk.Frame(root)
bottom.pack(side=tk.BOTTOM)


ganaste = "Ganaste"
empate = "Empate"
perdiste = "Perdiste"


def regresar():
    computadora_label.configure(image=seleccion)


def es_papel():
    computadora = random.choice(elementos)
    if computadora == "papel":
        computadora_label.configure(image=papel_img)
        usuario_elige.set(f"{empate}")
    elif computadora == "piedra":
        computadora_label.configure(image=piedra_img)
        usuario_elige.set(f"{ganaste}")
        gano_usuario.set(gano_usuario.get() + 1)
    elif computadora == "tijera":
        computadora_label.configure(image=tijera_img)
        usuario_elige.set(f"{perdiste}")
        gano_computadora.set(gano_computadora.get() + 1)
    resultado_acumulado.set(f"Tú: {str(gano_usuario.get())}\nComputadora: {str(gano_computadora.get())}")
    root.after(2000, regresar)


def es_piedra():
    computadora = random.choice(elementos)
    if computadora == "papel":
        computadora_label.configure(image=papel_img)
        usuario_elige.set(f"{perdiste}")
        gano_computadora.set(gano_computadora.get() + 1)
    elif computadora == "piedra":
        computadora_label.configure(image=piedra_img)
        usuario_elige.set(f"{empate}")
    elif computadora == "tijera":
        computadora_label.configure(image=tijera_img)
        usuario_elige.set(f"{ganaste}")
        gano_usuario.set(gano_usuario.get() + 1)
    resultado_acumulado.set(f"Tú: {str(gano_usuario.get())}\nComputadora: {str(gano_computadora.get())}")
    root.after(2000, regresar)


def es_tijera():
    computadora = random.choice(elementos)
    if computadora == "papel":
        computadora_label.configure(image=papel_img)
        usuario_elige.set(f"{ganaste}")
        gano_usuario.set(gano_usuario.get() + 1)
    elif computadora == "piedra":
        computadora_label.configure(image=piedra_img)
        usuario_elige.set(f"{perdiste}")
        gano_computadora.set(gano_computadora.get() + 1)
    elif computadora == "tijera":
        computadora_label.configure(image=tijera_img)
        usuario_elige.set(f"{empate}")
    resultado_acumulado.set(f"Tú: {str(gano_usuario.get())}\nComputadora: {str(gano_computadora.get())}")
    root.after(2000, regresar)


def reinicio():
    gano_usuario.set(0)
    gano_computadora.set(0)
    computadora_label.configure(image=seleccion)
    usuario_elige.set("")
    resultado_acumulado.set("")


usuario_elige = tk.StringVar(value="\n\n")
gano_usuario = tk.IntVar()
gano_usuario.set(0)
gano_computadora = tk.IntVar()
gano_computadora.set(0)

elementos = ["piedra", "papel", "tijera"]

titulo = tk.Label(top, text='Piedra, papel o tijera', font=('Consolas', 13))
computadora_elige_label = tk.Label(top, text='Computadora elige:', font=('Consolas', 11))
computadora_label = tk.Label(top, image=seleccion)

tu_eliges = tk.Label(top, text='Tú eliges:', font=('Consolas', 11))
papel_boton = tk.Button(top, image=papel_img, command=es_papel)
piedra_boton = tk.Button(top, image=piedra_img, command=es_piedra)
tijera_boton = tk.Button(top, image=tijera_img, command=es_tijera)

resultado = tk.Label(bottom, textvariable=usuario_elige, font=('Consolas', 17))
resultado_acumulado = tk.StringVar()
resultado_acumulado.set("Tú: 0\nComputadora: 0")
acumulado = tk.Label(bottom, textvariable=resultado_acumulado, font=('Consolas', 8))

reiniciar = tk.Button(bottom, text="Reiniciar", command=reinicio)


titulo.pack(side=tk.TOP, pady=5)
computadora_elige_label.pack(side=tk.TOP, pady=5)
computadora_label.pack(side=tk.TOP, pady=5)

tu_eliges.pack(side=tk.TOP, pady=7)
papel_boton.pack(side=tk.LEFT, padx=3)
piedra_boton.pack(side=tk.LEFT, padx=3)
tijera_boton.pack(side=tk.LEFT, padx=3)

resultado.pack(side=tk.TOP)
acumulado.pack(side=tk.TOP, pady=5)

reiniciar.pack(side=tk.TOP, pady=10)


root.mainloop()
