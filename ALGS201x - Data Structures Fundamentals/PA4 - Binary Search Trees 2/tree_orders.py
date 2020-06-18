# python3
# Input: An integer (n) for the number of vertices
#        Following lines contain the key of the vertex, index of the left child, and the index of the right child
# Output: The keys of the vertices using in-order traversal
#         The keys of the vertices using pre-order traversal
#         The keys of the vertices using post-order traversal

# Set the recursion limit and stack size
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# Wrap all functions into a class
class TreeOrders:
    
    # Read in the data
    def read(self):
      self.n = int(sys.stdin.readline())
      self.key = [0 for i in range(self.n)]
      self.left = [0 for i in range(self.n)]
      self.right = [0 for i in range(self.n)]
      for i in range(self.n):
        [a, b, c] = map(int, sys.stdin.readline().split())
        self.key[i] = a
        self.left[i] = b
        self.right[i] = c

    # In-Order Traversal
    def inOrder(self):
      self.result = []
      current_id = 0
    
      while True:
          if current_id != -1:
              self.result.append(current_id)
              current_id = self.left[current_id]
          elif self.result:
              current_id = self.result.pop()
              yield self.key[current_id]
              current_id = self.right[current_id]
          else:
              break
                 
      return self.result

    # Pre-Order Traversal
    def preOrder(self):
      self.result = []
      current_id = 0
    
      while True:
          if current_id != -1:
              yield self.key[current_id]
              self.result.append(current_id)
              current_id = self.left[current_id]
          elif self.result:
              current_id = self.result.pop()
              current_id = self.right[current_id]
          else:
              break
                  
      return self.result

    # Post-Order Traversal    
    def postOrder(self):
      self.result1 = [0]
      self.result2 = []
    
      while self.result1:
          current_id = self.result1.pop()
          self.result2.append(self.key[current_id])
    
          left_id = self.left[current_id]
          right_id = self.right[current_id]
          if left_id != -1:
              self.result1.append(left_id)
          if right_id != -1:
              self.result1.append(right_id)
    
      while self.result2:
          yield self.result2.pop()

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

# Starts main()
threading.Thread(target=main).start()