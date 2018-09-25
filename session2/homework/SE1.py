a = int(input("chieu cao cua ban la:"))
b = int(input("can nang cua ban la:"))
print(a, "cm")
print(b,"kg")
a = a/100
BMI = b/(a*a)
print("chi so BMI cua ban la:", BMI)

if BMI < 16:
    print("giam can")
elif 16 < BMI < 18.5:   
    print("thieu can ")
elif 18.5 < BMI < 25:
    print("binh thuong")
elif 25 < BMI < 30:
    print("thua can")
else:
    print("beo phi")    


