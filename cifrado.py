cifrar     ={
            "a": "h", "b": "i", "c": "j",
            "d": "k", "e": "l", "f": "m",
            "g": "n", "h": "ñ", "i": "o",
            "j": "p", "k": "q", "l": "r",
            "m": "s", "n": "t", "ñ": "u",
            "o": "v", "p": "w", "q": "x",
            "r": "y", "s": "z", "t": "a",
            "u": "b", "v": "c", "w": "d",
            "x": "e", "y": "f", "z": "g",
            "_": " "
            }

descifrar   ={
            "h": "a", "i": "b", "j": "c",
            "k": "d", "l": "e", "m": "f",
            "n": "g", "ñ": "h", "o": "i",
            "p": "j", "q": "k", "r": "l",
            "s": "m", "t": "n", "u": "ñ",
            "v": "o", "w": "p", "x": "q",
            "y": "r", "z": "s", "a": "t",
            "b": "u", "c": "v", "d": "w",
            "e": "x", "f": "y", "g": "z",
            "_": " "
}

eleccion= int(input("Cifrado cesar clave 7: \n1)Cifrar\n2)Descifrar\n"))
caracter = ""

if eleccion == 1:
    msj= str(input("Frase a cifrar: "))
    msjList=list(msj.replace(" ", "_"))
    for i in msjList:
        caracter = caracter + cifrar[str(i)]

elif eleccion == 2:
    msj= str(input("Frase a decsifrar: "))
    msjList=list(msj.replace(" ", "_"))
    for i in msjList:
        caracter = caracter + descifrar[str(i)]

print(caracter)