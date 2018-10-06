person = {
    "name": "HoangAnh",
    "age": 21,
}
text = input("Nhap key va value ")
pair = text.split(",")
# pair = text.split(",")
# key = pair[0]
# value = pair[1]

key, value = pair

person[key] = value
print(person)


