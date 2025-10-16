class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict:",self.graph_dict)

    def get_path(self,end,path=[]):
        path = path +[start]

        if start == end:
            return [path]


if __name__ == '__main__':
    routes = [
        ('mumbai','paris'),
        ('mumbai','dubai'),
        ('paris','dubai'),
        ('paris','new york'),
        ('dubai','new york'),
        ('new yourk','toronto'),
    ]
    route_graph = Graph(routes)
    start = 'mumbai'
    end = 'mumbai'
    print(f'path between {start} and {end}:',route_graph.get_path(start,end))