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

def spojny(sprawdzany_graph):
    new_graph = [sprawdzany_graph.keys()[0]]
    queue = [sprawdzany_graph.keys()[0]]
    checked = []
    while True:
        try:
            wierzcholek = queue.pop()
            checked.append(wierzcholek)
        except IndexError:
            break
        for polaczenie in sprawdzany_graph[wierzcholek]:
            if polaczenie not in new_graph:
                new_graph.append(polaczenie)
            if polaczenie not in checked and polaczenie not in queue:
                queue.append(polaczenie)
    for wierzcholek in sprawdzany_graph.keys():
        if wierzcholek not in new_graph:
            return False
    return True

for wierzcholek in graph.keys():
    if len(graph[wierzcholek]) % 2 == 1:
        print("Nie jest Eulerowski - nieparzysty stopien")
        break
else:
    if not spojny(graph):
        print("Nie jest Eulerowski - nie spojny")
    else:
        krawedzie = []
        for wierzcholek in graph.keys():
            for polaczenie in graph[wierzcholek]:
                if (polaczenie, wierzcholek) not in krawedzie:
                    krawedzie.append((wierzcholek, polaczenie))
        krawedz_obecna = krawedzie.pop()
        sciezka = [krawedz_obecna]
        kierunek = krawedz_obecna[1]
        while len(krawedzie) != 0:
            mozliwe = []
            for krawedz in krawedzie:
                if krawedz[0] == kierunek or krawedz[1] == kierunek:
                    mozliwe.append(krawedz)
                if len(mozliwe) == 1:
                    if mozliwe[0][0] == kierunek:
                        kierunek = mozliwe[0][1]
                    else:
                        kierunek = mozliwe[0][0]
                    krawedz_obecna = mozliwe[0]
                    krawedzie.remove(krawedz_obecna)
                else:
                    for mozliwa_krawedz in mozliwe:
                        new_graph = {}
                        for krawedz in krawedzie:
                            new_graph[krawedz[0]] = []
                            new_graph[krawedz[1]] = []
                        for krawedz in krawedzie:
                            new_graph[krawedz[0]].append(krawedz[1])
                            new_graph[krawedz[1]].append(krawedz[0])
                        if spojny(new_graph):
                            if mozliwa_krawedz[0] == kierunek:
                                kierunek = mozliwa_krawedz[1]
                            else:
                                kierunek = mozliwa_krawedz[0]
                            krawedz_obecna = mozliwa_krawedz
                            krawedzie.remove(krawedz_obecna)
                            break
            sciezka.append(krawedz_obecna)
        print("Cykl Eulera: {0}".format(sciezka))
