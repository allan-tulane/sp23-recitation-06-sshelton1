import math, queue
from collections import Counter

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
      # TODO
      x = p.get()
      y = p.get()
      z = TreeNode(x,y,(x.data[0] + y.data[0], ''))
      p.put(z)
        
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
  # TODO - perform a tree traversal and collect encodings for leaves in code
  if node.left != None:
    # prefix += '0'
    get_code(node.left,prefix+'0',code)
  if node.right != None:
    # prefix += '1'
    get_code(node.right,prefix+'1',code)
  if node.right == None and node.left == None:
    code[node.data[1]] = prefix
  return code

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
  # TODO
  cost = 0
  val_list = f.keys()
  length = len(val_list)
  bits = int(math.log(length,2)) + 1
  for i in f.values():
    cost += bits * i
  return cost

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
  cost = 0
  for i in f.keys():
    bits = len(C[i])
    quant = f[i]
    cost += bits * quant
  return cost


print("For f1.txt:")
f1 = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f1))
T1 = make_huffman_tree(f1)
C1 = get_code(T1)
print("Huffman cost:  %d" % huffman_cost(C1, f1))

print("\nalice29.txt:")
f2 = get_frequencies('alice29.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f2))
T2 = make_huffman_tree(f2)
C2 = get_code(T2)
print("Huffman cost:  %d" % huffman_cost(C2, f2))

print("\nFor asyoulik.txt:")
f3 = get_frequencies('asyoulik.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f3))
T3 = make_huffman_tree(f3)
C3 = get_code(T3)
print("Huffman cost:  %d" % huffman_cost(C3, f3))

print("\nFor fields.c:")
f4 = get_frequencies('fields.c')
print("Fixed-length cost:  %d" % fixed_length_cost(f4))
T4 = make_huffman_tree(f4)
C4 = get_code(T4)
print("Huffman cost:  %d" % huffman_cost(C4, f4))

print("\nFor grammar.lsp:")
f5 = get_frequencies('grammar.lsp')
print("Fixed-length cost:  %d" % fixed_length_cost(f5))
T5 = make_huffman_tree(f5)
C5 = get_code(T5)
print("Huffman cost:  %d" % huffman_cost(C5, f5))
