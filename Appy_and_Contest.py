for i in range(int(input())):
    n,a,b,k=map(int,input().split())
    c=0
    for i in range(min(a,b),n+1):
        if (i%a==0 and i%b!=0) or (i%a!=0 and i%b==0):
            c+=1
        if c>=k:
            print('Win')
            break
    else:
        print('Lose')