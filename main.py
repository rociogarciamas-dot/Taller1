import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# EJERCICIO 1: Gasto total por usuario

for usuario, compras in data.items():
    total = 0

    for compra in compras:
        total = total + compra["precio"]

    print(f"{usuario}: {total:.2f} €")

# EJERCICIO 2: Cliente VIP

cliente_vip = ""
gasto_maximo = 0

for usuario, compras in data.items():
    total = 0

    for compra in compras:
        total = total + compra["precio"]

    if total > gasto_maximo:
        gasto_maximo = total
        cliente_vip = usuario

print(f"Cliente VIP: {cliente_vip} ({gasto_maximo:.2f} €)")

# EJERCICIO 3: Cliente con más artículos

cliente_mas_compras = ""
max_articulos = 0

for usuario, compras in data.items():
    numero_articulos = len(compras)

    if numero_articulos > max_articulos:
        max_articulos = numero_articulos
        cliente_mas_compras = usuario

print(f"Cliente con más artículos: {cliente_mas_compras} ({max_articulos} artículos)")
