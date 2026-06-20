# s=int(input("enter a number:"))
# using%
# if s%2==0:
#     print(s,"is an even number")
# else:
#     print(s,"is an odd number")
# using&
# if s&1==0:
#     print("even")
# else:
#     print("odd")
# using//
# if ((s//2)*2)==s:
#     print("even")
# else:
#     print("odd")
# n=7
# s=str(n)
# if(s[-1]in '0248'):
#     print("even")
# else:
#     print("odd")

# n=6
# s=bin(n)
# print(s)
# print(n<<2)
# print(n>>2)

# x=1010
# print(x<<2)
# print(x<<3)
# print(x<<4)
# a=2
# b=4
# print(a,b)
# a=a^b
# b=a^b
# a=a^b
# print(a,b)
x=10
# s=bin(x)
# count=0
# count=s.count("1")
# print(count)
# l=[]
# while(x>0):
#     l.insert(0,x%2)
#     x//=2
# print(l)
# count=0
# for i in range(len(l)):
#     if(l[i]==1):
#         count+=1
# print(count)


# a^=b
# b^=a
# a^=b
# print(a,b)

#1010110----> find decical number
# binary="1010110"
# value=int(binary,2)
# print(value)
val="1010110"                                      
result=0
# for bit in val:
#     result=result*2+(bit=='1')                  #'1'-->0*2+1=1 ,'0'-->1*2+0=2,'1'-->2*2+1=5,'0'-->5*2+0=10,'1'-->10*2+1=21,'1'-->21*2+1=43,'0'-->43*2+0=86
# print(result)


# for i in range(len(val)):          #length=7  result=0,result=1 then result=1*2=2,result=2*2=4 then result=5,result 5*2=10,result=10*2+1=20
#     result=result*2                 
#     if val[i]=='1':                # val[0]=1  then true then add 1,result=1 , val[1]=0 false result=2,val[2]=1 true the add 1 result=5,val[3]=0 false result=10,
#         result+=1                               #val[4]=1 true add 1 result=21,val[5]=1 true then add1 result=43,val[6]=0 false result=86
# print(result)


# power of 2
n=16
# if n>0:
#     if(n&(n-1)==0):
#         print("power of 2")
#     else:
#         print("not a power of 2")
while n > 1:
    n=n//2
    if n%2==0 or n==1:
        print("Power of 2")
        break
if n%2!=0:
        print("Not Power of 2")
    


    

# count no of 1's and no of 0's
#find position of 1's
