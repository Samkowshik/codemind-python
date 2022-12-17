n=int(input())
l,x=[],0
for i in range(n):
    s=input()
    l.append(s)
for i in l:
    if '+' in i:
        x+=1
    else:
        x-=1
print(x)