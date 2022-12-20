n=int(input())
lst=list(map(int,input().split()))
l=[0]*n
l[0]=1 if (lst[0]>lst[1] and lst[1]<lst[2]) or (lst[0]<lst[1] and lst[1]>lst[2]) else 0
for i in range(1,n-1):
    l[i]=1 if (lst[i+1]>lst[i] and lst[i-1]>lst[i]) or (lst[i+1]<lst[i] and lst[i-1]<lst[i])  else 0
l[n-1]=1 if (lst[n-1]>lst[n-2] and lst[n-2]<lst[n-3]) or (lst[n-1]<lst[n-2] and lst[n-2]>lst[n-3]) else 0
a='no' if 0 in l else 'yes'
print(a)