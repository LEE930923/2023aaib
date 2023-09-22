a=input()
b=int(a)

if b>=90: ans = 'A'
if 80<=b<90: ans = 'B'
if 70<=b<80: ans = 'C'
if 70<=b<60: ans = 'D'
if b<60: ans = 'F'
print(ans,end='')