### Copyright (c) 2022 Syntegrate
###
### This software is released under the MIT License.
### https://opensource.org/licenses/MIT

import rhinoscriptsyntax as rs
import csv


path_ref = 'C:\\Users\\Name\\Desktop\\_data\\fastener_set_list_id.csv'


with open(path_ref, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        rs.SelectObjects(row)



