# python3
# Input: An integer (n) that denotes the length of the sequence
#        A sequence of integers (Pairwise)
# Output: The maximum value that can be obtained by multiplying two integers from the sequence

n = int(input())
Pairwise = [int(x) for x in input().split()]
assert(len(Pairwise) == n)

# Initialize first element of array as the largest
# Loop through the array to find the index with the largest element
Index1 = 0
for i in range(1,n):
    if Pairwise[i] > Pairwise[Index1]:
        Index1 = i

# Initialize Index2 dependent on the value of Index1
if Index1 == 0:
    Index2 = 1
else:
    Index2 = 0

# Loop through the array to find the index with the largest element that ISN'T Index1
for i in range(1,n):
    if i != Index1 and Pairwise[i] > Pairwise[Index2]:
        Index2 = i
        
print(Pairwise[Index1]*Pairwise[Index2])