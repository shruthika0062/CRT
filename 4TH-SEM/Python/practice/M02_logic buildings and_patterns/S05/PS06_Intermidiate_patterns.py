#Intermediate patterns
'''
--->sample input:[1,2,3,4,5 ]
   sample output: [1,4,9,16,25]
   '''  

li = [1,2,3,4,5]
#output : [1,4,9,16,25]
res =[]
for i in li:
    res.append(i**2)
print(res)

"""
--->sample input:[1,2,3,4,5 ]
   sample output: [2,,4]
"""
li = [1,2,3,4,5]
#output : [2,4]
res =[]
for i in li:
    if i%2==0:
        res.append(i)
print(res)

"""
sample input:['a','b','c']
sample output: 'a b c'
"""
li = ['a','b','c']
#output : 'a b c'   
res = ''
for i in li:
    res += i + ' '
print(res.strip())

    
"""
Pyramid pattern
n=4
       *
      * *
     * * *
    * * * *
"""
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i )

    """
    number pyramid
    n=4
       1
      1 2
     1 2 3  
    1 2 3 4
    """
    n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(str(x) for x in range(1, i + 1)))    
    