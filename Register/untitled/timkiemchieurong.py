class Node:
  def __init__(self,ten, cha=None):
    self.ten = ten
    self.cha = cha
  def display(self):
    print(self.ten)

from collections import defaultdict
data = defaultdict(list)
data['A']=['B','C','D']
data['B']=['M','N']
data['C']=['L']
data['D']=['O','P']
data['M']=['X','Y']
data['N']=['U','V']
data['O']=['I','J']
data['Y']=['R','S']
data['V']=['G','H']

def kiemtra(tam,mo):
  for v in mo:
    if v.ten == tam.ten:
      return True
    return False

def duongdi(n):
  print(n.ten)
  if n.cha is not None:
    duongdi(n.cha)
  else:
    return

def BFS(to, tg):
  mo=[]
  dong=[]
  mo.append(to)

  while True:
    if len(mo) == 0:
      print('Khong tim kiem thanh cong')
      return
    n = mo.pop(0)

    if n.ten == tg.ten:
      print('Tim kiem thanh cong')
      duongdi(n)
      return
    dong.append(n)

    for v in data[n.ten]:
      tam= Node(v)
      ok1=kiemtra(tam,mo)
      ok2=kiemtra(tam,dong)

      if not ok1 and not ok2:
        mo.append(tam)
        tam.cha=n

BFS(Node('A'),Node('S'))



