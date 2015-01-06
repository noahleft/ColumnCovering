#!/usr/local/bin/python3
from OneMax import OneMax

class row:
  def __init__(self,data_row):
    self.index=data_row[0]
    self.data=data_row[1:]
  def combine(self,other):
    self.data=list(map(lambda x: self.data[x]+other.data[x],range(len(self.data))))
  def combineMult(self,others):
    self.data=list(map(lambda x: sum([others[y].data[x] for y in range(len(others))]),range(len(self.data))))


class gene:
  def __init__(self,gene_seq,rowList):
    self.sequence=gene_seq
    self.setup(rowList)
  def setup(self,rowList):
    ones=list(filter(lambda index: self.sequence[index]=='1',list(range(len(self.sequence)))))
    self.data=row([0]+[0]*len(rowList[0].data))
    rows=list(map(lambda x:rowList[x],ones))
    self.data.combineMult(rows)
    return self.calculate_fitness()
  def calculate_fitness(self):
    #return len(list(filter(lambda x:x>0,self.data.data)))-sum(self.data.data)/len(self.data.data)
    #return len(list(filter(lambda x:x>0,self.data.data)))-len(list(filter(lambda y:y=='1',self.sequence)))/len(self.sequence)
    fault=  len(list(filter(lambda x:x>0,self.data.data)))/len(self.data.data)
    pattern=len(list(filter(lambda y:y=='0',self.sequence)))/len(self.sequence)
    bias=   int(fault)
    if bias==1:
      return 100*(2*bias+pattern)
    else:
      return len(list(filter(lambda x:x>0,self.data.data)))/len(self.data.data)*100-len(list(filter(lambda y:y=='1',self.sequence)))/len(self.sequence)
      return 100*(fault+0.1*pattern)
  def getDetailFitness(self):
    return self.data.data
  def dump(self,detail=None):
    print('gene fitness ',self.calculate_fitness(),end='\t')
    print('gene sequence ',len(list(filter(lambda x:x=='1',self.sequence))),'/',len(self.sequence))
    if detail:
      print('gene sequence ',self.sequence)
      print('gene fault distribution',self.getDetailFitness())


class generationList:
  def __init__(self,generationSize,dataSize,dataList,parent,cross,matting=None):
    self.race=OneMax(population=generationSize,termination=100, \
                     fitnessFunc=lambda x:gene(x,dataList).calculate_fitness(), \
                     parentSelect=parent,crossOver=cross)
    self.race.initialize(dataSize,matting)
  def getLastGeneration(self,dataList):
    return list(map(lambda y:gene(y,dataList),self.race.mattingPool))
  def evolution(self):
    self.race.run()


