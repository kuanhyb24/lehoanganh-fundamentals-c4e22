cau1 = [{
    'de bai' : "Answer the following algebra questions:",
    'cau hoi' : "If x = 8, then what is the value of 4(x+3)?",
    'lua chon' : ["1. 35","2. 36","3. 40","4. 44"],
    'lua chon dung': 4,
        },
        {
    'de bai' : "Estimate this answer (exact calculation not needed):",
    'cau hoi' : "Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?",
    'lua chon' : ["1. About 55","2. About 65","3. About 75","4. About 85"],
    'lua chon dung' : 2,
        }]

diem = 0
for i in range(len(cau1)):
    print(cau1[i]['de bai'])
    print(cau1[i]['cau hoi'])
    print(*cau1[i]['lua chon'], sep='\n')
    answer = int(input("ban chon: "))
         # if answer.isdigit():
         #     answer = int(answer)
    if answer == cau1[i]['lua chon dung']:
        print("chinh xac")
        diem = diem + 1
    else:
        print(":(")
         # else:
         #     print(":(")  
print("You correctly answer ", diem, "out of 2 questions")

        





