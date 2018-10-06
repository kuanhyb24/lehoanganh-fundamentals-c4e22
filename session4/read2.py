person = {
    "name": "Hoanganh",
    "age": 21,
}
n = input("ban muon xem thong tin gi? ")
# if n == "name" or n == "age":
#     print(person[n])
# else:
#     print("khong co thong tin ban tim")
if n not in person:
    print(" k co")
else:
        print(person[n])