products = [
    {"name" : "keyboard", "price" : 45},
    {"name" : "monitor", "price" : 180},
    {"name" : "mouse", "price" : 25},
    {"name" : "headphones", "price" : 75},
    {"name" : "USB drive", "price" : 15},
    {"name" : "webcam", "price" : 60},
]

def under_fifty(products):
    return products.get("price") < 50

products_under_fifty = filter(under_fifty, products)

print(f"""
Products under $50:
{list((products_under_fifty))}""")