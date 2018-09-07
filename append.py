# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 18:48:31 2018

@author: liupan
"""

f = open(r'File.txt', 'r')
p = open(r'Res.txt', 'w')
res = []

for line in f:
    if line == '\n':
        continue
    res.append(line.strip())
for value in res:
    p.writelines("'" + value + "'" + "," + "\n")
f.close()
p.close()
