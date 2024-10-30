def getDistinctproducts(products):
    s = set()
    for product in products:
        s.add(product)
    return sorted(s)
products = ["watermelon", "grapes", "grapes", "apple", "grapes"]
print(getDistinctproducts(products))