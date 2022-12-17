def p(n):
    if n>4:
        return n%4
    else:
        return n
s=input()
u=s.count('U')
d=s.count('D')
l=s.count('L')
r=s.count('R')
u=p(u)
d=p(d)
l=p(l)
r=p(r)
print(u==d and l==r)