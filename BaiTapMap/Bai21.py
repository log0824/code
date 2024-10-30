class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def Add(self, word):
        node = self.root
        for c in word:
            if c not in node.child:
                 node.child[c] = TrieNode()
            node = node.child[c]
            node.count += 1
    
    def count_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.child:
                return 0
            node = node.child[c]
        return node.count
    
trie = Trie()
contacts = ["Codelearn", "Codewar"]
names = ["Code", "Codel", "io"]
for contact in contacts:
    trie.Add(contact)
l = []
for name in names:
    l.append(trie.count_prefix(name))

print(l)