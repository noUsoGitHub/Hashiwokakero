from collections import deque
class Nodo:
    def __init__(self, dato,x=0,y=0):
        self.Dato = dato
        self.Direcciones= [0,0,0,0]#Arriba-Derecha-Abajo-Izquierda
        self.Puentes = 0
        self.X=x
        self.Y=y
        self.Full=False
        
    def information(self):
        dato_color = '\033[30m'  # Pred
        if self.Dato == '-' or self.Dato == '|':
            dato_color = '\033[32m'  # verde
        elif self.Dato == '=' or self.Dato == '||':
            dato_color = '\033[31m'  # rojo

        reset_color = '\033[0m'  # resetear el color a predeterminado

        return "Nodo: {}{}\nDirecciones: {}\nPuentes: {}\nConexiones: {}\nX: {}\nY: {}{}".format(dato_color, self.Dato, self.Direcciones, self.Puentes, self.X, self.Y)


    def conectar(self, Hashiwokakero, Nodo, Dir, Cantidad=1):
        if not isinstance(self.Dato, int):
            return -6  # No seleccionaste una isla inicial válida.
        
        if not isinstance(Nodo.Dato, int):
            return -5  # Selecciona una isla objetivo válida.
        
        if self.X != Nodo.X and self.Y != Nodo.Y:
            return -1  # Los puntos no están en la misma fila o columna.
        
        if not Hashiwokakero.verificar_camino(Nodo.X, Nodo.Y, self.X, self.Y):
            return -2  # Camino bloqueado.
        print(self.Puentes,Cantidad,self.Dato,self.Direcciones[Dir])
        if self.Puentes + Cantidad > self.Dato or self.Direcciones[Dir] >2: 
            return -3  # Máximo de puentes en el punto de origen.
        
        if Nodo.Puentes + Cantidad > Nodo.Dato or  Nodo.Direcciones[(Dir + 2) % 4] >2:
            return -4  # Máximo de puentes en el punto de destino.
        
        self.Puentes += Cantidad
        self.Direcciones[Dir] += 1
        Nodo.Puentes += Cantidad
        Nodo.Direcciones[(Dir + 2) % 4] += 1
        Hashiwokakero.formar_camino(Nodo.X, Nodo.Y, self.X, self.Y)
        
        if Nodo.Puentes == Nodo.Dato:
            Nodo.Full = True
        
        if self.Puentes == self.Dato:
            self.Full = True
        
        return 1  # Islas conectadas.
    def desconectar(self, Hashiwokakero, Nodo, Dir, Cantidad=1):
        if not isinstance(self.Dato, int):
            return -6  # No seleccionaste una isla inicial válida.

        if not isinstance(Nodo.Dato, int):
            return -5  # Selecciona una isla objetivo válida.

        if self.X != Nodo.X and self.Y != Nodo.Y:
            return -1  # Los puntos no están en la misma fila o columna.

        if self.Direcciones[Dir] == 0 or Nodo.Direcciones[(Dir + 2) % 4] == 0:
            return -7  # No hay puentes para desconectar en el punto de origen o destino.

        self.Puentes -= Cantidad
        self.Direcciones[Dir] -= 1
        Nodo.Puentes -= Cantidad
        Nodo.Direcciones[(Dir + 2) % 4] -= 1
        Hashiwokakero.eliminar_camino(Nodo.X, Nodo.Y, self.X, self.Y)

        if Nodo.Puentes < Nodo.Dato:
            Nodo.Full = False

        if self.Puentes < self.Dato:
            self.Full = False

        return 1  # Islas desconectadas.
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
        self.visitados = []

    def verificar_victoria(self):
        for i in range(len(self.Matriz)):
            for j in range(len((self.Matriz))):
                if isinstance(self.Matriz[i][j].Dato, int):
                    if not self.Matriz[i][j].Full:
                        return False
        if(self.verificar_conexion() is False):
            return None
        return True
    def verificar_conexion(self):
        # Inicializar todos los nodos como no visitados
        visitado = [[False for _ in range(len(self.Matriz[0]))] for _ in range(len(self.Matriz))]

        # Encontrar el primer nodo no vacío para comenzar la búsqueda
        inicio = None
        for i in range(len(self.Matriz)):
            for j in range(len(self.Matriz[0])):
                if isinstance(self.Matriz[i][j].Dato, int):
                    inicio = (i, j)
                    break
            if inicio:
                break

        # Si no se encuentra ningún nodo inicial, se considera que todos los nodos están conectados
        if not inicio:
            print("Todos los nodos están conectados.")
            return True

        # Realizar la búsqueda en anchura (BFS)
        queue = deque([inicio])
        visitado[inicio[0]][inicio[1]] = True

        while queue:
            x, y = queue.popleft()
            nodo_actual = self.Matriz[x][y]
            cont = 0
            # Verificar los vecinos del nodo actual
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                
                nx, ny = x + dx, y + dy
                # Verificar los límites de la matriz y si el nodo vecino es un nodo válido
                if 0 <= nx < len(self.Matriz) and 0 <= ny < len(self.Matriz[0]):
                    vecino = self.Matriz[nx][ny]
                    # Verificar si el nodo vecino es una isla y está conectado al nodo actual
                    if isinstance(vecino.Dato, int) is False and not visitado[nx][ny]:

                        if vecino.Dato in "-=||":
                            visitado[nx][ny] = True
                            queue.append((nx, ny))
                    elif isinstance(vecino.Dato, int) and not visitado[nx][ny]:
                        if vecino.Dato == vecino.Puentes:
                            visitado[nx][ny] = True
                            queue.append((nx, ny))
                        else:
                            return False
        # Verificar si todos los nodos han sido visitados
        for i in range(len(self.Matriz)):
            for j in range(len(self.Matriz[0])):
                if isinstance(self.Matriz[i][j].Dato, int) and not visitado[i][j]:
                    print(f"No todos los nodos están conectados.")
                    return False
        print("Todos los nodos están conectados.")
        return True


    def verificar_camino(self, x1, y1, x2, y2):
        # Verificar que no haya nada en el camino
        if x1 == x2:
            for j in range(min(y1, y2)+1, max(y1, y2)):
                if isinstance(self.Matriz[x1][j].Dato,int) or self.Matriz[x1][j].Dato in "|":
                    return False
        elif y1 == y2:
            for i in range(min(x1, x2)+1, max(x1, x2)):
                if isinstance(self.Matriz[i][y1].Dato ,int ) or self.Matriz[i][y1].Dato in "-=":
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
    def eliminar_camino(self, x1, y1, x2, y2):
        # Elimina el camino en los nodos
        if x1 == x2:
            for j in range(min(y1, y2) + 1, max(y1, y2)):
                if self.Matriz[x1][j].Dato == "=":
                    self.Matriz[x1][j].Dato = "-"
                elif self.Matriz[x1][j].Dato == "-":
                    self.Matriz[x1][j].Dato = " "
        elif y1 == y2:
            for i in range(min(x1, x2) + 1, max(x1, x2)):
                if self.Matriz[i][y1].Dato == "||":
                    self.Matriz[i][y1].Dato = "|"
                elif self.Matriz[i][y1].Dato == "|":
                    self.Matriz[i][y1].Dato = " "

    def information(self):
        data = ""
        matriz = self.Matriz
        matriz_len = len(matriz)

        for i in range(matriz_len):
            for j in range(matriz_len):
                dato = matriz[i][j].Dato
                dato_color = '\033[30m'  # verde

                if dato == '-' or dato == '|':
                    dato_color = '\033[32m'  # verde
                elif dato == '=' or dato == '||':
                    dato_color = '\033[33m'  # rojo
                elif matriz[i][j].Full:
                    dato_color = '\033[31m'  # rojo
                elif not matriz[i][j].Full and dato != ' ':
                    dato_color = '\033[35m'  # rojo
                
                reset_color = '\033[0m'  # resetear el color a predeterminado

                data += "{}[{}]({},{}){}\t".format(dato_color, dato, matriz[i][j].X, matriz[i][j].Y, reset_color)
            data += "\n"

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
    
    def validar(self, x1, y1, x2, y2):
        if self.Matriz[x1][y1].Full or self.Matriz[x2][y2].Full :
            return False
        return True
    def obtener_vecinos(self, x, y):
        vecinos = []

        # Buscar en la misma fila hacia la izquierda
        for j in range(y - 1, -1, -1):
            if isinstance(self.Matriz[x][j].Dato, int):
                if self.validar(x,y,x,j):
                    vecinos.append((x, j))
                break
            elif "|" in self.Matriz[x][j].Dato :
                break

        # Buscar en la misma fila hacia la derecha
        for j in range(y + 1, len(self.Matriz[0])):
            if isinstance(self.Matriz[x][j].Dato, int):
                if self.validar(x,y,x,j):
                    vecinos.append((x, j))
                break
            elif "|" in self.Matriz[x][j].Dato :
                break

        # Buscar en la misma columna hacia arriba
        for i in range(x - 1, -1, -1):
            if isinstance(self.Matriz[i][y].Dato, int):
                if self.validar(x,y,i,y):
                    vecinos.append((i, y))
                break
            elif  self.Matriz[i][y].Dato in "-=":
                break

        # Buscar en la misma columna hacia abajo
        for i in range(x + 1, len(self.Matriz)):
            if isinstance(self.Matriz[i][y].Dato, int):
                if self.validar(x,y,i,y):
                    vecinos.append((i, y))
                break
            elif  self.Matriz[i][y].Dato in "-=":
                break

        return vecinos
    def calcular_direccion(self,x1, y1, x2, y2):
        if x1 == x2:
            if y2 > y1:
                return 1 # Norte
            else:
                return 3 # Sur
        elif y1 == y2:
            if x2 > x1:
                return 0 # Este
            else:
                return 2 # Oeste
        else:
            print("LOKA")
            return -1 # los puntos no están en la misma fila/columna
    
    def resolver(self):
        # Encontrar una isla de inicio
        inicio = None
        max = 0
        for i in range(len(self.Matriz)):
            for j in range(len(self.Matriz[0])):
                if isinstance(self.Matriz[i][j].Dato, int):
                    if max<self.Matriz[i][j].Dato:
                        inicio = (i, j)
                        max = self.Matriz[i][j].Dato

        if not inicio:
            print("No se encontró una isla de inicio")
            return

        # Llamar a la función de búsqueda exhaustiva
        try:
            solucion_encontrada = self.busqueda_exhaustiva(inicio)
        except Exception as e:  # Capturar cualquier tipo de excepción
            print("No se ha encontrado una solución. Tiempo excedido.")
            print(e)
            return False


        if solucion_encontrada:
            print("Se ha encontrado una solución:")
            print(self.information())
        else:
            print("No se ha encontrado una solución")
    
    def busqueda_exhaustiva(self, nodo):
        # Verificar si se ha alcanzado el objetivo
        if self.verificar_victoria():
            exit()

        x, y = nodo
        
        # Obtener los vecinos del nodo actual
        vecinos = self.obtener_vecinos(x, y)

        def custom_key(item):
            x, y = item
            bridges = self.Matriz[x][y].Direcciones
            return (sum(bridges), -self.Matriz[x][y].Dato)
        vecinos = sorted(vecinos, key=custom_key)

        counter = 0
        # Procesar los vecinos no visitados
        for vecino in vecinos:
            # Verificar si el vecino ya ha sido visitado
            if vecino not in self.visitados:
                # Realizar la conexión con el vecino
                #print("Conectar", vecino, "a", x, ",", y)
                result =   self.Matriz[x][y].conectar(self, self.Matriz[vecino[0]][vecino[1]], self.calcular_direccion(x, y, vecino[0], vecino[1]))
                #print("Resultado",result)
                self.visitados.append(vecino)
                if result != 1:
                    #print("Removing",vecino)
                    self.visitados.remove(vecino)
                print(self.information())

                # Marcar el vecino como visitado
                
                counter+=1
                # Realizar la llamada recursiva para el vecino
                
                solucion_encontrada = self.busqueda_exhaustiva(vecino)
                if not solucion_encontrada:
                    pass
                else:
                    # Deshacer la conexión con el vecino (backtracking)
                    #print("Desconectar", vecino, "a", x, ",", y)
                    self.Matriz[x][y].desconectar(self, self.Matriz[vecino[0]][vecino[1]], self.calcular_direccion(x, y, vecino[0], vecino[1]))
                    print(self.information())
                        # Desmarcar el vecino como visitado
                    self.visitados.remove(vecino)

                # Si se encontró una solución válida, retornar True
                if solucion_encontrada:
                    return True
        #print("Breaking", nodo)
        return False
