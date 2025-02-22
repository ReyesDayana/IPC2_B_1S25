# Funciones

print("--------len(lista)------------")
mi_lista = [1, 2, 3]
longitud = len(mi_lista)
print(longitud)

print("--------max(lista)------------")
mi_lista = [1, 2, 3, 4]
maximo = max(mi_lista)
print(maximo)

print("--------min(lista)------------")
mi_lista = [1, 2, 3]
minimo = min(mi_lista)
print(minimo)

print("--------sum(lista)------------")
mi_lista = [1, 2, 3]
suma = sum(mi_lista)
print(suma)

print("-------sorted(lista)-----------")
mi_lista = [3, 1, 2]
ordenada = sorted(mi_lista)
print(ordenada)

# Métodos

print("-------append(elemento)-----------")
mi_lista = [1, 2, 3]
mi_lista.append(4)
print(mi_lista)

print("-------insert(indice, elemento)-----------")
mi_lista = [1, 3, 4]
mi_lista.insert(1, 2)
print(mi_lista)

print("-------remove(elemento)-----------")
mi_lista = [1, 2, 3, 2]
mi_lista.remove(2)
print(mi_lista)


print("-------pop()-----------")
mi_lista = [1, 2, 3, 4, 5, 6]
ultimo = mi_lista.pop()
print(ultimo)
print(mi_lista)
mi_lista.pop(1)
print(mi_lista)

print("-------clear()-----------")
mi_lista = [1, 2, 3]
mi_lista.clear()
print(mi_lista)

print("-------count(elemento)-----------")
mi_lista = [1, 2, 3, 2]
cuenta = mi_lista.count(2)
print(cuenta)

print("-------sort()-----------")
mi_lista = [7, 1, 4, 8, 12, 3]
mi_lista.sort()
print(mi_lista)
mi_lista.sort(reverse=True)
print(mi_lista)

print("-------reverse()-----------")
mi_lista = [1, 2, 3]
mi_lista.reverse()
print(mi_lista)

print("-------Recorrer lista-----------")
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in mi_lista:
    print(i)
print(mi_lista[1])