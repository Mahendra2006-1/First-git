#Arithemetic operators
a = 10
b = 9
print("sum :",a+b)
print("subtraction: ",a-b)
print("multiplication: ",a*b)
print("division: ",a/b)
print("modular division: ",a%b)

#comparision operator
print("equal: ",a==b)
print("not equal: ",a!=b)
print("greater: ",a>b)
print("lesser: ",a<b)
print("greater or equal: ",a>=b)
print("lesser or equal: ",a<=b)

#logical operator
print("and",a>5 and b<5)
print('or',a>5 or b<5)
print('not',not(b<5))

#assignment operator
print(a)
a += 5
print(a)
a -= 6
print(a)
a *= 3
print(a)
a /= 2
print(a)
a %= 3
print(a)

#bitwise operator
a = 10

print("bitwise or :",a|b)
print("bitwise and: ",a&b)
print('bitwise xor: ',a^b)
print('bitwise not: ',~a)
print("left shift: ",a<<2)
print("right shift:",b>>2)

#Membership operator
c = 'apple'
print("in operator: ",'p' in c)
print("not in operator: ",'p' not in c )

#identity operator
af = 'train'
bf = 'tank'
print(af is bf)
print(af is not bf)


#ternary operator
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  
