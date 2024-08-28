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

def seleccionar_alfabeto():
    print("#---------- Selección de Alfabeto ----------#")
    print("|[1] Alfabeto Inglés                        |")
    print("|[2] Alfabeto Español                       |")
    print("|[3] Definir tu propio alfabeto             |")
    print("#-------------------------------------------#")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif opcion == "2":
        return "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    elif opcion == "3":
        alfabeto_usuario = input("Ingrese el alfabeto que desea usar (sin espacios, caracteres únicos): ")
        return alfabeto_usuario.upper()
    else:
        print("Opción no válida. Usando alfabeto inglés por defecto.")
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def menu():
    while True:
        print("#---------- Cifrado César Afín ----------#")
        print("|[1] Cifrar un mensaje                   |")
        print("|[2] Descifrar un mensaje                |")
        print("|[3] Salir                               |")
        print("#----------------------------------------#")
        opcion = input("Seleccione una opción: ")
        
        if opcion in ["1", "2"]:
            alfabeto = seleccionar_alfabeto()
            
            if opcion == "1":
                print(          "#----------------------------------------#")
                mensaje = input("|Ingrese el mensaje a cifrar:            |").upper()
                print(          "#----------------------------------------#")
                a = int(input(  "|Ingrese el valor multiplicativo (a):    |"))
                b = int(input(  "|Ingrese el valor aditivo (b):           |"))
                print(          "#----------------------------------------#")
                
                try:
                    mensaje_cifrado = cifrado_afin(mensaje, a, b, alfabeto)
                    print(f"Mensaje cifrado: {mensaje_cifrado}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif opcion == "2":
                print(                "#----------------------------------------#")
                texto_cifrado = input("|Ingrese el mensaje a descifrar:         |").upper()
                print(                "#----------------------------------------#")
                a = int(input(        "|Ingrese el valor multiplicativo (a):    |"))
                b = int(input(        "|Ingrese el valor aditivo (b):           |"))
                print(                "#----------------------------------------#")
                try:
                    mensaje_descifrado = descifrado_afin(texto_cifrado, a, b, alfabeto)
                    print(f"Mensaje descifrado: {mensaje_descifrado}")
                except ValueError as e:
                    print(f"Error: {e}")
        
        elif opcion == "3":
            print("Adios")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

menu()


