items = ['bun', 'pho', 'com rang']
print(*items, sep="\n")
n = int(input("vi tri ma ban muon xem la: "))
if 0 <= n <= 2:
    print(items[n-1])
else:
    print("khong co vi tri ban can tim ")
    
