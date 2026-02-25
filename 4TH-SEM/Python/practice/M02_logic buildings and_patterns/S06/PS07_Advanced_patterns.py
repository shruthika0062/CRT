"""
1. pascal triangle
n=5
     1   
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1 

 
n = int(input())
for i in range(1,n+1):
    num = 1
    for j in range(i):
        print(num, end=" ")
        num = num * (i - j - 1) // (j + 1)
    print() 
"""

"""
2.butterfly pattern
n=4
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *
"""

n= int(input())
for i in range(1,n+1):
    print("*"*i + " "*(2*(n-i)) + "*"*i)
for j in range(n,0,-1):
    print("*"*j + " "*(2*(n-j)) + "*"*j)    
    