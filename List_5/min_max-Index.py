A=list(map(int,input().split()))
min_index=1
minimum=A[0]
i=1
while i<len(A):
    if (A[i]<minimum):
        minimum=A[i]
        min_index=i+1
    i+=1
print(min_index)




