from graph_tool.all import *



def intro():
    # opens your file in mode "read"
    f = open("email-EU-core.txt", "r")
    # splits each line into a list of integers
    lines = [[int(n) for n in x.split()] for x in f.readlines()]
    # closes the file
    f.close()

    # makes the graph
    g = Graph()
    # adds enough vertices (the "1 + " is for position 0)
    # g.add_vertex(1 + max([l[0] for l in lines] + [l[1] for l in lines]))

    # for each line
    for line in lines:
        # make a new edge
        g.add_edge(g.add_vertex(line[0]), g.add_vertex(line[1]))
        # weight it

    pos = gt.(g)
    graph_draw(g, pos)

    pass



if __name__ == '__main__':
    intro()