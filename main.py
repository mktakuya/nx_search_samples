#!/usr/bin/env python
import os
import csv
import networkx as nx
from netsearch import NetSearch

def is_target(G, n):
    if 'tgt' in G.node[n]:
        return G.node[n]['tgt']
    else:
        return False

def read_edges_from(path):
    with open(os.getcwd() + '/' + path, 'r') as f:
        reader = csv.reader(f)
        edges = list(reader)
    int_edges = []
    for edge in edges:
        int_edges.append(list(map(int, edge)))
    return int_edges

def display_adjacency_list(G):
    for node in G.nodes():
        print("%s: %s" % (node, G.neighbors(node)))
    print()

if __name__ == '__main__':
    # ネットワークの生成
    G = nx.Graph()
    edges = read_edges_from('./data/net.el')
    G.add_edges_from(edges)

    print("【隣接リスト】")
    display_adjacency_list(G)

    start = 1
    print("開始ノードを %s に設定。" % start)

    subject = 18
    print("目的ノードを %s に設定。" % subject)
    G.node[subject]['tgt'] = True
    print()

    print("【幅優先探索】")
    suc, idx = NetSearch.bfs(G, start, is_target)
    if suc:
        print("Found: %s" % idx)
    else:
        print("Not Found")
    print()

    print("【深さ優先探索】")
    suc, idx = NetSearch.dfs(G, start, is_target)

    if suc:
        print("Found: %s" % idx)
    else:
        print("Not Found")
    print()
