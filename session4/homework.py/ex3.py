cau1 = {
    'de bai' : "Answer the following algebra questions:",
    'cau hoi' : "If x = 8, then what is the value of 4(x+3)?",
    'lua chon' : ["1. 35","2. 36","3. 40","4. 44"],
    'lua chon dung': 4,
}

while True:
    print(cau1['de bai'])
    print(cau1['cau hoi'])
    for n in cau1['lua chon']:
        print(n)
    answer = int(input("ban chon: "))
        # if answer.isdigit():
        #     answer = int(answer)
    if answer == cau1['lua chon dung']:
        print("chinh xac")
        break
    else:
        print(":(")
        
        # else:
        #     print(":(")    


