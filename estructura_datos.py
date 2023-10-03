'''
Crear una lista 1,2,5,3,2,3,6,10,8,9
1. Convertir la lista en un set para eliminar duplicados
2. Calcular la suma de los numeros usando una lista
3. Calcular la suma de los numeros usando un set
4. Crear un diccionario para almacenar las estadisticas
Numeros unicos, suma total de lista, suma total del set, maximo valor y minimo
5. Imprimir las estadisticas
'''

lista= [1,2,5,3,2,3,6,10,8,9]
ed= set(lista)
sum_lista= sum(lista)
sum_set= sum(ed)
num_unicos= len(ed)
maximo= max(ed)
minimo= min(ed)
diccionario ={'Núm unicos':num_unicos, 'Suma total de lista':sum_lista, 'Suma total de set': sum_set,
              'Valor maximo':maximo, 'Valor minimo':minimo}
print(diccionario)