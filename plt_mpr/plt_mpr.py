#!/usr/bin/env python
# -*- coding: utf-8 -*-

# """PLATESSSS!"""

## __Import__
import pandas as pd
import os
import glob
import csv
import scipy as sp
import shutil
from bin import nm
import math
from pick import pick


## What would you like to map today?
## set variables / import data

## enter data file of src plates
inp = input('Please specify a tab delineated source file:  ')
a = pd.read_csv(inp, sep='\t')
b = input('Please specify the exact name of the column of plate ids in source file:  ')
c = tuple(a[b].unique())

## select mapping - NB math is made from the choices, format properly 'src/dest'
title = 'Please select a mapping (source / destination): (Space marks, enter continues)'
choices = ['96/384', '384/384'] # should be ported over to external config file ()?)
chc, cdx = pick(choices, title)

## sets variable for map
if cdx == 0:
    map = pd.read_csv('../configs/96to384.csv')
elif cdx == 1:
    map = pd.read_csv('../configs/384to384.csv')

## set x for further def of loops
x = 1/eval(chc)

## number of new plates needed
nw_plts = math.ceil(len(c)/x)

prf = input('Please specify a prefix:  ')
rang = input("Please enter a range for plate names - you need {}  - use a comma and no spaces: ".format(nw_plts))

n2 = tuple(nm.nm_gn1(prf, rang))

## group by
zz = tuple([tuple(c[i:i+4]) for i in range(0, len(c),4)])

## zips/combines
zzz = tuple(zip(n2, zz))

# print(zzz)

## Add lot number column

## MUST FILL IN EMPTY INDEX HEADERS

## inject new id (nid)
## inject plate position (plt_pos)

nm.new_add(zzz, a, b, x)

## calculate new well off old, plt_pos, nid

rr = nm.mapp(a, map)

## save and eject

rr.to_csv('../final.csv', index=False)
