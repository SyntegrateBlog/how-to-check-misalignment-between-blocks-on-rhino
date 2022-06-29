### Copyright (c) 2022 Syntegrate
###
### This software is released under the MIT License.
### https://opensource.org/licenses/MIT


import rhinoscriptsyntax as rs
import itertools



class Dev():
    
    
    def convert_R0R1R2R3_to_matrix(self, r):
        
        ### R0R1R2R3 >>> 4x4
        ### R0=(-0.24928482690902,0,0.968430211772093,-7200.92422833453), R1=(0,1,0,1580.10445128621), R2=(-0.968430211772093,0,-0.24928482690902,15686.4604485356), R3=(0,0,0,1)
        rr = r.split(" ")
        
        mat = []
        for i in xrange(len(rr)):
            tmp = rr[i]
           
            ### Remove R0=(, )
            _head, elm = tmp.split("(")
            elm, _footer = elm.split(")")
            elms = elm.split(",")
            
            ### Cast (str to int)
            new_elms = []
            for e in elms:
                new_elms.append(float(e))
           
            # print(new_elms)
            mat.append(new_elms)
        
        return mat


    def matrixes_to_position(self, matrixes):
        
        ### Calc Position
        pos = []
            
        p = []
        for j in xrange(len(matrixes)):
            v = matrixes[j]

            ### X, Y, Z
            if j < 3: 
                vv = v[3]
                # print(vv[3])
                p.append(vv)
            
        pos.append(p)

        return pos



def def_path(name):
    if name == "Ref_List":
        return ("C:\\Users\\Name\\Desktop\\_data\\ref_blockList.csv")
    elif name == "Check_List":
        return ("C:\\Users\\Name\\Desktop\\_data\\blockList.csv")


###
paths = ["Check_List", "Ref_List"]

selpath = rs.ListBox(paths, "select ref or list")
p = def_path(selpath)
print(p)




dv = Dev()

### Get Block ID
block_ids = rs.GetObjects("select blocks", 4096)

### Get Block Info

block_set = []
for block_id in block_ids:
    b_set = []
    n = rs.BlockInstanceName(block_id)
    m = str(rs.BlockInstanceXform(block_id))

    mat = dv.convert_R0R1R2R3_to_matrix(m)
    pos = dv.matrixes_to_position(mat)

    d_id = rs.GetUserText(block_id, "DIE_SET_ID")

    b_set.append(str(block_id))
    b_set.append(n)
    b_set.append(pos[0][0])
    b_set.append(pos[0][1])
    b_set.append(pos[0][2])
    b_set.append(d_id)

    itertools.chain.from_iterable(b_set)
    block_set.append(str(b_set))


#print(block_set)


with open(p, mode='w') as f:
    f.write('\n'.join(block_set))


