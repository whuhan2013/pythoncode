import glob
from collections import Counter
import re

def list_txt():
    return glob.glob("*.txt")

def wc(filename):
    datalist=[]
    with open(filename,'r') as f:
        for line in f:
            content=re.sub("\"|,|\.","",line)
            datalist.extend(content.strip().split(' '))

    return Counter(datalist).most_common(1)

def most_comm():
    alltext=list_txt()
    for text in alltext:
        print(wc(text))

if __name__ == '__main__':
    # most_comm()
    result=map(wc,list_txt())
    for ind,eva in enumerate(result):
        print(ind,eva)

