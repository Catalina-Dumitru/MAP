n=int(input("Introduceti un nr:"))
a=1
b=1
i=1
c=0
while i<n:
    c=a+b
    a=b 
    b=c
    i+=1
print(a)

