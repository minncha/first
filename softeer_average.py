import sys

n,k = map(int, input().split())
s=list(map(int, input().split()))

for i in range(k):
    a,b = map(int,input().split())
  
    average = sum(s[a-1:b])/(b-a+1)
    
    print("%0.2f"%average)
    
    print("ddd")