from search import Graph

def main():
    g = Graph('./data/tiny_network.adjlist')
    result = len(g.bfs("31806696"))
    print(result)


main()

