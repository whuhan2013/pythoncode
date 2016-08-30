import os

mdir=r'D://Data/git/my_blog'

file_list=os.walk(mdir)

for root,dirs,files in file_list:
    for name in files:
        if name[-3:] == '.py':
            filedir = root + "\\" + name
            print(filedir)