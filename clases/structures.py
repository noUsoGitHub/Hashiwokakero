
class Nodo:
    def __init__(self, dato,x=0,y=0):
        self.Dato = dato
        self.Direcciones= [0,0,0,0]#Arriba-Derecha-Abajo-Izquierda
        self.Puentes = 0
        self.X=x
        self.Y=y
        self.Full=False
        self.conexiones = []
        
    def information(self):
        return f"Nodo : {self.Dato} \nDirecciones: {self.Direcciones} \nPuentes: {self.Puentes} \nConexiones: {[n.Dato for n in self.conexiones]}\nX :{self.X}\nY :{self.Y}"
    
    def conectar(self, Hashiwokakero, Nodo, Dir, Cantidad=1):
        print("Recibi:")
        print(self.information())
        print(Nodo.information())
        if isinstance(self.Dato, int):
            if isinstance(Nodo.Dato, int):
                if self.X != Nodo.X and self.Y != Nodo.Y:
                    return -1  # Los puntos no están en la misma fila o columna.
                if not Hashiwokakero.verificar_camino(Nodo.X, Nodo.Y, self.X, self.Y):
                    return -2  # Camino bloqueado.
                if self.Direcciones[Dir] == 2:
                    return -3  # Máximo de puentes en el punto de origen.
                if Nodo.Direcciones[(Dir + 2) % 4] == 2:
                    return -4  # Máximo de puentes en el punto de destino.

                if self.Puentes + Cantidad <= self.Dato:
                    if Nodo.Puentes + Cantidad <= Nodo.Dato:
                        self.Puentes += Cantidad
                        self.Direcciones[Dir] += 1
                        Nodo.Puentes += Cantidad
                        Nodo.Direcciones[(Dir + 2) % 4] += 1
                        self.conectar_nodo(Nodo)
                        Nodo.conectar_nodo(self)
                        Hashiwokakero.formar_camino(Nodo.X, Nodo.Y, self.X, self.Y)
                        if Nodo.Puentes == Nodo.Dato:
                            Nodo.Full = True
                        if self.Puentes == self.Dato:
                            self.Full = True
                        return 1  # Islas conectadas.
                    else:
                        return -4  # Máximo de puentes en el punto de destino.
                else:
                    return -3  # Máximo de puentes en el punto de origen.
            else:
                return -5  # Selecciona una isla objetivo válida.
        else:
            return -6  # No seleccionaste una isla inicial válida.
    def conectar_nodo(self, Nodo):
            if Nodo not in self.conexiones:
                self.conexiones.append(Nodo)

class Solicitud:
    def __init__(self):
        self.x1=-1
        self.x2=-1
        self.y1=-1
        self.y2=-1
    def validate(self):
        if self.x1 == -1 or self.x2 == -1 or self.y1 == -1 or self.y2 == -1:
            return False
        return True
    def empty(self):
        self.x1 = -1
        self.x2 = -1
        self.y1 = -1
        self.y2 = -1
class Hashiwokakero:
    def __init__(self):
        self.Matriz = []
        self.created =False
    def verificar_victoria(self):
        for i in range(len(self.Matriz)):
            for j in range(len((self.Matriz))):
                if isinstance(self.Matriz[i][j].Dato, int):
                    if not self.Matriz[i][j].Full:
                        return False
        return True
    def verificar_camino(self, x1, y1, x2, y2):
        # Verificar que no haya nada en el camino
        if x1 == x2:
            for j in range(min(y1, y2)+1, max(y1, y2)):
                if isinstance(self.Matriz[x1][j].Dato,int):
                    return False
        elif y1 == y2:
            for i in range(min(x1, x2)+1, max(x1, x2)):
                if isinstance(self.Matriz[i][y1].Dato ,int ):
                    return False
        return True
    def formar_camino(self, x1, y1, x2, y2):
        # Forma camino en los nodos
        if x1 == x2:
            for j in range(min(y1, y2)+1, max(y1, y2)):
                if self.Matriz[x1][j].Dato == " ":
                    self.Matriz[x1][j].Dato = "-"
                elif self.Matriz[x1][j].Dato == "-":
                    self.Matriz[x1][j].Dato = "="
        elif y1 == y2:
            for i in range(min(x1, x2)+1, max(x1, x2)):
                if self.Matriz[i][y1].Dato == " ":
                    self.Matriz[i][y1].Dato = "|"
                elif self.Matriz[i][y1].Dato =="|":
                    self.Matriz[i][y1].Dato = "||"
    def information(self):
        data=""
        for i in self.Matriz:
            for j in i:
                data+= f"{j.Dato} ({j.X},{j.Y})\t"
            data+="\n"
        print(len(self.Matriz))
        return data
    def convertir(self, archivo):
        self.Matriz=[]
        with open(archivo) as f:
            lineas = f.readlines()

        for linea in lineas[1:]:
            lista = []
            fila = list(map(int, linea.strip().split()))
            for element in fila:
                lista.append(Nodo(element))
                lista.append(Nodo(0))
            self.Matriz.append(lista)
            self.Matriz.append([Nodo(0) for _ in range(len(fila)*2)])

        for i in range(len(self.Matriz)):
            for j in range(len((self.Matriz))):
                self.Matriz[i][j].X=i
                self.Matriz[i][j].Y=j
                if self.Matriz[i][j].Dato == 0:
                    self.Matriz[i][j].Dato = " "