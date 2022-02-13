# python3
# Input: Sequence of integers (HeapArray)
# Output: The number of swaps taken to transform the array into a heap
#         All of the swaps made

def Min_Heapify(HeapArray, HeapSize, Swaps, CurrentNode):
    
    # Set the left/right child nodes and the smallest node
    LeftChild = int(2*CurrentNode + 1)
    RightChild = int(2*CurrentNode + 2)
    Smallest = CurrentNode
    
    # If LeftChild is in the array and it's smaller than CurrentNode, assign it to Smallest 
    if LeftChild <= HeapSize and HeapArray[LeftChild] < HeapArray[CurrentNode]:
        Smallest = LeftChild
    # If RightChild is in the array and it's smaller than CurrentNode, assign it to Smallest 
    if RightChild <= HeapSize and HeapArray[RightChild] < HeapArray[Smallest]:
        Smallest = RightChild
    # If Smallest was reassigned, make note of the swap and make the swap
    # Recursively call the function to complete the appropriate swaps
    if Smallest != CurrentNode:
        Swaps.append((CurrentNode, Smallest))
        HeapArray[CurrentNode], HeapArray[Smallest] = HeapArray[Smallest], HeapArray[CurrentNode]
        Min_Heapify(HeapArray, HeapSize, Swaps, Smallest)
        
def build_heap(HeapArray):
    # Initialize the swaps array and heap size
    Swaps = []
    HeapSize = len(HeapArray) - 1
    
    # Loop backwards from HeapSize to -1
    for CurrentNode in range(int(HeapSize//2), -1, -1):
        Min_Heapify(HeapArray, HeapSize, Swaps, CurrentNode)
    return Swaps

def main():
    n = int(input())
    HeapArray = list(map(int, input().split()))
    assert len(HeapArray) == n

    Swaps = build_heap(HeapArray)

    print(len(Swaps))
    for i, j in Swaps:
        print(i, j)

if __name__ == "__main__":
    main()