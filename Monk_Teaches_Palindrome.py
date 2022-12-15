for t in range(int(input())):
    s=input()
    s1=s[::-1]
    if s==s1:
        if len(s)%2:
            print('YES ODD')
        else:
            print('YES EVEN')
    else:
        print('NO')