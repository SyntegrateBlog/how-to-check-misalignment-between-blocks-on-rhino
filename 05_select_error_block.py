### Copyright (c) 2022 Syntegrate
###
### This software is released under the MIT License.
### https://opensource.org/licenses/MIT


import rhinoscriptsyntax as rs
import csv

path_error = 'C:\\Users\\Name\\Desktop\\_data\\error_ids.csv'



with open(path_error, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        rs.SelectObjects(row)


