"Ejercicio Fibonacci" 

def ejercicio_fibonacci(terminos):
    resultado = [] 
    primer_termino = 1
    resultado.append(str(primer_termino)) 
    segundo_termino = 1
    resultado.append(str(segundo_termino)) 

    # Se descartan los dos terminos ya agregados
    for numero in range (terminos - 2):
        total = primer_termino + segundo_termino
        segundo_termino = primer_termino
        primer_termino = total
        resultado.append(str(total)) 
    return resultado


numero_terminos = int(input("Ingrese el numero de terminos que quiera: ")) 
print(", ".join(ejercicio_fibonacci(numero_terminos))) 




