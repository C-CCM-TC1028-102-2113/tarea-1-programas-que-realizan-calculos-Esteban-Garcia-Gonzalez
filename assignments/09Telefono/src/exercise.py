def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    nmsj=int(input('Dame el número de mensajes:'))
    nmg=float(input('Dame el número de megas:'))
    nmi=int(input('Dame el número de minutos:'))
    pmsj= nmsj*0.8
    pmg=nmg*0.8
    pmi=nmi*0.8
    pt= pmsj+pmg+pmi
    print('El costo mensual es:'+str(pt))
    pass


if __name__ == '__main__':
    main()
