import os
from os import listdir
from os.path import isfile, join
from random import randint

min_val = 1
max_val = 9999999999

sig_dig = 10

name = input("Image Type: ")

lst_file = []
lst_count = []
cwd = dir_path = os.path.dirname(os.path.realpath(__file__))

for file in os.listdir(cwd):
    
    print (file)
    lst_file.append(file)
    
count = range(len(lst_file))

for i in count:
    lst_count.append(i)

x=0    
for file in lst_file:
    if not file.endswith('.py'):
        num = (str(randint(min_val,max_val)).zfill(sig_dig))
        os.rename(file,(str(num+'.jpg')))

lst_file = []
lst_count = []
        
for file in os.listdir(cwd):
    
    #print (file)
    lst_file.append(file)
    
count = range(len(lst_file))

for i in count:
    lst_count.append(i)

file_num = 0   
sig_dig = 5 
for file in lst_file:
    if not file.endswith('.py'):
        file_num+=1
        
        os.rename(file,(str(name +" - " +str(file_num).zfill(sig_dig)+'.jpg')))
        print (str(file_num))