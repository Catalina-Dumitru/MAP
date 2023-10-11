i=int(input("Scrieti un an:"))
if (i%400==0) or (i%4==0 and i%100!=0):
    print("Acesta este un an bisect")
else:
    print("Acesta nu este un an bisect")
