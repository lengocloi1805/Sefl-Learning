from operations import OperationToProduct
from menu import *
####################
class AS2_Main:
    def run(self):
        file_name = ""
        operation = OperationToProduct()
        while True:
            print(menu)
            n = int(input())
            if (n == 1):
                print("Choice 1: Load data from file and display")
                print("Please enter the find path:")
                file_name = input().strip()
                operation.case1(file_name)
            elif (n == 2):
                print("Choice 2: Input & add to the end")
                operation.case2()
            elif (n == 3):
                print("Choice 3: Display data")
                operation.case3()
            elif (n == 4):
                print("Choice 4: Save product list to file")
                file_output = input("Please enter the output path:")
                operation.case4(file_output)
                print("The file is saved successfully!")
            elif (n == 5):
                print("Choice 5: Search by ID")
                id = input("Please enter the ID: ")
                operation.case5(id)
            elif (n == 6):
                print("Choice 6: Deleted by ID")
                id = input("Please enter the ID: ")
                operation.case6(id)
            elif (n == 7):
                print("Choice 7: Sorted by ID")
                operation.case7()
            elif (n == 8):
                print("Choice 8: Convert to Binary")
                id = input("Please enter the ID: ")
                operation.case8(id)
            elif (n == 9):
                print("Choice 9: Load to stack and display")
                operation.case9(file_name)
            elif (n == 10):
                print("Choice 10: Load to queue and display")
                operation.case10(file_name)
            elif (n == 0):
                print('Thank!!!')
                break
            else:
                print('Don\'t have option. Please press again!')
                pass
########################
if __name__ == "__main__":
    main = AS2_Main()
    main.run()