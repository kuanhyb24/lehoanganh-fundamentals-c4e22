person = {
    "name": "Hoanganh",
    "age": 21,
}
print(person)
key = input("ban muon xao hay cap nhat (D or U) ")
if key =="D":
    n = input("ban muon xoa key nao: ")
    if n not in person:
        print("k co")
    else:
        del person[n]
        print(person)
elif key == "U":
    a = input("ban muon cap nhap cai gi : ")
    v = input("thong tin moi: ")
    person[a] = v
    print(person)
else:
    print("k co")
