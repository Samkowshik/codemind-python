n=input()
l=list(map(int,input().split()))
l.sort()
if min(l)<1:
    for i in range(1,max(l)):
        if i not in l:
            print(i)
            break
    else:
        print(max(l)+1)
else:
    print(1)