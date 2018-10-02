while True:
    n = input("enter your password: ")
    i = len(n)
    if i < 8:
        print("false")
    elif n.isdigit():        
        print("must not contain only digits")
    elif n.isupper():        
        print("must contain lowercase letters")     
    elif n.islower():
        print("must contain uppercase letters")         
    else:
        print("true")
        break
        
        

