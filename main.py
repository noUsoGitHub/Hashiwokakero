from clases.structures import Nodo,Hashiwokakero
from clases.speedCommons import maths



# Carga basica:
hashi = Hashiwokakero()
hashi.convertir("Matrices/prueba.txt")
print(hashi.information())
# FIN CARGA




# Imprimimos la matriz resultante
#'''
# Creamos una instancia de la clase Hashiwokakero y cargamos la matriz de nodos


while True:
    x1, y1, x2, y2 = map(int, input("Punto X1, Y1, X2, Y2: \nEscribe -10 en todo para usar el solucionador automatico  ").split())
    if x1== -10 and x2 == -10 and y1 == -10 and y2 == -10:
        hashi.resolver()
    retorno= hashi.Matriz[x1][y1].conectar(hashi,hashi.Matriz[x2][y2],maths.calcular_direccion(x1,x2,y1,y2))
    import os
    os.system('cls')
    print(hashi.information())
    victoria =  hashi.verificar_victoria() 
    if victoria is True or victoria is None :
        exit()
        


#'''