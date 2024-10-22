texto = "Hola Mundo"
print(texto.upper())
print(texto.lower())
print(texto.find("Mun"))
nuevoTexto = texto.replace("Mun", "chanchito feliz")
print(texto, nuevoTexto)
print("Mundo" in texto)
descripcion = """metodos de string"""
nombre = "Ariel"
apellido = "Rivas"
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)
#para borrar espacios en blanco y ponerlo en Chn sfsfs
texto.strip().capitalize()
texto.lstrip() #izquierda
texto.rstrip() #derecha
curso = "Ultimate \"Python\""
print(curso)
curso = "Ultimate \nPython\""
print(curso)