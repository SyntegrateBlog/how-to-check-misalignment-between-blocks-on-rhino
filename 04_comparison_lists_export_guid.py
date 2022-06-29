### Copyright (c) 2022 Syntegrate
###
### This software is released under the MIT License.
### https://opensource.org/licenses/MIT


import csv

path6 = 'C:\\Users\\Name\\Desktop\\_data\\blockList_sorted.csv'
path7 = 'C:\\Users\\Name\\Desktop\\_data\\ref_distanceList.csv'
path8 = 'C:\\Users\\Name\\Desktop\\_data\\error_ids.csv'

a = []
b = []


def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def readCsv(path):
    aa = []
    with open (path, 'r', encoding="utf-8") as f:
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
                    new_row.append(ttt)

                #delete empty    
                new_row1 = []    
                for elem in new_row:
                    if elem != '':
                        new_row1.append(elem)

            aa.append(new_row1)
    print(aa)   
    return aa


def comparisonOfTwoLists(refList, list1):
    ids = []

    for i in range(len(list1)): 
        for j in range(len(refList)):

            #search BK
            if list1[i] != refList[j] and len(list1[i]) == len(refList[j]):

                #search only blockname and position
                num = int(len(refList[j]) / 4)

                #check block set in reflist and list
                tmp_ref_set = []
                tmp_list_set = []

                for k in range(num):
                    blcname_id = 1 + k*4

                    bkname_r = str(refList[j][blcname_id])
                    bkname_l = str(list1[i][blcname_id])
                  
                    tmp_ref_set.append(bkname_r)
                    tmp_list_set.append(bkname_l)

                if tmp_ref_set == tmp_list_set:
                    for m in range(num):
                        blcpos_id = 2 + m*4
                        
                        pos_r = float(refList[j][blcpos_id])
                        pos_l = float(list1[i][blcpos_id])

                        if pos_r != pos_l:
                            blcguid = blcpos_id - 2
                            ids.append(list1[i][blcguid])


                            

                        else:
                            pass
                else:
                    pass        
                    
            else:
                pass
                                   
    #print(ids)        
    return ids



def writeCsv(path, list):
    with open (path, 'w') as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerow(list)
    print("done2")



blclist = readCsv(path6)
ref = readCsv(path7)
error_blocks = comparisonOfTwoLists(ref, blclist)
writeCsv(path8, error_blocks)



