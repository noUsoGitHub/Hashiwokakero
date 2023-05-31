from clases.structures import Nodo,Hashiwokakero
from clases.speedCommons import maths



# Carga basica:
hashi = Hashiwokakero()
hashi.convertir("test.txt")
print(hashi.information())
# FIN CARGA

hashi.resolver()


# Imprimimos la matriz resultante
'''
# Creamos una instancia de la clase Hashiwokakero y cargamos la matriz de nodos


while True:
    x1, y1, x2, y2 = map(int, input("Punto X1, Y1, X2, Y2: ").split())
    retorno= hashi.Matriz[x1][y1].conectar(hashi,hashi.Matriz[x2][y2],maths.calcular_direccion(x1,x2,y1,y2))
    import os
    os.system('cls')
    print(retorno)
    print(hashi.information())
    victoria =  hashi.verificar_victoria() 
    if victoria is True or victoria is None :
        exit()
        


#'''