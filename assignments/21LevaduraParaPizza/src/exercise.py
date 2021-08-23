def main():
    #escribe tu código abajo de esta línea

    h=float(input('Dame la harina en gramos: '))

    kg= h/1000
    l= round(kg*50/1,1)

    print('Necesitas estos gramos de levadura: '+ str(l))

    pass

if __name__ == '__main__':
    main()
