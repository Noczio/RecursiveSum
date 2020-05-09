# -*- coding: utf-8 -*-
#region Importanciones
import json # gracias a esta libreria podemos utilizar regiones en python
#endregion Importaciones

#region funciones
def sumar(minLimit,maxLimit):
    if(minLimit==maxLimit): # ambas entradas en un principio son 0 o en algun momento ambas llegaran a ser 0 por recursividad
        return minLimit # si colocaramos return 0 cuando los dos limites se intersecten entonces no se suma la ultiam iteracion
    elif minLimit>=0 and maxLimit>0: # caso sumar desde 0 hasta +infinito      
        return sumar(minLimit,maxLimit-1)+maxLimit        
    else: # caso sumar desde -infinito hasta 0
        return sumar(minLimit+1,maxLimit)+minLimit
#endregion funciones

#region metodo main
if __name__== "__main__": 
    try:
        minLimit=int(input("Ingrese el límite inferior: "))
        maxLimit=int(input("Ingrese el límite superior: "))

        if(minLimit>maxLimit):
            temp=minLimit
            minLimit=maxLimit
            maxLimit=temp
        
        answ=sumar(minLimit,maxLimit)
        print("La suma desde {} hasta {} es: {}".format(minLimit,maxLimit,answ))       
            
    except:
        print("Ocurrio un error")
    input("Presiona cualquier tecla para terminar ... ")
#endregion metodo main