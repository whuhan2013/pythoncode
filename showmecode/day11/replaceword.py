import os

def Words(path):
    filterWords=[]
    with open(path, 'r',encoding= 'utf-8') as f:
        for word in f:
            filterWords.append(word.strip('\n'))
        print(filterWords)
        return filterWords

if __name__=='__main__':
    filterwords=Words('filtered_words.txt')

    while(True):
        myinput=input("input your line:")

        for word in filterwords:
            if word in myinput:
                myinput=myinput.replace(word,''.join(['*' for x in range(len(word))]))

        print(myinput)