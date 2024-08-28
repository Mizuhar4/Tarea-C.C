import tkinter as tk
from tkinter import messagebox

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def inverso_modular(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def cifrado_afin(texto, a, b, alfabeto):
    resultado = []
    m = len(alfabeto)
    
    if mcd(a, m) != 1:
        raise ValueError("El valor de 'a' debe ser coprimo con el tamaño del alfabeto.")
    
    for caracter in texto:
        if caracter in alfabeto:
            indice = alfabeto.index(caracter)
            nuevo_indice = (a * indice + b) % m
            resultado.append(alfabeto[nuevo_indice])
        else:
            resultado.append(caracter)
    
    return ''.join(resultado)

def descifrado_afin(texto_cifrado, a, b, alfabeto):
    resultado = []
    m = len(alfabeto)
    a_inv = inverso_modular(a, m)
    
    if a_inv is None:
        raise ValueError("No existe un inverso multiplicativo para 'a' con el alfabeto dado.")
    
    for caracter in texto_cifrado:
        if caracter in alfabeto:
            indice = alfabeto.index(caracter)
            nuevo_indice = (a_inv * (indice - b)) % m
            resultado.append(alfabeto[nuevo_indice])
        else:
            resultado.append(caracter)
    
    return ''.join(resultado)

def seleccionar_alfabeto(opcion):
    if opcion == "Inglés":
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif opcion == "Español":
        return "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    elif opcion == "Usuario":
        alfabeto_usuario = alfabeto_entry.get().upper()
        return alfabeto_usuario
    else:
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cifrar_mensaje():
    try:
        alfabeto = seleccionar_alfabeto(alfabeto_var.get())
        mensaje = mensaje_entry.get().upper()
        a = int(a_entry.get())
        b = int(b_entry.get())
        
        mensaje_cifrado = cifrado_afin(mensaje, a, b, alfabeto)
        resultado_label.config(text=f"Mensaje cifrado: {mensaje_cifrado}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def descifrar_mensaje():
    try:
        alfabeto = seleccionar_alfabeto(alfabeto_var.get())
        texto_cifrado = mensaje_entry.get().upper()
        a = int(a_entry.get())
        b = int(b_entry.get())
        
        mensaje_descifrado = descifrado_afin(texto_cifrado, a, b, alfabeto)
        resultado_label.config(text=f"Mensaje descifrado: {mensaje_descifrado}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Cifrado César Afín")
root.geometry("600x600")  
alfabeto_var = tk.StringVar(value="Inglés")

alfabeto_label = tk.Label(root, text="Selecciona el alfabeto:")
alfabeto_label.pack(pady=10)

alfabeto_menu = tk.OptionMenu(root, alfabeto_var, "Inglés", "Español", "Usuario")
alfabeto_menu.pack(pady=5)

alfabeto_entry = tk.Entry(root)
alfabeto_entry.pack(pady=5)
alfabeto_entry.insert(0, "Ingrese alfabeto si selecciona 'Usuario'")

mensaje_label = tk.Label(root, text="Ingrese el mensaje:")
mensaje_label.pack(pady=10)
mensaje_entry = tk.Entry(root)
mensaje_entry.pack(pady=5)

a_label = tk.Label(root, text="Ingrese el valor multiplicativo (a):")
a_label.pack(pady=10)
a_entry = tk.Entry(root)
a_entry.pack(pady=5)

b_label = tk.Label(root, text="Ingrese el valor aditivo (b):")
b_label.pack(pady=10)
b_entry = tk.Entry(root)
b_entry.pack(pady=5)

cifrar_button = tk.Button(root, text="Cifrar", command=cifrar_mensaje)
cifrar_button.pack(pady=10)

descifrar_button = tk.Button(root, text="Descifrar", command=descifrar_mensaje)
descifrar_button.pack(pady=10)

resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=20)

root.mainloop()

