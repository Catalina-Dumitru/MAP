prim=1
n=int(input("introducetu n:"))
for d in range(2,n,1):
    if n%d==0:
     prim=0
if prim==1 and n>=2:
    print("este prim")
else:
    print("nu e prim")      