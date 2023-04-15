# import random

# numero_random = random.randint(0,1)
# if numero_random == 0:
#   print("Cara")
# else:
#   print ("Cruz")

# numero_flotante = random.random()
# print(numero_flotante)


import random
lista_nombres = input('ingresa la lista de nombres')
nombres = lista_nombres.split(',')

el_que_paga = random.choice(nombres)
# nombres[random.randint(0,len(nombres)-1)]

print(el_que_paga + " va a pagar la cuenta")


# row1 = [" "," "," "]
# row2 = [" "," "," "]
# row3 = [" "," "," "]
# map = [row1, row2, row3]

# print(f"{row1}\n{row2}\n{row3}")
# casilla = input("Indique donde quiere colocar el tesoro")

# map [int(casilla[0])-1][int(casilla[1])-1] = 'X'
# print(f"{row1}\n{row2}\n{row3}")
