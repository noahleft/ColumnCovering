#!/usr/local/bin/python3

from sys import argv
from row import row

with open(argv[1],'r') as infile:
  strlines=infile.readlines()
  table={'0':0,'1':1}
  element=list(map(lambda x:[x.strip('\n').split(',')[0]]+list(map(lambda y: table[y], x.strip('\n').split(',')[1:])),strlines))
  dataList=list(map(lambda x:row(x),element))

dataSize=len(dataList)
dataLeng=len(dataList[0].data) # not important term
print('There are ',dataSize,' candidate gene.')




