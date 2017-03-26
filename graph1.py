v = 1
graph = {}
while v != 0:
    v = int(input('Podaj wierzcholek lub 0: '))
    if v != 0:
        graph[v] = []
e = 1
while e != 0:
    e = int(input('Podaj poczatek krawedzi lub 0: '))
    if e != 0:
        f = int(input('Podaj koniec krawedzi krawedzi: '))
        if e not in graph[f]:
            graph[e].append(f)
            graph[f].append(e)
print("\n")
for wierzcholek in graph.keys():
    print("Stopien wierzcholka {0} = {1}".format(wierzcholek, len(graph[wierzcholek])))
stopien = 0
for wierzcholek in graph.keys():
    if len(graph[wierzcholek]) > stopien:
        stopien = len(graph[wierzcholek])
print("Stopien grafu to: {0}".format(stopien))
