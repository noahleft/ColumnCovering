#!/usr/local/bin/python3
from sys import argv

with open(argv[1],'r') as infile:
  strlines=infile.readlines()

strlines=list(map(lambda x:x.strip('\n'),strlines))
element =list(map(lambda x:x.split(','),strlines))

reverse =list(map(lambda x:[y[x] for y in element],range(len(element[0]))))
rev_strlines=list(map(lambda x: ','.join(x),reverse))

rest=[]
for index in range(len(rev_strlines)):
  strline=rev_strlines[index]
  if not '1' in strline:
    print(strline)
    continue
  if not strline in rev_strlines[index+1:]:
    rest.append(index)

reduced_rev_strlines=list(map(lambda x:rev_strlines[x],rest))
reduced_reverse=list(map(lambda x: x.split(','),reduced_rev_strlines))

element =list(map(lambda x:[y[x] for y in reduced_reverse],range(len(reduced_reverse[0]))))
strlines=list(map(lambda x: ','.join(x),element))

with open(argv[2],'w') as outfile:
  for strline in strlines:
    outfile.write(strline+'\n')




