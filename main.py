from clases.structures import Nodo,Hashiwokakero
from clases.speedCommons import pretty


Matriz = Hashiwokakero()
Matriz.convertir("matriz.txt")
print(Matriz.information())
uno = Nodo(8)
dos = Nodo(8)
uno.conectar(dos,2,2)
print(uno.conectar(dos,2,2))
print(uno.information())
print(dos.information())
