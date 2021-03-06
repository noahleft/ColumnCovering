#!/usr/local/bin/python3

from sys import argv
from gene import row
from gene import gene
from gene import generationList
import random

from parentSelection import RouletteSelection
from parentSelection import TournamentSelection
from fitness import oneCutCrossOver
from fitness import uniformCrossOver

with open(argv[1],'r') as infile:
  strlines=infile.readlines()
  table={'0':0,'1':1}
  element=list(map(lambda x:[x.strip('\n').split(',')[0]]+list(map(lambda y: table[y], x.strip('\n').split(',')[1:])),strlines))
  dataList=list(map(lambda x:row(x),element))

dataSize=len(dataList)
dataLeng=len(dataList[0].data) # not important term
print('There are ',dataSize,' candidate gene.')
print('Generation size ',50)

def binary(i,length):
  s=bin(i)[2:]
  if len(s)<length:
    s='0'*(length-len(s))+s
  return s

### create original generation (race)
#original_generation=[]
#for index in range(5):
#  original_generation.append(gene(binary(random.getrandbits(dataSize),dataSize),dataList))
###

import shelve
db=shelve.open('ec.shelve','r')

#pare=RouletteSelection
pare=TournamentSelection

race=generationList(generationSize=50, \
                    dataSize=dataSize, \
                    dataList=dataList, \
                    parent=pare, \
                    cross=uniformCrossOver, \
                    matting=db['ec'])  # race history
db.close()


def calFitnessList(race):
  return list(map(lambda x: x.calculate_fitness() ,race.getLastGeneration(dataList)))

def dump(race):
  fitnessList=calFitnessList(race)
  for gene in list(sorted(race.getLastGeneration(dataList),key=lambda x: x.calculate_fitness(),reverse=True))[:1]:
    gene.dump(detail=True)

print('original race:')
dump(race)

race.evolution()
print('dumping result')
dump(race)

db=shelve.open('ec.shelve')
db['ec']=race.race.mattingPool
db.close()


race.race.writeOut('ec.csv')


