a = 1
b = 0
c = 0
n = int(input("arm"))
while a<=9:
    a+=1
    while b<=9:
        b+=1
        while c<9:
            c+=1
            arm = a * 100 + b * 10 + c
            armcube = a * a * a + b * b * b + c * c * c
if arm==armcube:
    print(arm)
