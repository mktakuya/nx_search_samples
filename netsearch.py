import time
import sys
from collections import deque
import networkx as nx

class NetSearch:
    def bfs(G, startnode, tgtfunc):
        queue = deque()
        checked = []
        checked.append(startnode)
        queue.append(startnode)

        while len(queue) != 0:
            time.sleep(0.1)
            n = queue.popleft()
            if tgtfunc(G, n):
                print(' %s' % n)
                return True, n
            else:
                print(' %s' % n, end = ' ->')
                for node in G.neighbors(n):
                    if node not in checked:
                        queue.append(node)
                    checked.append(node)
        return False, None

    def dfs(G, startnode, tgtfunc):
        stack = []
        checked = []
        stack.append(startnode)
        checked.append(startnode)

        while len(stack) != 0:
            time.sleep(0.1)
            n = stack.pop()
            if tgtfunc(G, n):
                print(' %s' % n)
                return True, n
            else:
                print(' %s' % n, end = ' ->')
                for node in G.neighbors(n):
                    if node not in checked:
                        stack.append(node)
                    checked.append(node)
        return False, None

