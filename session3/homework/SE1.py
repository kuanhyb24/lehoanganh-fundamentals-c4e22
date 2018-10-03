while True:
    print("welcome to shop")
    y = input("what do you want ( C, R, U, D)?")
    if y == "R":
        items = ['T-Shirt', 'sweater']
        print("mat hang cua chung toi la: ", *items, sep=", ")
    elif y == "C":
        n = input("enter new items: ")
        items.append(n)
        print("cac mat hang cua chung toi: ", *items, sep=", ")
    elif y == "U":      
        a = int(input("Update position? "))
        Update = str(input("New items? "))
        items[a-1] = Update    
        print("mat hang cua chung toi la: ", *items, sep=", ")
    elif y == "D":    
        i = int(input("Delete position? "))
        items.remove('Jeans')
        print("mat hang cua chung toi la: ", *items, sep=", ")        
        break


