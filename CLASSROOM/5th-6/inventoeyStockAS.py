#. Inventory Stock Alert System 
#Problem Statement 
#An inventory manager stores stock quantities as: 
#stock = [25, 5, 0, 12, 3, 18, 0, 30]


stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock = 0
restock_required = []
healthy_stock = []
available_products = 0

for qty in stock:

    # Out of stock products display
    if qty == 0:
        out_of_stock += 1

    # Restock required products quantity less than 10
    if qty < 10:
        restock_required.append(qty)

    # Available products count
    if qty > 0:
        available_products += 1

    # Healthy stock quantity 15 or more
    if qty >= 15:
        healthy_stock.append(qty)

print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock_required)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)