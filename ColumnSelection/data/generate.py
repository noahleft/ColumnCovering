#!/usr/local/bin/python3
import random
from sys import argv

print('# of colunm:',argv[1])
print('# of row   :',argv[2])
'''
def randomGen(ratio=0.5):
  tmp=random.random()
  if tmp<ratio:
    return 'X'
  elif tmp>(1-ratio/2):
    return '0'
  else:
    return '1'
'''

def randomGen():
  if random.random()>0.5:
    return '1'
  else:
    return '0'

with open('data.csv','w') as outfile:
  for index in range(int(argv[2])):
    outfile.write(str(index)+',')
    for idx in range(int(argv[1])-1):
      outfile.write(str(randomGen())+',')
    outfile.write(str(randomGen())+'\n')

