from clases.structures import Nodo,Hashiwokakero
from clases.speedCommons import maths


# Creamos una instancia de la clase Hashiwokakero y cargamos la matriz de nodos
hashi = Hashiwokakero()
hashi.convertir("test.txt")

# Imprimimos la matriz resultante
print(hashi.information())
while True:
    x1 = int(input("Punto X1: "))
    y1 = int(input("Punto Y1: "))
    x2 = int(input("Punto X2: "))
    y2 = int(input("Punto Y2: "))
    retorno= hashi.Matriz[x1][y1].conectar(hashi,hashi.Matriz[x2][y2],maths.calcular_direccion(x1,x2,y1,y2))
    import os
    os.system('cls')
    print(retorno)
    print(hashi.information())
    if hashi.verificar_victoria():
        print("Ganaste!!!!")
        exit()

        