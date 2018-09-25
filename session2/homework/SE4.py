#a
print("*" *20)
#b
n = int(input("nhap n : "))
print("*" *n)
#c
total = ""
for i in range(9):
    if i%2 == 0 :
        i = "x"
    else:
        i = "*"
    total += i
print(total)
#d
n = int(input("nhap n : "))
total = ""
for i in range(n):
    if i%2 == 0 :
        i = "x"
    else:
        i = "*"
    total += i
print(total)
#e
print()
print()
#f
for i in range(3):
    print("*" *7)
#g
n = int(input("nhap n : "))
m = int(input("nhap m : "))
for i in range(m):
    print("*" *n)