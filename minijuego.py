import random

num = random.randint(0, 100)



a = 0

while num != a:

    a = int(input("ingrese un numero"))

    if num == a:
        print("Es el numero",num)

    elif num > a:
        print("El numero ingresado es mas chico que el random")

    elif num < a:
        print("El numero ingresado es mas grande que el random")



print("Felicitanciones encontraste en numero random:",num)
