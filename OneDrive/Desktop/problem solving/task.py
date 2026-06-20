s="1011"                                     
result=0
for i in range(len(s)):          #length=7  result=0,result=1 then result=1*2=2,result=2*2=4 then result=5,result 5*2=10,result=10*2+1=20
    result=result*2                 
    if s[i]=='1':                # val[0]=1  then true then add 1,result=1 , val[1]=0 false result=2,val[2]=1 true the add 1 result=5,val[3]=0 false result=10,
        result+=1                               #val[4]=1 true add 1 result=21,val[5]=1 true then add1 result=43,val[6]=0 false result=86
print(result)
print("power of result:",result**2)
if result>0:                          #86>0 then true
    if (result&(result-1))==0:       #(86&(86-1)) --> 86&85 --> 1010110 &1010101=1010100=84 false  then print not power of two
        print("Power of 2")
    else:
        print("Not Power of 2")        #index:0 1 2 3 4 5 6  
ones=s.count('1')                     # val=1 0 1 0 1 1 0    1--> yes(1),0--> no,1-->yes(2),0--> no,1-->yes(3),1-->yes(4),0-->no   =4
zeros=s.count('0')                                           #1-->no,0--> yes(1),1-->no,0-->yes(2),1-->no,1-->no,0-->yes(3)   =3
print( "no of 1's:",ones)      #4
print("no of 0's:",zeros)      #3                                   index:0 1 2 3 4 5 6   
for i in range(len(s)):      #7-->0,1,2,3,4,5,6                     val=1 0 1 0 1 1 0 
    if(s[i]=='1'):            #val[0]=1 true then print 0,val[1]=0 false,val[2]=1 true print 2,val[3]=0 false, val[4]=1 true print 4, val[5]=1 true print 5,val[6]=0 false 
        print(i)

