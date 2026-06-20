n=1011
m=n
count=0
while(n>0):
    n=n&(n-1)
    count+=1
print(count)
x=format(m,'b')
print (len(x)-count)