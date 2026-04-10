input_date=list(input())
a=[int(i) for i in input_date if '0'<=i<='9']
num=0
k=1
for i in a:
    num+=i*k
    k+=1
    if k==10:
        k=0
n=num%11
if n==int(input_date[12]):
    print("Right")
else:
    input_date[12]=str(n)
    print(''.join(input_date))
