import random



a = 0
c = 0
j = 0
computadora = None

while a < 5:


    num = random.randint(1, 150)

    if num <= 50:

        computadora = 1 #PIEDRA

    elif num > 50 and  num <= 100:

        computadora = 2 #PAPEL

    elif num >= 150:

        computadora = 3 #TIJERA

    print("la computadora eligio:",computadora)


    jugador = int(input("seleccione: 1.Piedra, 2.Papel, 3.Tijera"))



    if jugador == computadora:

        print("EMPATE")



    elif jugador == 1 and computadora == 2:

        print("GANA COMPUTADORA")

        c = c + 1

    elif computadora == 1 and jugador == 2:

        print("GANA JUGADOR")

        j = j + 1


    elif jugador == 1 and computadora == 3:

        print("GANA JUGADOR")

        j = j + 1

    elif computadora == 1 and jugador == 3:

        print("GANA COMPUTADORA")

        c = c + 1



    elif jugador == 2 and computadora == 3:

        print("GANA COMPUTADORA")

        c = c + 1

    elif computadora == 2 and jugador == 3:

        print("GANA JUGADOR")

        j = j + 1



    a = a + 1

print("LOS RESULTADOS SON:")
print("JUGADOR:",j)
print("COMPUTADORA:",c)

