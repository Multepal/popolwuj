#!/usr/bin/env python

import re

COL = re.compile(r'<div xml:lang="(\w+)" type="column">')
PB = re.compile(r'<pb xml:id="([^"]+)"/>')
LB = re.compile(r'<lb n="(\d+)"/>(.*)')

file = "./xom-all-flat-mod-pnums.xml"
newdoc = []
with open(file, 'r') as xml:
    C = P = L = ''
    for line in xml.readlines():
        line = line.strip()
        if COL.match(line):
            m = COL.match(line)
            C = m[1]
            newdoc.append(line)
        elif PB.match(line):
            m = PB.match(line)
            P = m[1]
            newdoc.append(line)
        elif LB.match(line):
            m = LB.match(line)
            L = m[1]
            content = m[2]
            lb_id = '{}-{}-{}'.format(P, C, L)
            newdoc.append('<lb n="{}" id="{}"/>{}'.format(L, lb_id, content))
        else:
            newdoc.append(line)
            
with open('xom-all-flat-mod-pnums-lbids.xml', 'w') as out:
    out.write('\n'.join(newdoc))