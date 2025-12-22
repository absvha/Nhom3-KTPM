def path_cost(start , goal, parent, g):
  path=[]
  current = goal
  while current != start:
    path.append(current)
    current = parent[current]
  path.append(start)
  path.reverse()
  print("Duong di", '->'.join(path))
  print("C(p)=", g[goal])

def A_start(graph, start, goals):
  mo= [start]
  g = {start:0}
  dong=[]
  f={start: h(start)}
  parent = {}

  while mo:
    min_f = float('inf')
    min_node = None
    for node in mo:
      if f[node]< min_f:
        min_f = f[node]
        min_node = node
    n= min_node

    if n in goals:
      path_cost(start, n, parent, g)
      print(parent)
      return True

    mo.append(n)
    dong.append(n)

    for m, cost_g, cost_h in graph.get(n, []):
      cost_g_new= g[m]+ cost_g
      if m not in mo and m not in dong:
        g[m] = cost_g_new
        f[m]= g[m] + cost_h
        parent[m]= n
        mo.append(m)

      elif m in mo and g[m]>cost_g_new:
        g[m] = cost_g_new
        f[m] = g[m] + cost_h
        parent[m] =n

  return False

