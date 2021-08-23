def main():
    #escribe tu código abajo de esta línea
    n=int(input('Dame un número: '))

    p=0
    
    while (n > 0):
        if (n % 2 == 0):
            p=p+1
        else:
            p=p

        n=n//10
    

    print('El número de dígitos pares es: '+ str(int(p)))

    pass

if _name_ == '_main_':
    main()
