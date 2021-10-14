import numpy as np
import pandas as pd

def task1(filename):
    try:
        #Get input file name
        file_object  = open(filename, 'r')
        print('Successfully opened {}'.format(filename[-10:]))
        print()
        return file_object, True
    except:
        print("Sorry, I can't find this file ")
        exit()

def task2(file_object):

    #Remove \n at end of the line using list comprehension and split , from line
    file = [ x.strip().split(',') for x in file_object.readlines()]

    #Count valid and invalid line
    count_valid = 0
    count_invalid = 0

    #Lines valid:
    valid_lines =[]
    for x in file:
        if len(x) != 26 or x[0][0] != 'N' or len(x[0][1:]) != 8 or x[0][1:].isdigit() == False:
            count_invalid +=1
            if len(x) != 26:
                error = 'does not contain exactly 26 values:'
            elif x[0][0] != 'N' or len(x[0][1:]) != 8 or x[0][1:].isdigit() == False:
                error = 'N# is invalid'
            print('Invalid line of data: {} '.format(str(error)))
            print(x)
        else:
            count_valid +=1
            valid_lines.append(x)
    return count_invalid, count_valid, valid_lines

def task3(answer_key, valid_lines):
    #convert string answer_key to list
    answer_key = answer_key.split(',')

    for i in range(len(valid_lines)):
        valid_lines[i].pop(0)
    for x in valid_lines:
        for j in range(len(answer_key)):
            # Answer is ignored
            if x[j] == '':
                x[j] = 0
            # Answer is true
            elif x[j] == answer_key[j]:
                x[j] = 4
            # Answer is false
            else:
                x[j] = -1
    score = np.array(valid_lines)
    total_score = np.sum(score, axis=1)
    DF = pd.DataFrame(total_score).describe()
    DF_tolist = [DF.index.tolist()] + DF.values.tolist()

    #New_dict is a dict contain statistical value ie: count, mean, std, min, max, median
    key_word = DF_tolist[0]
    dict_score = {}
    for i in range(len(key_word)):
        dict_score[key_word[i]] = DF_tolist[i + 1][0]

    mean_score = dict_score['mean']
    max_score = dict_score['max']
    min_score = dict_score['min']
    range_score = max_score - min_score
    median_score = dict_score['50%']
    return mean_score, max_score, min_score, range_score, median_score, total_score

def task4(file_name, ID_student, total_score):
    file_name= file_name.replace('.','_grade.')
    file_name= file_name.replace('Input_data','Output_data')
    f = open(file_name, 'w')
    x = list(zip(ID_student, total_score))
    for a,b in x:
        s = str(a) + ',' + str(b)
        f.write(s +'\n')
    f.close()
###################################################
def main():
    while True:
        filename = input('Enter file name: ')
        file_object, check_error = task1(filename)

        if check_error == True:
            print('**** ANALYZING ****')
            print()
            
            count_invalid, count_valid, valid_lines = task2(file_object)
            ID_student =[x[0] for x in valid_lines]
            if count_invalid == 0:
                print('No errors found')
                print()

            print('**** REPORT ****')
            print()

            print('Total valid lines of data: {}'.format(count_valid))
            print('Total invalid lines of data: {}'.format(count_invalid))
            print()

            answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
            mean_score, max_score, min_score, range_score, median_score, total_score = task3(answer_key, valid_lines)
            print('Mean (average) score: {}'.format(mean_score))
            print('Highest score: {}'.format(max_score))
            print('Lowest score: {}'.format(min_score))
            print('Range of score: {}'.format(range_score))
            print('Median score: {}'.format(median_score))
            task4(filename, ID_student, total_score)
            print('================================ RESTART =============================')

if __name__ == '__main__':
    main()



