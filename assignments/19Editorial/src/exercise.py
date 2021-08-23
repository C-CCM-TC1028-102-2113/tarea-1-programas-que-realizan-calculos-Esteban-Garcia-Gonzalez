def main():
    #escribe tu código abajo de esta línea
    p=int(input('Dame el número de palabras: '))

    if ((p % 475) == 0):
        p=p/475
        c= float((p*60)*0.9)
        print('El costo de la publicación es: '+ str(c))
    


    else:
        p= (p//475)+1
        c= float((p*60)*.9)
        print('El costo de la publicación es: '+ str(c))

    pass

if __name__ == '__main__':
    main()
