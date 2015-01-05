#!/usr/local/bin/python3
from random import getrandbits

class OneMax:
  def __init__(self,population,termination,fitnessFunc, \
               parentSelect,crossOver):
    self.population=population
    self.termination=termination
    self.fitnessFunc=fitnessFunc
    self.parentSelect=parentSelect
    self.crossOver=crossOver
  def initialize(self,dataSize,mattingPool=None):
    if mattingPool:
      self.mattingPool=mattingPool
    else:
      self.mattingPool=list(map(lambda x: '0'*(dataSize-len(bin(x)[2:]))+bin(x)[2:], \
                                [getrandbits(dataSize) for i in range(self.population)]))
    self.bestFitnessRecord=[]
    self.updateFitnessRecord()
  def updateFitnessRecord(self):
    self.bestFitnessRecord.append(max(list(map(self.fitnessFunc, \
                                               self.mattingPool))))
  def selection(self):
    return self.parentSelect(self.mattingPool, \
                             list(map(self.fitnessFunc, \
                                      self.mattingPool)))
  def production(self):
    parentPair=[self.selection() for i in range(2)]
    childPair=self.crossOver(parentPair)
    return childPair
  def run(self):
    for i in range(self.termination):
      print('\r',i,end='')
      self.runEpoch()
  def runEpoch(self):
    newMattingPool=[]
    for i in range(int(self.population/2)):
      newMattingPool.extend(self.production())
    self.mattingPool=newMattingPool
    self.updateFitnessRecord()
  def printOut(self):
    print(self.bestFitnessRecord)
  def writeOut(self,filepath):
    with open(filepath,'a') as outfile:
      outfile.write(','.join(list(map(lambda x:str(x),
                                      self.bestFitnessRecord)))+'\n')
