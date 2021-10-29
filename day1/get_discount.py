def get_discount(price, discount):
    return price * (1 - discount/100)

print(get_discount(100, 10))
