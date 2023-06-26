s=input().lower()
s=s.replace(' ','')
s=list(sorted(set(s)))
print(''.join(s))