from graph_tool.all import *
from random import randint, choice, randrange

def NewTreeMap(depth, growth=(2, 5)):
    m = Graph()
    layers = [[] for x in range(depth)]
    layers[0].append(m.add_vertex())
    for i in range(depth-1):
        for v in layers[i]:
            for n in m.add_vertex(randint(growth[0], growth[1])):
                layers[i+1].append(n)
                m.add_edge(v, n)
                #m.add_edge(n, v)
    return m, layers

def AddLoopBacks(m, layers, difference, growth = (2, 3)):
    mlay = [[v for v in layer] for layer in layers]
    for i in range(difference, len(layers)):
        for j in range(len(layers[i])//randint(growth[0], growth[1])+1):
            start = mlay[i].pop(randrange(len(mlay[i])))
            end = choice(layers[i-randint(2, difference)])
            m.add_edge(start, end)
            print("backup")



if __name__ == "__main__":
    m, l = NewTreeMap(4, (2, 3))
    layout = radial_tree_layout(m, m.vertex(0))
    AddLoopBacks(m, l, 3)
    #layout = arf_layout(m, max_iter=0, d = 2.5, a=3)
    graph_draw(m, pos=layout, vertex_font_size=12, output_size=(1000, 1000), output="temp.png")