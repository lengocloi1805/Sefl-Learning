class Node:
    def __init__(self,product):
        self.product = product
        self.next = None
        self.pre = None

class MyList:
    def __init__(self):
        self.start = None

    def setStart(self,node):
        self.start = node

    def getStart(self):
        return self.start

    def sort(self):
        current = self.start
        index = None
        if (self.start is None):
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if (current.product.id > index.product.id):
                        temp = current.product
                        current.product = index.product 
                        index.product = temp
                    index = index.next
                current = current.next
        self.printProduct()
          
    def printProduct(self):
        fNode = self.start
        print("ID | Title | Quantity | Price ")
        while fNode is not None:
            print(fNode.product.id," | ", fNode.product.title, " | ", fNode.product.quantity , " | ",fNode.product.price)
            fNode = fNode.next 

    def saveFile(self,file):
        fh = open(file,"w")
        fh.write("ID | Title | Quantity | Price \n")
        fNode = self.start
        while fNode is not None:
            fh.write(fNode.product.id +" | " + fNode.product.title + " | " +str(fNode.product.quantity) + " | " + str(fNode.product.price) + "\n")
            fNode = fNode.next
        fh.close()
