s=input()
n=int(input())
l=len(s)
a=s.count('a')
a=(n//l)*a
s=s[:n%l]
a=a+s.count('a')
print(a)