a = int(input("enter start number: "))
b =  int(input("enter end number: "))
print("the prime numbrers in between ",a ,"and",b)

for num in range(a,b+1):
    if num >1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)
    else:
        print("wrong number")

