class Node:
  def __init__(self, ten, Cha= None):
    self.ten= ten
    self.Cha = Cha

  def display(self):
    print(self.ten)

from collections import defaultdict
data = defaultdict(list)
data['A'] = ['B','C','D']
data['B'] = ['M','N']
data['C'] = ['L']
data['D'] = ['O', 'P']
data['M'] = ['X','Y']
data['N'] = ['U','V']
data['O'] = ['I','J']
data['Y'] = ['R','S']
data['V'] = ['G','H']

def kiemtra(tam, MO):
  for v in MO:
    if v.ten == tam.ten:
      return True
  return False

def duongdi(n):
  print(n.ten)
  if n.Cha != None:
    duongdi(n.Cha)
  else:
    return

def DFS(to, tg):
  MO= []
  DONG= []
  MO.append(to)

  while True:
    if len(MO) == 0:
      print('Khong tim thay duong di')
      return
    n= MO.pop(0)

    if n.ten == tg.ten:
      print('Tim kiem thanh cong')
      duongdi(n)
      return
    DONG.append(n)

    pos = 0
    for v in data[n.ten]:
      tam = Node(v)
      ok1 = kiemtra(tam, MO)
      ok2= kiemtra(tam, DONG)

      if not ok1 and not ok2:
        MO.insert(pos, tam)
      pos += 1
      tam.Cha = n

DFS(Node('A'), Node('N'))



