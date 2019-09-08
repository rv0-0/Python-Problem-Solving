"""Question:Lets say you have array A[0]=1 A[1]=-1 ....A[n]=x
Then what would be the smartest way to find out the number of times when A[i]+A[j] is even where i < j
So if we have {1,2,3,4,5} we have 1+3 1+5 2+4 3+5 = 4 pairs which are even.
output -1 if number of pairs are >= 10e9"""

l=list(map(int,input().split(" ")))
odd=even=0
for i in l:
    if(i%2==0):
        even+=1
    else:
        odd+=1
i=(odd*(odd-1)/2)+(even*(even-1)/2)
if(i>1000000000):
    print(-1)
else:
    print(int(i))
