print("Bienvenido a la calculadora de propinas\n")
total = float(input("Cual es el total de la factura? $"))
personas = int(input("Cuantas personas van a dividir la propina "))
porcentaje = float(input("Cual es el valor de la propina: 5, 10, 15, 20? "))
propina = total * (1 + (porcentaje / 100)) / personas
final = "{:.2f}".format(propina)
print(f"Cada persona debe pagar: $ {final}")
