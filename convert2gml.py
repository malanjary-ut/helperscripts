#!/usr/bin/python
import networkx as nx
import argparse

def addattributes(G,d,attr):
    A = {}
    with open(attr,"r") as fil:
        titles = [x.replace(" ","").replace("-","").replace("_","") for x in fil.next().strip().split(d)]
        for x in titles[1:]:
            A[x] = {}
        for line in fil:
            cols = line.strip().split(d)
            for i,col in enumerate(cols):
                if i and cols[0] in G.nodes():
                    A[titles[i]][cols[0]] = col
    for title,item in A.items():
        nx.set_node_attributes(G,title,item)
    return G

def convert2gml(fname,outname,header,attr,rw,d="\t"):
    G=nx.Graph()
    alledges=[]
    with open(fname,"U") as fil:
        for line in fil:
            if header:
                #skip first line
                header = False
                continue
            x=line.strip().split(d)
            if len(x)>=3:
                if rw:
                    w = float(x[2])
                else:
                    # Convert distance to weight (0-1.0) lower distance = higher weight
                    w = 1.0-float(x[2])
                alledges.append([str(x[0]),str(x[1]),w])
    G.add_weighted_edges_from(alledges)
    if attr:
        G = addattributes(G,d,attr)
    nx.write_gml(G,outname)

# Commandline Execution
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Convert table to gml file""")
    parser.add_argument("input", help="Table to convert (3 columns, ex row: node1    node2    0.889 )")
    parser.add_argument("-d", "--delim", help="Delimiter. (default=Tab separated columns)", default="\t")
    parser.add_argument("-o", "--outgml", help="Filename for gml output (default=output.gml)",default="output.gml")
    parser.add_argument("-aa", "--addattributes", help="Filename with list of attributes to add. Attribute titles should be placed in first line and no spaces used ex: (node_id    attribute_1    attribute_2)",default="")
    parser.add_argument("-sh", "--skipheader", help="Skip first line if header exists (default=False)",action="store_true",default=False)
    parser.add_argument("-rw", "--rawweight", help="Third column edge weight will be read directly without processing. Default converts lower distance values (0-1.0) to higher weight = (1 - distance)",action="store_true",default=False)
    args = parser.parse_args()
    convert2gml(args.input, args.outgml, args.skipheader, args.addattributes, args.rawweight, args.delim)