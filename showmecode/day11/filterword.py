import os

def Words(path):
    filterWords=[]
    with open(path, 'r',encoding= 'utf-8') as f:
        for word in f:
            filterWords.append(word.strip('\n'))
        return filterWords

if __name__=='__main__':
    filterwords=Words('filtered_words.txt')
    while(True):
        myinput=input("input your line:").split()
        if set(myinput).intersection(filterwords):
            print('Freedom')
        else:
            print('Human Rights')

