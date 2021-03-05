#!/usr/bin/#!/usr/bin/env python3
import os
import numpy as np

def KSA(llave):
    longitud_llave = len(llave)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + llave[i%longitud_llave]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S,n):
    i = 0
    j = 0
    llave = []

    while n>0:
        n = n - 1
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[ (S[i] + S[j]) % 256 ]
        llave.append(K)
    return llave
def llave_to_array(llave):
    return [ord(c) for c in llave]

def leer_archivo(file):
    with open(file,'r') as f:
        fr = f.read()
    return fr
def sobreescribir_archivo(file, mensaje):
    with open(file, 'w') as f:
        fw = f.write(mensaje)
def encriptar():
    llave = input("Ingrese clave generadora: ")
    archivo = input("Ingrese el nombre del archivo: ")

    texto = leer_archivo(archivo)
    llave = llave_to_array(llave)

    S = KSA(llave)
    cadena_cifrante = np.array(PRGA(S, len(texto)))
    print("\nKeystream:")
    print(cadena_cifrante)

    texto = np.array([ord(i) for i in texto])
    cipher = cadena_cifrante ^ texto #XOR dos arrays
    print(cipher)

    print("\nHexadecimal:")
    print(cipher.astype(np.uint8).data.hex()) #imprime en hexadecimal
    print("\nUnicode:")
    print([chr(c) for c in cipher]) #print unicode

    sobreescribir_archivo(archivo,cipher.astype(np.uint8).data.hex())


def desencriptar():
    llave = input("Ingrese clave generadora: ")
    archivo = input("Ingrese el nombre del archivo: ")
    texto = leer_archivo(archivo)
    llave = llave_to_array(llave)

    S = KSA(llave)
    cadena_cifrante = np.array(PRGA(S, len(texto)//2))
    print("\nKeystream:")
    print(cadena_cifrante)

    hex_list = [texto[i:i+2] for i in range(0, len(texto), 2)]
    texto2 = np.array([int(i,16) for i in hex_list])

    decipher = cadena_cifrante ^ texto2
    print("\nHexadecimal:")
    print(texto) #imprime en hexadecimal
    print("\nUnicode:")
    print([chr(c) for c in decipher]) #print unicode

    sobreescribir_archivo(archivo,"".join([chr(c) for c in decipher]))




def main():

    while True:
        #os.system("cls")
        print("####################")
        print("#### Cipher RC4 ####")
        print("####################\n")
        print("[1] Encriptar")
        print("[2] Desencriptar")
        print("[3] Salir")
        seleccion = input("\nIngrese la opción deseada: ")

        if seleccion == str(1):
            encriptar()

        elif seleccion == str(2):
            desencriptar()

        elif seleccion == str(3):
            break



if __name__ == '__main__':
    main()
