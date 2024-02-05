def sort_by(products, key):
    sorted_products = sorted(products, key=lambda x: list(x.values())[0][key],reverse=True)
    print(sorted_products)

products = [
    {"iphone": {"price": 1000, "ratings": 4}},
    {"samsung": {"price": 800, "ratings": 3}},
    {"lg": {"price": 1200, "ratings": 5}}
]

sort_by(products, "ratings")


