instrucciones = '''
Crea un procedimiento: es_par_o_impar(n) 
Que diga si un número es par o impar. Solo debe mostrar el resultado en pantalla, no devolverlo.
'''


def es_par_o_impar(n):
    if n % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

es_par_o_impar(5)
es_par_o_impar(10)
