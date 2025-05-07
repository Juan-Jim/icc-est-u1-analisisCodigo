# Archivo principal main
import matplotlib.pyplot as plt
import benchmarking as bm
##from benchmarking import Benchmarking
from metodos_ordenamientos import Metodo_ordenamiento

if __name__ == "__main__":
    ##print("Funciona")
    # bm.Benchmarking()
    #Benchmarking()
    bench = bm.Benchmarking()
    metodosO = Metodo_ordenamiento()
    
    ##tam = 10000   
    tamanios = [5000, 10000, 20000]
    resultados = []
    
    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)

        metodos_dic = {
            "burbuja": metodosO.metodo_burbuja,
            "burbujaM": metodosO.sort_burbuja_mejorado_optimizado,
            "seleccion": metodosO.sort_seleccion,
            "shell": metodosO.sort_shell,
        }

    

        for nombre , fun_metodo in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)

    for tam, nombre, tiempo in resultados:
        print(f'Tamano: {tam}, nombre metodo: {nombre}, tiempo: {tiempo:.6f} segundos')



# Prepara datos para ser graficas 
# 1 Crea un diccionario o map para almacenar resultados por metodos
    tiempos_by_metodo = {
        "burbuja": [],
        "burbujaM": [],
        "seleccion": [],
        "shell": []
    }

    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)
        
    plt.figure(figsize=(10,6))

    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label = nombre, marker = "o")

#agregar parametros

plt.title("Comparacion de tiempo prar cada metodo")     
plt.xlabel("Tamanio de los arreglos")
plt.ylabel("Tiempo de ejecucion")

    
plt.legend()

plt.show()

