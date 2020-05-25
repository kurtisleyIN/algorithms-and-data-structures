# python3
# Input: an integer (n) and a list (a) that has length n, 
# Output: maximum value that can be obtained by multiplying two integers
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

Index1 = 0
for i in range(1,n):
    if a[i] > a[Index1]:
        Index1 = i
        
if Index1 == 0:
    Index2 = 1
else:
    Index2 = 0

for i in range(1,n):
    if i != Index1 and a[i] > a[Index2]:
        Index2 = i
        
result = a[Index1]*a[Index2]
print(result)