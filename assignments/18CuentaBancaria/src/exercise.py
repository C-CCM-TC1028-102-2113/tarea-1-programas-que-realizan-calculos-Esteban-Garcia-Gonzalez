def main():
    #escribe tu código abajo de esta línea
    si=float(input('Dame el saldo del mes anterior: '))
    i= float(input('Dame los ingresos: '))
    e= float(input('Dame los egresos: '))
    nc=int(input('Dame el número de cheques: '))

    sf= si-e+i-(nc*13)
    t= sf*(.925)

    print('El saldo final de la cuenta es: '+ str(total))

    pass

if __name__ == '__main__':
    main()
