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

# EJERCICIO 4: Producto más caro y más barato

producto_mas_caro = None
producto_mas_barato = None

for usuario, compras in data.items():
    for compra in compras:

        if producto_mas_caro is None or compra["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = compra

        if producto_mas_barato is None or compra["precio"] < producto_mas_barato["precio"]:
            producto_mas_barato = compra

print(f"Producto más caro: {producto_mas_caro['producto']} ({producto_mas_caro['precio']:.2f} €)")
print(f"Producto más barato: {producto_mas_barato['producto']} ({producto_mas_barato['precio']:.2f} €)")

# EJERCICIO 5: Resumen por categorías

gastos_categorias = {}

for usuario, compras in data.items():
    for compra in compras:
        categoria = compra["categoria"]
        precio = compra["precio"]

        if categoria not in gastos_categorias:
            gastos_categorias[categoria] = 0

        gastos_categorias[categoria] += precio

print("Resumen por categorías:")

for categoria, total in gastos_categorias.items():
    print(f"{categoria}: {total:.2f} €")

# EJERCICIO 6: Añadir el 21% de IVA

for usuario, compras in data.items():
    for compra in compras:
        precio = compra["precio"]
        precio_con_iva = round(precio * 1.21, 2)

        compra["precio_con_iva"] = precio_con_iva

print("Productos con IVA:")

for usuario, compras in data.items():
    for compra in compras:
        print(f"{compra['producto']}: {compra['precio_con_iva']:.2f} €")
