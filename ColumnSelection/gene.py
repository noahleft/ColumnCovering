#!/usr/local/bin/python3

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
  def dump(self):
    print('gene fitness ',self.calculate_fitness(),end='\t')
    print('gene sequence ',self.sequence)
    print('gene fault distribution',self.getDetailFitness())

