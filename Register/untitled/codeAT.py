graph = {
    "A": {"B": 2, "C": 4, "F": 6},
    "B": {},
    "C": {"D": 8, "E": 2},
    "D": {},
    "E": {},
    "F": {"G": 5, "H": 1},
    "G": {},
    "H": {}
}

def path_cost(start, goal, parent, g):
  path= []
  current = goal
  while current != start:
    path.append(current)
    current = parent[current]
  path.append(start)
  path.reverse()
  print("Duong di", '->' .join(path))
  print("C(p)=", g[goal])

def AT(graph, start, goals):
  mo= [start]
  g={start:0}
  dong=[]
  parent={}

  while mo:
    min_cost = float('inf')
    n= None
    for vertex in mo:
      cost = g.get(vertex, float('inf'))
      if cost < min_cost:
        min_cost = cost
        n= vertex

    if n in goals:
      path_cost(start, n, parent, g)
      return True
    mo.remove(n)
    dong.append(n)

    for m in graph.get(n, {}):
      cost = graph[n][m]
      new_cost = g[n]+ cost

      if m in g:
        if new_cost <g[m]:
           g[m] = new_cost
           parent[m]= n

      else:
        g[m] = new_cost
        parent[m]= n
        mo.append(m)
  return False


start = "A"
goals = ["D", "H"]
AT(graph, start, goals)
