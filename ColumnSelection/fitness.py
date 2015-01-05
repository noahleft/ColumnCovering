#!/usr/local/bin/python3

def fitnessFunction(strline):
  return len(list(filter(lambda x: x=='1',strline)))

from random import randint

def oneCutCrossOver(parentPair):
  cutPoint=randint(1,len(parentPair[0])-1) # 49 cut points
  return [parentPair[0][:cutPoint]+parentPair[1][cutPoint:], \
          parentPair[1][:cutPoint]+parentPair[0][cutPoint:]]

from random import random

def uniformCrossOver(parentPair):
  pair=[ round(random()) for x in range(len(parentPair[0]))]
  str1=list(map(lambda x:parentPair[pair[x]][x],range(len(pair))))
  str2=list(map(lambda x:parentPair[::-1][pair[x]][x],range(len(pair))))
  return [str1,str2]

