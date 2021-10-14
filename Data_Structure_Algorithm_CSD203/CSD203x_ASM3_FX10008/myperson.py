from BST import *
from person import *
from queuee import *
#####################
class MyPerson:
    def __init__(self):
        self.MyBSTree = MyBSTree(None)
        self.MyQueue = MyQueue()
    
    def load_file(self, file_name):
        try:
            file_path = open(file_name, 'r', encoding='utf8')
            file_path.readline()
            for line in file_path:
                arr = list(line.strip().split(','))
                person = Person1(arr[0], arr[1], arr[2], arr[3])
                self.MyBSTree.insert(person)
            print("The file is loaded successfully!")
        except:
            print("File path is correct!")

    def add_person(self):
        IDExist = True
        ID = None
        while IDExist:
            ID = input("Please insert the new ID:")
            #  Check ID is existed
            person = self.MyBSTree.search_person(ID)
            if person is None:
                IDExist = False
            else:
                print("This ID has been chosen, please choose anothor ID!")
        name = input("Please insert the Name:")
        birth_place = input("Please insert the Birthplace:")
        birth_of_date = input("Please insert the Birth of Date:")
        person = Person1(ID, name, birth_of_date, birth_place)
        # Add to Tree
        self.MyBSTree.insert(person)
        print("New ID:", person.ID)
        print("Name:", person.Name)
        print("Birthplace:", person.BirthPlace)
        print("Date of birth:", person.DayofBirth)
        input('Please type anything to come back to the main menu!')

    def InorderTraversal(self):
        lst = self.MyBSTree.Inorder()
        print("ID | Name | Day of Birth | Birthplace")
        for person in lst:
            person.printx()
        input('Please type anything to come back to the main menu!')
        
    def BFS(self):
        print("ID | Name | Day of Birth | Birthplace")
        if self.MyBSTree is None:
            return 
        self.MyQueue.add(self.MyBSTree)
        # Loop Queue and Print
        while self.MyQueue.peek() is not None:
            current_node = self.MyQueue.remove()
            current_node.person.printx()
            if (current_node.left is not None):
                self.MyQueue.add(current_node.left)
            if (current_node.right is not None):
                self.MyQueue.add(current_node.right)
        input("Please type anything to come back to the main memu")

    def Search_ID(self, ID):
        print("Search for ID = ", ID)
        person = self.MyBSTree.search_person(ID)
        if person is not None:
            print("ID | Name | Day of Birth | Birthplace")
            person.printx()
        else:
            print("The searched ID is not valid")
        input("Please type anything to come back to the main memu")

    def remove_ID(self,ID):
        personFound =  self.MyBSTree.search_person(ID)
        if personFound is not None:
            self.MyBSTree.remove(ID)
            print("Delete the person with the ID = ", ID)
            print("ID | Name | Day of Birth | Birthplace")
            personFound.printx()
        else:
            print("The searched ID is not valid")
        input("Please type anything to come back to the main memu")