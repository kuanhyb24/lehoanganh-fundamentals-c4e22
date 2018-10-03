sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hoang Anh and these are my ship sizes")
print(sizes)
#month 1 :
for i in range(len(sizes)):
    sizes[i] = sizes[i] + 50
print("one month has passed, now here is my flock")
print(sizes)
n= int(input("vi tri ma ban muon doi la "))
update = int(input("ban muon thay thanh so "))
sizes[n]=update
print("after shearing, here is my flock")
print(sizes)

#month 2 :
for i in range(len(sizes)):
    sizes[i] = sizes[i] + 50
print("one month has passed, now here is my flock")
print(sizes)
print("now my biggest sheep has size", max(sizes))
n = int(input("vi tri ma ban muon doi la "))
update = int(input("ban muon thay doi thanh so "))
sizes[n]=update
print("after shearing, here is my flock")
print(sizes)

#month 3 :
for i in range(len(sizes)):
    sizes[i] = sizes[i] + 50
print("one month has passed, now here is my flock")
print(sizes)
print("now my biggest sheep has size", max(sizes))
n = int(input("vi tri ma ban muon doi la "))
update = int(input("ban muon thay doi thanh so "))
sizes[n]=update
print("after shearing, here is my flock")
print(sizes)

