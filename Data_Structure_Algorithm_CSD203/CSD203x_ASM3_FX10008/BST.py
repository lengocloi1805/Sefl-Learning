class MyBSTree:
    def __init__(self, person):
        self.person = person
        self.left = None
        self.right = None

    def insert(self, person):
        if self.person is not None:
            if person.ID < self.person.ID:
                if self.left is not None:
                    self.left.insert(person)
                else:
                    self.left = MyBSTree(person)
            elif person.ID > self.person.ID:
                if self.right is not None:
                    self.right.insert(person)
                else:
                    self.right = MyBSTree(person)
            else:
                return
        else:
            self.person = person

    def search_person(self, ID):
        if ID < self.person.ID:
            if self.left is None:
                return None
            return self.left.search_person(ID)
        elif ID > self.person.ID:
            if self.right is None:
                return None
            return self.right.search_person(ID)
        return self.person

    # Left -> Root -> Right
    def Inorder(self):
        lst = []
        if self.left is not None:
            lst += self.left.Inorder()
        lst.append(self.person)
        if self.right is not None:
            lst += self.right.Inorder()
        return lst

    def remove(self, ID):
        # check if tree is empty
        if self.person is None:
            print('BST is empty')
            return
        # find the node
        if ID < self.person.ID:
            if self.left is not None:
                self.left = self.left.remove(ID)
            else:
                print('{} is not present in BST'.format(ID))
        elif ID > self.person.ID:
            if self.right is not None:
                self.right = self.right.remove(ID)
            else:
                print('{} is not present in BST'.format(ID))
        # remove that node (three cases - 0, 1, or 2 childs)
        else:
            # if left is None, return right, and vice-versa
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            # find the mind_value in right side of delection node
            node = self.right
            while node.right is not None:
                node = node.right
            self.person = node.person
            self.right = self.right.remove(node.person.ID)
        return self
