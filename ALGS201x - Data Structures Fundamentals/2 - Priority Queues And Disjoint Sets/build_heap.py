# python3

def Min_Heapify(data, heap_size, index, swaps):
    left = int(2*index + 1)
    right = int(2*index + 2)
    smallest = index
    if left <= heap_size and data[left] < data[index]:
        smallest = left
    if right <= heap_size and data[right] < data[smallest]:
        smallest = right
    if smallest != index:
        swaps.append((index, smallest))
        data[index], data[smallest] = data[smallest], data[index]
        Min_Heapify(data, heap_size, smallest, swaps)
        
def build_heap(data):
    swaps = []
    heap_size = len(data) - 1
    for i in range(int(heap_size//2), -1, -1):
        Min_Heapify(data, heap_size, i, swaps)
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()