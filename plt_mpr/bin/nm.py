#!/usr/bin/env python
# -*- coding: utf-8 -*-

# """PLATESSSS!"""

import pandas as pd

def nm_gn1(pf, rng):
    r = rng.split(',')
    rr = tuple(range(int(r[0]), (int(r[1])+1)))

    pp = list([pf])
    o = pp * len(rr)

    p = []

    for i in rr:
         ii = str(i)
         p.append(ii)

    y = tuple(zip(o, p))

    n2 = []

    for u in y:
        n2.append(''.join(u))

    return(n2)

def new_add(z, a1, b1, x1):
    a1['new_plate'] = a1.index
    a1['plate_pos'] = a1.index

    for i in range(len(a1[b1])):
        for ii in range(len(z)):
            for iii in range(int(x1)):
                if a1[b1][i] == z[ii][1][iii]:
                    a1['plate_pos'][i] = iii + 1
                    a1['new_plate'][i] = z[ii][0]

## returns rr
def mapp(org, mp):
    rr = pd.merge(org, mp, on=['plate_pos', 'position'])
    return(rr)
