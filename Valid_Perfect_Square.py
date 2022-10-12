t=int(input())
for i in range (t):
    n=int(input())
    r=n**0.5//1
    if r*r==n:
        print('True')
    else:
        print('False')