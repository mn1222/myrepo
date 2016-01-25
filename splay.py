# TASK:
#
# This is the SplayTree code we saw earlier in the 
# unit. We didn't achieve full statement coverage 
# during the unit, but we will now!
# Your task is to achieve full statement coverage 
# on the SplayTree class. 
# 
# You will need to:
# 1) Write your test code in the test function.
# 2) Press submit. The grader will tell you if you 
#    fail to cover any specific part of the code.
# 3) Update your test function until you cover the 
#    entire code base.
#
# You can also run your code through a code coverage 
# tool on your local machine if you prefer. This is 
# not necessary, however.
# If you have any questions, please don't hesitate 
# to ask in the forums!

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def equals(self, node):
        return self.key == node.key

class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None) #For splay()

    def insert(self, key):
        if (self.root == None):
            self.root = Node(key)
            return

        self.splay(key)
        if self.root.key == key:
            # If the key is already there in the tree, don't do anything.
            return

        n = Node(key)
        if key < self.root.key:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if self.root is None or key != self.root.key:
            return

        # Now delete the root.
        if self.root.left== None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key

    def isEmpty(self):
        return self.root == None
    
    def splay(self, key):
        l = r = self.header
        t = self.root
        if t is None:
            return
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t


# Write test code in this function to achieve 
# full statement coverage on the SplayTree class.
def test():
    ###Your code here.
    splayTree = SplayTree()
    splayTree.remove("auto")
    splayTree.insert("auto")
    splayTree.insert("banane")
    splayTree.insert("auto")
    splayTree.insert("arbeit")
    splayTree.remove("arbeit")
    splayTree.remove("auto")
    splayTree.findMin()
    
    splayTree2 = SplayTree()
    splayTree2.insert(2)
    splayTree2.insert(3)
    splayTree2.insert(4)
    splayTree2.remove(3)
    
    splayTree3 = SplayTree()
    splayTree3.findMin()
    
    splayTree4 = SplayTree()
    splayTree4.insert(1)
    splayTree4.insert(2)
    splayTree4.insert(3)
    splayTree4.findMin()
    splayTree4.findMax()
    splayTree4.isEmpty()
    
    splayTree5 = SplayTree()
    splayTree5.insert(5)
    splayTree5.find(4)
    
    splayTree5 = SplayTree()
    splayTree5.insert(4)
    splayTree5.insert(5)
    splayTree5.find(3)
    
    splayTree5 = SplayTree()
    splayTree5.insert(5)
    splayTree5.find(6)
    
    splayTree5 = SplayTree()
    splayTree5.insert(4)
    splayTree5.insert(3)
    splayTree5.find(5)    
test()

