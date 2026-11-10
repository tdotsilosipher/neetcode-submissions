# Create node class with list of children and whether if it is end of word
class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # pointer to root 
        cur = self.root
        # for each i in word
        for i in word:
            #  if letter is not in children on current tree
            if i not in cur.children:
                # create a node under current node
                cur.children[i] = TrieNode()
            # go to next node after creating
            cur = cur.children[i]
        # create end point as you reached the end
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return True
        