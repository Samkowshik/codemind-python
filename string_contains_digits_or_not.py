for t in range(int(input())):
    s=input()
    s=s.replace('@','')
    s=s.replace('.','')
    if s.isalpha():
        print('No')
    else:
        print('Yes')