from clase import FechaHora
if __name__ == '__main__':

    d=int(input("Ingrese Dia: "))

    mes=int(input("Ingrese Mes: "))

    a=int(input("Ingrese Año: "))

    h=int(input("Ingrese Hora: "))

    m=int(input("Ingrese Minutos: "))

    s=int(input("Ingrese Segundos: "))

    r = FechaHora() #  inicilizar día, mes, año con 1/1/2020, y hora, minutos y 

                              #  segundos con 0h, 0m, 0s.

    r1 = FechaHora(d,mes,a); # inicializar con 0h 0m 0s

    r2= FechaHora(d,mes,a,h, m, s)

    r.Mostrar()

    r1.Mostrar()

    r2.Mostrar()

    hora=int(input("Ingresa hora para establecerla r:"))

    r.PonerEnHora(hora) # solamente la hora

    r.Mostrar()

    hora=int(input("Ingresa hora para establecerla r2:"))
    minutos=int(input("Ingresa minutos para establecerla r2:"))
    r2.PonerEnHora(hora,minutos) #hora y minutos
    r2.Mostrar()


    hora=int(input("Ingresa hora para establecerla r:"))
    minutos=int(input("Ingresa minutos para establecerla r:"))
    segundos=int(input("Ingresa segundos para establecerla r:"))
    r.PonerEnHora(hora,minutos,segundos) #hora, minutos y segundos
    r.Mostrar()

    hora=int(input("Ingresa hora para adelantar r:"))
    minutos=int(input("Ingresa minutos para adelantar r:"))
    segundos=int(input("Ingresa segundos para adelantar r:"))
    r.AdelantarHora(hora,minutos,segundos) #sumar 3 horas a la hora actual
    r.Mostrar()

    hora=int(input("Ingresa hora para adelantar r1:"))
    minutos=int(input("Ingresa minutos para adelantar r1:"))
    segundos=int(input("Ingresa segundos para adelantar r1:"))
    r1.AdelantarHora(hora,minutos,segundos) #sumar 1 hora y 15 minutos a la hora actual
    r1.Mostrar()

    hora=int(input("Ingresa hora para adelantar r2:"))
    minutos=int(input("Ingresa minutos para adelantar r2:"))
    segundos=int(input("Ingresa segundos para adelantar r2:"))
    r2.AdelantarHora(hora,minutos,segundos) 
    r2.Mostrar()
    #funcion test
    r2.Test()