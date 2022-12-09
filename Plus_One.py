n=int(input())
lst=[i for i in input().split()]
a=''
for i in lst:
    a+=i
a=str(int(a)+1)
for i in a:
    print(i,end=" ")
