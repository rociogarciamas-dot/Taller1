import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# EJERCICIO 1: Gasto total por usuario

for usuario, compras in data.items():
    total = 0

    for compra in compras:
        total = total + compra["precio"]

    print(f"{usuario}: {total:.2f} €")
