for t in range(int(input())):
    n=input()
    a=int(max(n))
    b=int(min(n))
    if a-b==len(n)-1:
        print('YES')
    else:
        print('NO')