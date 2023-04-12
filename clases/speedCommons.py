class pretty:
    def prettyMatrix(M):
        Splt= str(M).split("[")
        for ln in Splt:
            ln = ln.replace(",","\t")
            if ln !="":
                print("["+ln)
                # calcula la dirección entre dos puntos
class utils:
    def load_matrix(filename):
        with open(filename, 'r') as file:
            # Read the dimensions of the matrix
            rows, cols = [int(dim) for dim in file.readline().split(",")]
    
            # Initialize empty matrix
            matrix = []
    
            # Parse each row of the matrix and add to the list
            for i in range(rows):
                row = [int(x) for x in file.readline().split()]
                matrix.append(row)
    
        return matrix,rows,cols
    
class maths:
    def calcular_direccion(x1, y1, x2, y2):
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
            return -1 # los puntos no están en la misma fila/columna

            