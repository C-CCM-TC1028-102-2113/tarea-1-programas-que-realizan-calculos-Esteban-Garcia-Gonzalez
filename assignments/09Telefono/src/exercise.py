def main():
    #escribe tu código abajo de esta línea
    msj= int(input('Dame el número de mensajes: '))
    megas=round(float(input('Dame el número de megas: ')),1)
    time= int(input('Dame el número de minutos: '))

    msj=msj*0.8
    megas=megas*0.8
    time=time*0.8

    total=msj+megas+time

    print('El costo mensual es: '+ str(total))
    pass

if __name__ == '__main__':
    main()
