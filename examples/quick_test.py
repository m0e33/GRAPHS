status = False
try:
    import snap
    import graph_tools
    import networkx
    status = True
except:
    pass

if status:
    print("SUCCESS, Snap, graph_tools and networkx are installed")
else:
    print("*** ERROR, something is missing")
