def main():
    #escribe tu código abajo de esta línea
    msj= int(input('Dame el número de mensajes: '))
    megas= float(input('Dame el número de megas: ')
    t= int(input('Dame el número de minutos: '))

    pmsj=msj*0.8
    pmegas=megas*0.8
    pt=t*0.8

    total=pmsj+pmegas+pt

    print('El costo mensual es: '+ str(total))
    pass

if __name__ == '__main__':
    main()
