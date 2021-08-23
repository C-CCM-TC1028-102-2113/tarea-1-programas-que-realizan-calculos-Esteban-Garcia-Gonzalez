def main():
    #escribe tu código abajo de esta línea
    msj= int(input('Dame el número de mensajes: '))
    mg=round(float(input('Dame el número de megas: ')),1)
    t= int(input('Dame el número de minutos: '))

    msj=msj*0.8
    mg=mg*0.8
    t=t*0.8

    total=msj+mg+t

    print('El costo mensual es: '+ str(total))
    pass

if __name__ == '__main__':
    main()
