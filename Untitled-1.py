def bubble_sort(wasa):
    n = len(wasa)
    for i in range(n):
        for j in range(0,n - i - 1):
            if wasa[j] > wasa[j+1]:
                wasa[j], wasa[j+1] = wasa[j+1], wasa[j]
    return wasa
a = bubble_sort([4,1,6,32,5])
print(a)
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista
u = selection_sort([4,1,6,32,5])
print(u)
def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista
c = insertion_sort([4,1,6,32,5])
print(c)