# -*- coding:utf-8 -*-
import os

map={}
map['blank'] = 0
map['annotation'] = 0
map['all'] = 0

#mdir=r'D://Data/git/my_blog/'
mdir=r'D:\Dowload\NewDoladFile\python-master'

file_list=os.walk(mdir)

def parse_file(filedir):
    if filedir[-3:]=='.py':
        with open(filedir,'r',encoding= 'utf-8') as h:
            allLines = h.readlines()
            print("file:",filedir,"行数为:",len(allLines))
            for line in allLines:
                line=line.strip()
                if line=='':
                    map['blank']+=1
                elif line[0]=='#':
                    map['annotation']+=1
            map['all']+=len(allLines)

for root,dirs,files in file_list:
    for name in files:
        filedir=root+"\\"+name
        parse_file(filedir)

print(map)



