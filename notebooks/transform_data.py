def calculate_revenue(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")
    return price * quantity

data = [
    {"product": "Widget A", "price": 10.0, "quantity": 100},
    {"product": "Widget B", "price": 25.0, "quantity": 50},
]

for item in data:
    revenue = calculate_revenue(item["price"], item["quantity"])
    print(f"{item['product']}: ${revenue:.2f}")