"""Practical application: mini project with data and functions.

Objectives:
- Apply data structures and functions.
- Manipulate data using lists and dictionaries.
- Prepare the ground for working later with libraries such as pandas."""

# Mini-project
# Manage a small list of products, with:
# - Name
# - Price
# - Category
#
# We will:
# - Register products (list of dictionaries)
# - Calculate total value
# - Filter by category
# - Calculate average price

# MINI-PROJECT FUNCTIONS

def create_product(name, price, category):  # Create and return a dictionary representing a product.
    return {
        "name": name,
        "price": float(price),
        "category": category,
    }


def add_product(product_list, product):  # Add a product to the list.
    product_list.append(product)


def calculate_total_value(product_list):  # Return the sum of all product prices.
    return sum(product["price"] for product in product_list)


def filter_by_category(product_list, category):  # Return a new list with only products from the informed category.
    return [p for p in product_list if p["category"] == category]


def calculate_average_price(product_list):  # Return the average price of the products.
    if not product_list:
        return 0
    return calculate_total_value(product_list) / len(product_list)


def display_products(product_list):  # Display the products on screen in a friendly way.
    if not product_list:
        print("No products registered.")
        return

    for product in product_list:
        name = product["name"]
        price = product["price"]
        category = product["category"]
        print(f"- {name} | R$ {price:.2f} | Category: {category}")


# USAGE SIMULATION (WITHOUT USER INPUT)

products = []

add_product(products, create_product("Laptop", 3500, "Electronics"))
add_product(products, create_product("Mouse", 80, "Electronics"))
add_product(products, create_product("T-shirt", 60, "Clothing"))
add_product(products, create_product("Python Book", 120, "Books"))

print("Product List:")
display_products(products)

total = calculate_total_value(products)
average = calculate_average_price(products)

print(f"\nTotal value of products: R$ {total:.2f}")
print(f"Average price of products: R$ {average:.2f}")

electronics = filter_by_category(products, "Electronics")
print("\nProducts in the 'Electronics' category:")
display_products(electronics)
