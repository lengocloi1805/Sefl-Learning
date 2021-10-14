import numpy as np
from menu import *
class Basic_Sorting():
    def save_file(self, arr, file_name):
        st = ', '.join(list(map(str, arr)))
        file_path = open(file_name, 'w')
        file_path.write(st)
        file_path.close()

    def read_file(self, file_name):
        file_path = open(file_name, 'r')
        for line in file_path:
            line = line.split(', ')
            arr = list(map(float, line))
        file_path.close()
        return arr

    def BubbleSort(self, arr):
        arr1 = arr.copy()
        file_path = open('OUTPUT1.TXT', 'w')
        n = len(arr1)
        while n >= 2:
            for i in range(n-1):
                if arr1[i] > arr1[i+1]:
                    arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
            n -= 1
            print(*arr1)
            st = ', '.join(list(map(str, arr1)))
            file_path.write(st + '\n')
        file_path.close()
        return arr1

    def SelectionSort(self, arr):
        arr1 = arr.copy()
        file_path = open('OUTPUT2.TXT', 'w')
        for i in range(len(arr1)):
            min_indx = i
            for j in range(i+1, len(arr1)):
                if arr1[j] < arr1[min_indx]:
                    min_indx = j
            arr1[i], arr1[min_indx] = arr1[min_indx], arr1[i]
            print(*arr1)
            st = ', '.join(list(map(str, arr1)))
            file_path.write(st + '\n')
        file_path.close()
        return arr1

    def InsertionSort(self, arr):
        arr1 = arr.copy()
        file_path = open('OUTPUT3.TXT', 'w')
        for i in range(1, len(arr1)):
            val = arr1[i]
            j = i-1
            while j >= 0 and arr1[j] > val:
                arr1[j+1] = arr1[j]
                j -= 1
            arr1[j+1] = val
            print(*arr1)
            st = ', '.join(list(map(str, arr1)))
            file_path.write(st + '\n')
        file_path.close()
        return arr1

    def LinearSearch(self, arr):
        arr1 = arr.copy()
        file_path = open('OUTPUT4.TXT', 'w')
        lst = []
        value = float(input())
        for i,v in enumerate(arr1):
            if v > value:
                print(i, end=' ')
                lst.append(str(i))
        print()
        st = ', '.join(lst)
        file_path.write(st)
        file_path.close()
        return st

    def BinarySearch(self, arr, value):
        r = len(arr) - 1
        l = 0
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == value:
                return mid
            elif value > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        if l > r:
            return None

###############################
if __name__ == '__main__':
    while True:
        print(menu)
        n = int(input().strip())
        if n == 1:
            print('Choice 1: Manual Input')
            print('Please enter input number of elements:')
            size_of_arr = int(input().strip())
            print('Please enter input elements:')
            arr = list(map(float, input().strip().split()))
        elif n == 2:
            print('Choice 2: File input')
            print('Please enter the file path:')
            name_in = input().strip()
            type_of_sort = Basic_Sorting()
            type_of_sort.save_file(arr, name_in)
            print('Input array:', *type_of_sort.read_file(name_in))
        elif n == 3:
            print('Choice 3: Bubble sort')
            out_arr = type_of_sort.BubbleSort(arr)
        elif n == 4:
            print('Choice 4: Selection sort')
            out_arr = type_of_sort.SelectionSort(arr)
        elif n == 5:
            print('Choice 5: Insertion sort')
            out_arr = type_of_sort.InsertionSort(arr)
        elif n == 6:
            print('Choice 6: Linear Search')
            print('Please enter searched input value:')
            type_of_sort.LinearSearch(arr)
        elif n == 7:
            print('Choice 7: Binary Search')
            print('Please enter searched input value:')
            value = float(input())
            print('The first equal position: ', type_of_sort.BinarySearch(out_arr, value))
        elif n == 0:
            print('Thank!!!')
            break
        else:
            print('Don\'t have option. Please press again!')
            pass
