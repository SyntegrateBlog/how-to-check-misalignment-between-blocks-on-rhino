### Copyright (c) 2022 Syntegrate
###
### This software is released under the MIT License.
### https://opensource.org/licenses/MIT

import itertools

from rhinoscript.geometry import TextDotText
import rhinoscriptsyntax as rs
import csv
from collections import Counter


path10 = 'C:\\Users\\Name\\Desktop\\_data\\fastener_set_list_id.csv'
path11 = 'C:\\Users\\Name\\Desktop\\_data\\fastener_set_list_id_num.csv'
path12 = 'C:\\Users\\Name\\Desktop\\_data\\fastener_set_list.csv'



#####################################
# get blocks and sort by DIE_SET_ID
#####################################


### Get Block ID
block_ids = rs.GetObjects("select blocks", 4096)



block_set = []
for block_id in block_ids:
    b_set = []
    n = rs.BlockInstanceName(block_id)
    d_id = rs.GetUserText(block_id, "DIE_SET_ID")

    b_set.append(n)
    b_set.append(block_id)
    b_set.append(d_id)

    itertools.chain.from_iterable(b_set)
    block_set.append(b_set)

#print(block_set)
block_set.sort(key=lambda x:x[2])



##############################
# create die set into a list
##############################

die_set_list = []
die_set = []


d_id = 0
for b in block_set:

    if d_id == 0:
        #first time
        d_id = b[2] 
        die_set1 = []
        die_set1.append(b[0])
        die_set1.append(b[1])

        die_set.append(die_set1)
        
    elif d_id == b[2]:
        die_set2 = []
        die_set2.append(b[0])
        die_set2.append(b[1])

        die_set.append(die_set2)
        
    else:
        die_set.sort(key=lambda x:x[0])
        if len(die_set) > 1: 
            die_set_list.append(die_set)

            die_set = []

            d_id = b[2]
            die_set3 = []
            die_set3.append(b[0])
            die_set3.append(b[1])

            die_set.append(die_set3)
        else: 
            die_set = []
            d_id = b[2]
            die_set3 = []
            die_set3.append(b[0])
            die_set3.append(b[1])

            die_set.append(die_set3)

die_set.sort(key=lambda x:x[0])
die_set_list.append(die_set)
#print(die_set_list)




#####################################
# select 1 die set of each of them
#####################################


# die_set_list = [[[BK.. , guid..],[F-.. , guid..],[F-.. , guid..]],[[BK.. , guid..],[F-.. , guid..],[F-.. , guid..]], []..  ]]]
# d_set = [[BK.. , guid..],[F-.. , guid..],[F-.. , guid..]]

purgedList = []
tmp_c2 = []
tmp_c2_all = []

for d_set in die_set_list:

    if tmp_c2 == []:
        t = []
        purgedList.append(d_set)
        for d in d_set:
            t.append(d[0])
        tmp_c2.append(t)
        ###
        tmp_c2_all.append(t)

    else:
        tmp_b1 = []     
        num_b1 = len(d_set)

        for i in range(num_b1):
            tmp_b1.append(d_set[i][0])
        count = 0
        ###
        tmp_c2_all.append(tmp_b1)

        for c2 in tmp_c2:
            if tmp_b1 == c2:
                count += 1
        
        if count == 0:
            purgedList.append(d_set)
            tmp_c2.append(tmp_b1)

#print(tmp_c2_all)
#print(purgedList)

purgedList_flatten = list(itertools.chain.from_iterable(purgedList))


guids = []
for i in range(len(purgedList_flatten)):
    guids.append(purgedList_flatten[i][1])





############################################
# die_set combination and how many die_set
############################################


purgedList_num = []

collect_num_list = Counter(tuple(item) for item in tmp_c2_all).items()
collect_num_list_l = [list(item) for item in collect_num_list]

# tuple to list
for c in collect_num_list_l:
    tmp = []
    cc = list(c[0])
    tmp.append(c[1])
    tmp.extend(cc)
    purgedList_num.append(tmp)

purgedList_num.sort(key=lambda x:(x[1], x[2]))
purgedList_num_str = []
for p in purgedList_num:
    purgedList_num_str.append(str(p))


# die set combinations and the number of sets
#print(purgedList_num)
    





###############################
# write csv
###############################

with open(path10, 'w') as f:
    writer = csv.writer(f, delimiter='\n')
    writer.writerow(guids)



with open(path12, 'w') as f:
    f.write('\n'.join(purgedList_num_str))



