prices = {
    'banana' : 4,
    'apple' : 2,
    'orange' : 1.5,
    'pear' : 3
}
stock = {
    'banana' : 6,
    'apple' : 0,
    'orange' : 32,
    'pear' : 15
}
for food in prices:
        print(food)
        print("prices: %s" % prices[food])
        print("stock: %s" % stock[food])
total = 0
for price in prices:
    money = prices[price] * stock[price]
    print(money)
    total = total + money
print("The total money is", total) 