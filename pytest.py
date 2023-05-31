def dfs(Grafo, nodo_inicial):
    visitados = set()  # Conjunto para llevar el registro de los nodos visitados
    dfs_recursivo(Grafo, nodo_inicial, visitados)

def dfs_recursivo(Grafo, nodo, visitados):
    visitados.add(nodo)  # Marcamos el nodo actual como visitado
    print(nodo)  # Procesamos el nodo actual (en este caso, lo imprimimos)

    # Recorremos los nodos vecinos no visitados del nodo actual
    for vecino in Grafo[nodo]:
        if vecino not in visitados:
            dfs_recursivo(Grafo, vecino, visitados)

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

nodo_inicial = 'A'
dfs(grafo, nodo_inicial)
    