n=int(input("Enter size: "))
a=[]
b=[]
for i in range(0,n):

    a.append(int(input("Enter element: ")))

for i in a:
    if i not in b:
        b.append(i)
print("List without duplications is ",b)
