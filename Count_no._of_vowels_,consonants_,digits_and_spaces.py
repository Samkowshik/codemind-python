s=input()
vo=['a','e','i','o','u','A','E','I','O','U']
v=c=d=w=0
for i in s:
    if i in vo:
        v+=1
    elif i.isdigit():
        d+=1
    elif i==' ':
        w+=1
    else:
        c+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',w)