n=int(input("Enter the limit: "))
for i in range(1,n+1):
    for j in range(65, 65+i):
        a=chr(j)
        print(a,end=" ")
    print()
