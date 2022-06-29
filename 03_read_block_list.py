### Copyright (c) 2022 Syntegrate
###
### This software is released under the MIT License.
### https://opensource.org/licenses/MIT

import csv
import numpy as np
import pandas as pd
from tkinter import *



a = []
b = []

def isfloat(string):
    try:
        float(string)
        return True

    except ValueError:
        return False





def readCsv(path):
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            new_row = []
            for i in range(len(row)):
                #cleanup list elm
                r = str(row[i])
                
                r1 = r.replace("'", "")
                r2 = r1.replace("[", "")
                r3 = r2.replace("]", "")
                
                bool = isfloat(r3)
                
                if bool is True:
                    ff = float(r3)
                    new_row.append(ff)
                else:
                    tt = str(r3)
                    ttt = tt.strip()
                    #print(ttt)
                    new_row.append(ttt)
            
            a.append(new_row)

    a.sort(key=lambda x:x[5])
    for i in range(len(a)):
        if "BRACKET" in a[i][1]:
            b.append(a[i]) 

    return a, b



def writeCsv(path, list):
    with open (path, 'w') as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerow(list)
    print("done")


def myRound(val, digit=0):
     p = 10 ** digit
     return (val * p * 2 + 1) // 2 /p



def sortList(list1, list2):
    distList = []
    set_id = 0

    for l2 in list2:
        id = l2[5]
        pt0 = np.array([l2[2], l2[3], l2[4]])
        bk = l2[1]
        d_fas = []
        for l1 in list1:
            d_bk = []
            # if DIE_SET_ID is same
            if l1[5] == id:
                
                pt = np.array([l1[2], l1[3], l1[4]])
                d = np.linalg.norm(pt0-pt)
                d = myRound(d, 1)

                #d_bk.append(bk)
                d_bk.append(l1[0])
                d_bk.append(l1[1])
                d_bk.append(d)
                d_bk.append(set_id)
            
            d_fas.append(d_bk)

        #delete empty
        d_fas_clean = list(filter(None, d_fas))
        d_fas_clean.sort(key=lambda x:x[1])
        
        distList.append(d_fas_clean)
        set_id += 1

 

    #print(distList)
    return distList



###select ref blocks or check blocks

root = Tk()
root.geometry('500x150')

listbox = Listbox(root, width=300, height=50, selectmode='single')

listbox.insert(1, "Check_List")
listbox.insert(2, "Ref_List")

def selected_item():
    for i in listbox.curselection():
        global selected
        selected = listbox.get(i)
        root.destroy()


def def_path2(name):
    
    path1 = 'C:\\Users\\Name\\Desktop\\_data\\blockList.csv'
    path2 = 'C:\\Users\\Name\\Desktop\\_data\\blockList_sorted.csv'
    path3 = 'C:\\Users\\Name\\Desktop\\_data\\ref_blockList.csv'
    path4 = 'C:\\Users\\Name\\Desktop\\_data\\ref_distanceList.csv'

    Check_List = [path1, path2]
    Ref_List = [path3, path4]
    if name == "Ref_List":
        return Ref_List
    elif name == "Check_List":
        return Check_List
        

btn = Button(root, text='select', command=selected_item)
btn.pack(side='bottom')
listbox.pack()

root.mainloop() 

path_list = def_path2(selected)
print(path_list)






##########################

readCsv(path_list[0]) #create 2 lists

distanceList = sortList(a, b)
writeCsv(path_list[1], distanceList)





