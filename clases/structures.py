class Nodo:
    def __init__(self, dato):
        self.Dato = dato
        self.Direcciones= [0,0,0,0]#Arriba-Derecha-Abajo-Izquierda
        self.Puentes = 0
    def information(self):
        return f"Nodo : {self.Dato} \nDirecciones: {self.Direcciones} \nPuentes: {self.Puentes}"
    def conectar(self,Nodo,Dir,Cantidad):
        if self.Direcciones[Dir] or Nodo.Direcciones[(Dir+2)%4]:
            return -2
        if self.Puentes+Cantidad<self.Dato:
            if Nodo.Puentes+Cantidad<Nodo.Dato:
                self.Puentes+=Cantidad
                self.Direcciones[Dir]=1
                Nodo.Puentes+=Cantidad
                Nodo.Direcciones[((Dir+2) % 4 )] = 1
                return 1
            else:
                return -1

        else:
            return -1
class Hashiwokakero:
    def __init__(self):
        self.Matriz = []
    def information(self):
        data=""
        for i in self.Matriz:
            for j in i:
                data+= str(j.Dato) +" "
            data+="\n"
        return data
    def convertir(self, archivo):
        with open(archivo) as f:
            lineas = f.readlines()
        
        for linea in lineas[1:]:
            lista=[]
            fila = list(map(int, linea.strip().split()))
            for element in fila:
                print(element)
                lista.append(Nodo(element))
            self.Matriz.append(lista)

