# python3
# Input: An integer (nodes) for the number of vertices
#        Following lines contain the key of the vertex, index of the left child, and the index of the right child
# Output: "CORRECT" if the tree is a binary search tree, "INCORRECT" if it is not

# Set the recursion and stack size limit
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# Recursively search to verify the tree matches the correct definition 
def IsBinarySearchTree(node, minimum, maximum):
  if not node in tree:
      return True
  
  if tree[node][0] < minimum or tree[node][0] > maximum:
      return False
  
  return IsBinarySearchTree(tree[node][1], minimum, tree[node][0] - 1) and IsBinarySearchTree(tree[node][2], tree[node][0] + 1, maximum)

def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree = {}
  int_max = 2147483647
  int_min = -2147483648
  
  for i in range(nodes):
    tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(0, int_min, int_max):
    print("CORRECT")
  else:
    print("INCORRECT")

# Starts main()
threading.Thread(target = main).start()