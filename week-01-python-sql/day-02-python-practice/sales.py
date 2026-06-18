print("Product Sales Report")
print("--------------------")

products = [
    {"name":"Laptop","category":"technology","price":30000,"quantity":2},
    {"name":"mouse","category":"technology","price":500,"quantity":10},
    {"name":"desk","category":"furniture","price":4000,"quantity":3},
    {"name":"chair","category":"furniture","price":2500,"quantity":4}
]

def calculate_sales(price,quantity):
    return price * quantity


def get_stock_status(quantity):
    if quantity >=5:
        return "in stock"
    else:
        return "low stock"

total_revenue = 0
best_product= ""
best_sales= 0
category_sales= {}

low_stock_count=0

print("\nProduct Results")

print("--------------------")

for product in products:
    name= product["name"]
    category= product["category"]
    quantity= product["quantity"]

    total_sales = calculate_sales(product["price"],product["quantity"])

    stock_status= get_stock_status(quantity)

    total_revenue = total_revenue + total_sales

    if total_sales > best_sales:
        best_sales = total_sales
        best_product= name

    if category not in category_sales:
        category_sales[category] = 0
    
    category_sales[category] = category_sales[category] + total_sales

    if stock_status=="low stock":
        low_stock_count=low_stock_count +1

    print(
        f"{name} | "
        f"category:{category}| "
        f"quantity:{quantity}| "
        f"sales:{total_sales} "
        f"stock:{stock_status}"
    )

average_sales=total_revenue/len(products)

print("----------------")
print(f"Total revenue: {total_revenue}")
print(f"average sales: {average_sales}")
print(f"best product: {best_product} with {best_sales}")

print(f"Low stock products: {low_stock_count}")

print( "-----------")
print("category sales")

for category, sales in category_sales.items():
    print(f"{category}:{sales}")
