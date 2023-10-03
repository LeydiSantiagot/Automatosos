'''
De la siguiente variable texto = Son las 7 de la noche y ya me quiero ir
Si se encuentra el numero 7 y es menor a 8, imprimir el numero 7 convertido a int y el texto
'es hora de irnos, son las 7'
'''

texto= 'Son las 7 de la noche y ya me quiero ir'

if '7' in texto:
    n= int('7')
    if n<8:
        print('Es hora de irnos, son las 7')