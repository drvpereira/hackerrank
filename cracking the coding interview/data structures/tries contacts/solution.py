class Node(object):
    
    __slots__ = ['count', 'children']
    
    def __init__(self):
        self.children = {}
        self.count = 0
    
    def add_char(self, char):
        if char not in self.children:
            node = Node()
            self.children[char] = node
        else:
            node = self.children[char]

        node.count += 1
        return node
    
    def add(self, string):
        index = 0
        node = self
        while index < len(string):
            node = node.add_char(string[index])
            index += 1
    
    def find(self, string):
        index = 0
        node = self
        
        while index < len(string):
            char = string[index]     
            if char in node.children:
                node = node.children[char]
            else:
                return 0
            index += 1
            
        return node.count

n = int(input().strip())
trie = Node()

for _ in range(n):
    op, contact = input().strip().split(' ')
    
    if op == 'add':
        trie.add(contact)
    elif op == 'find':
        print(trie.find(contact))
    