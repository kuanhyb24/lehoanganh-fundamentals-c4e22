while True:
    items = ['T-Shirt', 'sweater']
    print("mat hang cua chung toi la: ", *items, sep=", ")
    n = input("enter new items: ")
    items.append(n)
    print("cac mat hang cua chung toi: ", *items, sep=", ")
    a = int(input("Update position? "))
    Update = str(input("New items? "))
    items[a-1] = Update    
    print("mat hang cua chung toi la: ", *items, sep=", ")
    i = int(input("Delete position? "))
    items.remove('Jeans')
    print("mat hang cua chung toi la: ", *items, sep=", ")        
    break


