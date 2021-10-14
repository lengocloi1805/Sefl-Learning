from menu import *
from myperson import *
######################
class ASM3_main:
    def run(self):
        file_name = ""
        call = MyPerson()
        while True:
            print(menu)
            n = int(input())
            if (n == 1):
                print("Choice 1: Load data from file and display")
                print("Please enter the find path:")
                file_name = input().strip()
                call.load_file(file_name)     
            elif (n == 2):
                print("Choice 2: Insert a new Person")
                call.add_person()
            elif (n == 3):
                print("Choice 3: Inorder traverse")
                call.InorderTraversal()
            elif (n == 4):
                print("Choice 4: Breadth-First Traversal traverse")
                call.BFS()
            elif (n == 5):
                print("Choice 5: Search by Person ID")
                ID = input("Please insert the ID:")
                call.Search_ID(ID)
            elif (n == 6):
                print("Choice 6: Delete by Person ID")
                ID = input('Please insert the ID: ')
                call.remove_ID(ID)
            elif (n == 0):
                print('Thank!!!')
                break
            else:
                print('Don\'t have option. Please press again!')
                pass
##############################
if __name__ == '__main__':
    main = ASM3_main()
    main.run()