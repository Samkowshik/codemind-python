n=int(input())
l=list(map(int,input().split()))
lst=[0]*n
for i in range (n-1):
    for j in range (i+1,n):
        if (l[j]>l[i]):
            lst[i]=j-i
            break
        else:
            j+=1
print(*lst)
