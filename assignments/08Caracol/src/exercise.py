def main():
    #escribe tu código abajo de esta línea
    time=round(float(input('Dame los minutos: ')),1)

    vel=5.7
    dist=float((vel*6)*time)

    print('Centímentros recorridos: '+ str(round(dist,1)))



    pass

if _name_ == '_main_':
    main()
