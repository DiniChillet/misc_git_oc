from random import randint

val_min = 1
val_max = 10
nombre_a_deviner = randint(val_min, val_max)

for i in range(4):
    essai = int(input("Entrez votre valeur entre {0} et {1} ({2} essai):".format(val_min, val_max, i+1)))

    if (essai > nombre_a_deviner):
        print("Le nombre a deviner est plus petit que " + str(essai))
    elif (essai < nombre_a_deviner):
        print("Le nombre a deviner est plus grand que " + str(essai))
    else:
        print("!!!! gagne")
        break

    if i == 4:
        print("!!!! perdu. Le nombre a deviner etait {0}".format(nombre_a_deviner))


print("C'est fini")
