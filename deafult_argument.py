def net_price(price, discount=0,tax = 0.5):
    return price * (1 - discount)*(1 + tax)

print(net_price(100,0.1))
print(net_price(100))