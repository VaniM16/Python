n=int(input("Enter the required no.of terms: "))
print("Fibonacci series with",n ,"terms :")
s1=0
s2=1
for i in range(1,n+1):
    print(s1)
    fb=s1+s2
    s1=s2
    s2=fb
