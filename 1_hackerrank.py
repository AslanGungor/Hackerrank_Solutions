n=int(input("Lütfen sayıyı giriniz"))
m=int(3*int(n))
print(n,m)
for i in range(1,n+1):
    if i==(n+1)/2:
        for m in range(1,m+1):  
            print(".",end="")
    else:
        for k in range(1,m+1):
            print("-",end=" ")
            if k==(m-1)/2:              #En orta sütuna "|" işareti koyuyor
                print("|",end="")
    print()                             #Satır Atlama
