A=list(map(int,input().split()))
B=list(map(int,input().split()))
n=len(A)
m=len(B)
i=0
subString = False
while i<= (n-m):
    if (A[i:i+m]==B):
        subString=True
        break
    i+=1
if (subString):
    print("Yes")
else:
    print("No")




