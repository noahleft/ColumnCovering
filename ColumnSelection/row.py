#!/usr/local/bin/python3

class row:
  def __init__(self,data_row):
    self.index=data_row[0]
    self.data=data_row[1:]
  def combine(self,other):
    return list(map(lambda x: self.data[x]+other.data[x],range(len(self.data))))

class gene:
  def __init__(self,gene_seq):
    self.sequence=gene_seq

