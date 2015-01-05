#!/usr/local/bin/python3
from OneMax import OneMax

class row:
  def __init__(self,data_row):
    self.index=data_row[0]
    self.data=data_row[1:]
  def combine(self,other):
    self.data=list(map(lambda x: self.data[x]+other.data[x],range(len(self.data))))

class gene:
  def __init__(self,gene_seq,rowList):
    self.sequence=gene_seq
    self.setup(rowList)
  def setup(self,rowList):
    self.data=row([0]+[0]*len(rowList[0].data))
    for index in range(len(self.sequence)):
      if self.sequence[index]=='1':
        self.data.combine(rowList[index])
    return self.calculate_fitness()
  def calculate_fitness(self):
    return len(list(filter(lambda x:x>0,self.data.data)))-sum(self.data.data)/len(self.data.data)
  def getDetailFitness(self):
    return self.data.data
  def dump(self,detail=False):
    print('gene fitness ',self.calculate_fitness(),end='\t')
    print('gene sequence ',len(list(filter(lambda x:x=='1',self.sequence))),'/',len(self.sequence))
    if detail:
      print('gene sequence ',self.sequence)
      print('gene fault distribution',self.getDetailFitness())


class generationList:
  def __init__(self,generationSize,dataSize,dataList,parent,cross):
    self.race=OneMax(population=generationSize,termination=10, \
                     fitnessFunc=lambda x:gene(x,dataList).calculate_fitness(), \
                     parentSelect=parent,crossOver=cross)
    self.race.initialize(dataSize)
  def getLastGeneration(self,dataList):
    return list(map(lambda y:gene(y,dataList),self.race.mattingPool))
  def evolution(self):
    self.race.run()


