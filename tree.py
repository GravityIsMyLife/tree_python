class Node:
    def __init__(self):
         self.right = None
         self.left =  None
         self.value = None

    def add(self, val):
        if self.value is None:
            self.value = val
        elif self.value >= val:
            if self.right is None:
                self.right = Node()
            self.right.add(val)
        else:
            if self.left is None:
                self.left = Node()
            self.left.add(val)
    def printTree(self):
        if self.right is not None:
            self.right.printTree()
        print(self.value)
        if self.left is not None:
            self.left.printTree()



def main():
    tree = Node()
    tree.add(1)
    tree.add(10)
    tree.add(20)
    tree.add(2)
    tree.add(5)
    tree.printTree()


if __name__ == '__main__':
    main()