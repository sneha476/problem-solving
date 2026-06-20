
n=153
sum=0
temp=n
for i in range(len(str(n))):         
    val=temp%10                       #153%10=3, 15%10=5,
    sum+=val**len(str(n))              #3**3+5**3=27+125=152
    temp//10                              #15//10=1 sum=153
if n==sum:                                  #153=153
    print(n,"is armstrong")
else:
    print(n,"is not armstrong")
 