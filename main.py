v = []


class Vertex:
    def __init__(self, v, x, y):
        self.v = v
        self.x = x
        self.y = y
        self.her = None


def create_vertex(v, x, y):
    return Vertex(v, x, y)


def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print("Vertex ", v, " already exists.")
    else:
        vertices_no = vertices_no + 1
        graph[v] = []


def add_edge(v1, v2, e):
    global graph
    if v1 not in graph:
        print("Vertex ", v1, " does not exist.")
    elif v2 not in graph:
        print("Vertex ", v2, " does not exist.")
    else:

        temp = [v2, e]
        graph[v1].append(temp)


def h(p1, p2):
    return abs((p2.x - p1.x) + (p2.y - p1.y))

def a_star(start,end):
    visted=[start]
    fringe=[start]
    path=[start]
    x=start
    while True:
        if x == end :
            return visted
        for edges in graph[x]:
            y = edges[0]
            y.her=h(edges[0],end)+edges[1]


            # print(y.her)
            fringe.append(y)

        min = y
        for i in fringe:
            if i not in visted:
                visted.append(i)
                x = i
                fringe.clear()
                print(x.v)







def comper(x,y):
    if x<y:
        return True

vertices_no = 0
graph = {}
v68 = create_vertex(68, 863, 95)
v69 = create_vertex(69, 870, 146)
v76 = create_vertex(76, 824, 423)
v78 = create_vertex(78, 837, 384)
v82 = create_vertex(82, 876, 198)
v83 = create_vertex(83, 882, 262)
v84 = create_vertex(84, 979, 342)
v85 = create_vertex(85, 973, 184)
v86 = create_vertex(86, 966, 127)
v87 = create_vertex(87, 1024, 62)
v88 = create_vertex(88, 1147, 101)
v89 = create_vertex(89, 1263, 127)
v90 = create_vertex(90, 1244, 178)
v91 = create_vertex(91, 1238, 236)
v92 = create_vertex(92, 1231, 298)
v93 = create_vertex(93, 1224, 358)
v94 = create_vertex(94, 986, 306)
v95 = create_vertex(95, 952, 453)

add_vertex(v68)
add_vertex(v69)
add_vertex(v76)
add_vertex(v78)
add_vertex(v82)
add_vertex(v83)
add_vertex(v84)
add_vertex(v85)
add_vertex(v86)
add_vertex(v87)
add_vertex(v88)
add_vertex(v89)
add_vertex(v90)
add_vertex(v91)
add_vertex(v92)
add_vertex(v93)
add_vertex(v94)
add_vertex(v95)

add_edge(v68, v69, 1.3)
add_edge(v69, v68, 1.3)
add_edge(v68,v87,4.4)
add_edge(v87,v68,4.4)
add_edge(v69, v86, 2.6)
add_edge(v69, v82, 1.2)
add_edge(v86, v69, 2.6)
add_edge(v82, v69, 1.2)
add_edge(v86,v90,7.5)
add_edge(v90,v86,7.5)
add_edge(v86,v85,1.3)
add_edge(v85,v86,1.3)
add_edge(v85,v84,1.3)
add_edge(v84,v85,1.3)
add_edge(v85,v91,7.1)
add_edge(v91,v85,7.1)
add_edge(v84,v92,7)
add_edge(v92,v84,7)
add_edge(v84,v94,1.3)
add_edge(v94,v84,1.3)
add_edge(v94,v93,7)
add_edge(v93,v94,7)
add_edge(v94,v95,3.5)
add_edge(v95,v94,3.5)
add_edge(v95,v76,3)
add_edge(v76,v95,3)
add_edge(v76,v78,0.75)
add_edge(v78,v76,0.75)
add_edge(v78,v83,3.3)
add_edge(v83,v78,3.3)
add_edge(v83,v84,2.6)
add_edge(v84,v83,2.6)
add_edge(v83,v82,1.3)
add_edge(v82,v83,1.3)
add_edge(v89,v90,1.3)
add_edge(v90,v89,1.3)
add_edge(v90,v91,1.3)
add_edge(v91,v90,1.3)
add_edge(v91,v92,1.3)
add_edge(v92,v91,1.3)
add_edge(v92,v93,1.3)
add_edge(v93,v92,1.3)
add_edge(v87,v88,3.4)
add_edge(v88,v87,3.4)
add_edge(v88,v89,3.1)
add_edge(v89,v88,3.1)









def main():
    a_star(v68,v90)


if __name__ == "__main__":
    main()

