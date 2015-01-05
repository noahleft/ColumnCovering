#!/usr/local/bin/python3

from random import randrange

def RouletteSelection(mattingPool,fitnessRecord):
  counter=randrange(sum(fitnessRecord))
  idx=0
  while(counter>fitnessRecord[idx]):
    counter-=fitnessRecord[idx]
    idx+=1
  return mattingPool[idx]

def TournamentSelection(mattingPool,fitnessRecord):
  idx1=randrange(len(mattingPool))
  idx2=randrange(len(mattingPool))
  if fitnessRecord[idx1]>fitnessRecord[idx2]:
    idx=idx1
  else:
    idx=idx2
  return mattingPool[idx]

