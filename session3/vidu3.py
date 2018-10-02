items = ['com', 'pho', 'com rang']

i = input("ban muon xoa cai gi")
if i.isdigit():
    index = int(i)
    n = int(i)
    items.pop(n-1)
else:
    items.remove(i)