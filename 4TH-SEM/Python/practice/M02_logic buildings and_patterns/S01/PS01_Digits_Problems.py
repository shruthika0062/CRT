'''
sample input: 1234
sample output: 4

sample input: 12236
sample output: 5
'''
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1  
print(count)

'''
sample input: 10
sample output: 4

sample input: 14
sample output: 5
'''
num = int(input("Enter a number: "))
sum_digits = 0      
while num > 0:
    digit = num % 10  
    sum_digits += digit  
    num = num // 10
print(sum_digits)

'''
Read a number to display the even digits

sample input: 1234
sample output: 2 4
sample input: 12236
sample output: 2 2 6
'''
n=int(input())
while n>0:
    digit=n%10
    if digit%2==0:
        print(digit,end=" ")
    n=n//10
    
    
'''
reverse the numbers

sample input: 1234
sample output: 4321 

sample input: 12236
sample output: 63221

'''

def reverse_number(num):
    rev = 0
    while num > 0:
        rev = (rev*10)+(num%10)
        num = num//10
    return rev

n=reverse(int(input()))
while n>0:
    digit=n%10
    if digit%2==0:
        print(n%10,end="")
    n=n//10