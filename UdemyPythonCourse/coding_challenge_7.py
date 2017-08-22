products = {"soap": 12, "butter": 19, "bucket": 15, "belt": 49, "stick": 3}


def get_price(product):
    return products.get(product, "not found")

print get_price("soap")
print get_price("soap1")