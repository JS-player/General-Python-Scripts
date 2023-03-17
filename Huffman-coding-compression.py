import heapq
from collections import defaultdict

#Now, let's define a class for `Node` in the huffman tree as below:

class Node:
    def __init__(self, probability, symbol=None, left=None, right=None):
        self.symbol = symbol
        self.probability = probability
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.probability < other.probability


#Now, let's write a function to build the huffman tree:

def build_tree(probabilities):
    queue = [Node(probability, symbol) for symbol, probability in probabilities.items()]
    heapq.heapify(queue)

    while len(queue) > 1:
        left = heapq.heappop(queue)
        right = heapq.heappop(queue)
        heapq.heappush(queue, Node(left.probability + right.probability, left=left, right=right))

    return heapq.heappop(queue)

#Now, let's write a function to traverse the huffman tree and obtain the codes:

def traverse_tree(node, code, huffman_codes):
    if node.symbol is not None:
        huffman_codes[node.symbol] = code
    else:
        traverse_tree(node.left, code + "0", huffman_codes)
        traverse_tree(node.right, code + "1", huffman_codes)

#Now, let's write the main function that returns the huffman codes for a given probability distribution:

def get_huffman_codes(probabilities):
    tree = build_tree(probabilities)
    huffman_codes = defaultdict(str)
    traverse_tree(tree, "", huffman_codes)
    return dict(huffman_codes)

#Now, let's test our script with an example:

if __name__ == "__main__":
    probabilities = {
        "a": 0.5,
        "b": 0.25,
        "c": 0.15,
        "d": 0.08,
        "e": 0.02
    }
    
    huffman_codes = get_huffman_codes(probabilities)
    
    print("Huffman codes:")
    for symbol, code in huffman_codes.items():
        print(f"{symbol}: {code}")
