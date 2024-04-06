#datos compuestos

#creando una lista (se pueden modificar)
lista = ["Lionel Andres","Messi",True,1.79]

#creando una tupla (no se pueden modificar)
tupla = ("Lionel Andres","Messi",True,1.79) 

#valido
lista[2] = False

#no valido
#tupla[1] = "Ronaldo" 

#creando un conjunto (set) - (no se accede a elementos por índice, no almacena datos duplicados)
conjunto = {"Lionel Andres","Messi",True,1.79}
print(conjunto)

#crando un diccionario (dict) - (key : value)
diccionario= {
    "nombre": "Agustin",
    "apellido": "Ceballos",
    "altura": 179
}

