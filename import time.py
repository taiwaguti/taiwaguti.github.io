import time

# --- 1. ALGORITMOS DE BÚSQUEDA ---

# Búsqueda Secuencial (recorre uno por uno)
def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Retorna el índice si lo encuentra
    return -1  # Retorna -1 si no existe

# Búsqueda Binaria Iterativa (con ciclo while)
def busqueda_binaria_iterativa(lista, objetivo):
    baja = 0
    alta = len(lista) - 1
    
    while baja <= alta:
        medio = (baja + alta) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            baja = medio + 1  # Busca en la mitad derecha
        else:
            alta = medio - 1  # Busca en la mitad izquierda
    return -1

# Búsqueda Binaria Recursiva (se llama a sí misma)
def busqueda_binaria_recursiva(lista, objetivo, baja, alta):
    if baja > alta:
        return -1  # Caso base: no se encontró
        
    medio = (baja + alta) // 2
    if lista[medio] == objetivo:
        return medio  # Caso base: elemento encontrado
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, alta)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, baja, medio - 1)


# --- 2. PRUEBAS Y MEDICIÓN DE TIEMPOS ---

# Lista de tamaños que pide el ejercicio
tamanos = [100, 1000, 10000, 100000]

for tamano in tamanos:
    # Generar la lista ordenada como muestra tu primera imagen
    lista = list(range(tamano))
    
    # Definir los 4 casos de objetivos a buscar
    casos = ["Inicio", "Medio", "Final", "No existe"]
    
    for caso in casos:
        # Asignar el objetivo según el caso actual
        if caso == "Inicio":
            objetivo = lista[0]
        elif caso == "Medio":
            objetivo = lista[len(lista) // 2]
        elif caso == "Final":
            objetivo = lista[-1]
        elif caso == "No existe":
            objetivo = -1

        # --- Medir Búsqueda Secuencial ---
        inicio_tiempo = time.perf_counter()
        busqueda_secuencial(lista, objetivo)
        fin_tiempo = time.perf_counter()
        tiempo_secuencial = fin_tiempo - inicio_tiempo

        # --- Medir Búsqueda Binaria Iterativa ---
        inicio_tiempo = time.perf_counter()
        busqueda_binaria_iterativa(lista, objetivo)
        fin_tiempo = time.perf_counter()
        tiempo_iterativa = fin_tiempo - inicio_tiempo

        # --- Medir Búsqueda Binaria Recursiva ---
        inicio_tiempo = time.perf_counter()
        busqueda_binaria_recursiva(lista, objetivo, 0, len(lista) - 1)
        fin_tiempo = time.perf_counter()
        tiempo_recursiva = fin_tiempo - inicio_tiempo

        # Mostrar los resultados en pantalla ordenados por filas
        print("Tamaño:", tamano, "| Caso:", caso)
        print("  Secuencial:       ", tiempo_secuencial, "segundos")
        print("  Binaria Iterativa:", tiempo_iterativa, "segundos")
        print("  Binaria Recursiva:", tiempo_recursiva, "segundos")
        print("-" * 50)