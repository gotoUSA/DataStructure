import math
import heapq

graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]} #무방향
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]} #방향

g1 = {1: [2, 3, 4], 2: [1, 5], 3: [1, 6], 4: [1, 6], 5: [2, 6], 6: [3, 4, 5]}
g2 = {1: [3], 2: [3], 3: [5, 6], 4: [6], 5: [], 6: [5]}


graph = {
    "A": [("B", 1), ("C", 4), ("D", 5)],
    "B": [("A", 1), ("D", 2)],
    "C": [("A", 4), ("D", 4), ("E", 3)],
    "D": [("A", 5), ("B", 2), ("C", 4), ("F", 3)],
    "E": [("C", 3), ("F", 2)],
    "F": [("D", 3), ("E", 2)]
}


def dfs_recursive(graph,node):
    res=[]
    visited=set()
    
    def _dfs(u):
        if u in visited:
            return
        
        visited.add(u)
        res.append(u)
        
        for v in graph[u]:
            _dfs(v)
            
    _dfs(node)
    return res

def dfs(graph,node):
    res=[]
    stack=[node]
    visited= set(stack)
    
    while stack:
        u=stack.pop()
        res.append(u)
        
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
                
    return res

node_from={node: "" for node in graph}

def bfs(graph,node):
    res=[]
    queue=[node]
    visited=set(queue)
    while queue:
        u= queue.pop(0)
        res.append(u)
        for v,w in graph[u]:
            if v not in visited:
                node_from[v]=u
                visited.add(v)
                queue.append(v)
    return res


def dijkstra(graph,node):
    lead_time={node:math.inf for node in graph}
    node_from={node:None for node in graph}
    
    lead_time[node]=0
    visited=set()
    
    heap=[]
    heapq.heappush(heap,(0,node))
    
    while heap:
        prev_time,u=heapq.heappop(heap)
       
        for v, weight in graph[u]:
            if (new_time:=prev_time +weight) < lead_time[v]:
                lead_time[v]=new_time
                node_from[v]=u
                heapq.heappush(heap,(lead_time[v],v))
                
    return lead_time,node_from

def shortest_path(node_from, lead_time, start, end):
    path = ""
    node = end
    while node_from[node]:
        path = " → " + str(node) + path
        node = node_from[node]
    return f"{str(node) + path} (cost = {str(lead_time[end])})"
            
            
class Graph:
    def __init__(self):
        self.graph = {}
        self.cost={}
        self.node_form={}

#    def __str__(self):
#        return str(self.graph)

#사전을 보기 좋게 출력해 주는 pprint를 이용     
    def display(self):
        from pprint import pprint
        pprint(self.graph)
        print()

    def add_nodes(self, *nodes):
        for u in nodes:
            #노드가 그래프에 없을 때 추가한다.
            if u not in self.graph:
                self.graph[u] = {}


    def add_edges(self, *edges):
        for edge in edges:
            u, v = edge[0], edge[1]
            #간선 정보에 가중치가 없으면 0을 넣는다.
            w = edge[2] if len(edge) == 3 else 0

            #노드를 삽입하고, 연결될 노드와 가중치를 입력한다.
            self.add_nodes(u, v)
            self.graph[u][v] = w
            self.graph[v][u] = w
            
    def delete_edges(self, *edges):
        for u, v in edges:
            self.graph[u].pop(v, None)
            self.graph[v].pop(u, None)
            
    def delete_nodes(self, *nodes):
        for u in nodes:
            if u not in self.graph:
                continue
            for v in self.graph[u]:
                self.graph[v].pop(u, None)
            del self.graph[u]
            
    def dfs(self, node):
        res = []
        visited = set()

        self.cost = {node: 0 for node in self.graph}
        self.node_from = {node: None for node in self.graph}

        def _dfs(u):
            visited.add(u)
            res.append(u)
            for v in self.graph[u]:
                if v not in visited:
                    self.cost[v] = self.cost[u] + self.graph[u][v]
                    self.node_from[v] = u
                    _dfs(v)

        _dfs(node)
        return res
    
    def bfs(self, node):
        from collections import deque

        res = []
        queue = deque([node])
        visited = set(queue)

        #비용과 노드 정보를 저장하는 사전을 초기화한다.
        self.cost = {node: 0 for node in self.graph}
        self.node_from = {node: None for node in self.graph}

        while queue:
            u = queue.popleft()
            res.append(u)
            #현재 노드(u)와 간선으로 연결된 노드(v)를 가져온다.
            #사전을 그냥 순회할 때는 키(key)만 가져온다.
            for v in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    #노드 v로 가는 비용과 경로 정보를 저장한다.
                    #self.graph[u][v]는 노드 u와 v를 연결하는 간선의 가중치다.
                    self.cost[v] = self.cost[u] + self.graph[u][v]
                    self.node_from[v] = u
                    queue.append(v)

        return res
    
    def dijkstra(self, start):
        import math, heapq

        #비용과 노드 정보를 저장하는 사전을 초기화한다.
        self.cost = {node: math.inf for node in self.graph}
        self.node_from = {node: None for node in self.graph}
        self.cost[start] = 0

        res = []
        visited = set()

        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            prev_time, u = heapq.heappop(heap)
            if u in visited:
                continue
            res.append(u)
            visited.add(u)
            #현재 노드(u)와 간선으로 연결된 노드(v)를 가져온다.
            for v in self.graph[u]:
                #가중치 정보를 가져와서 인접노드로 가는 비용을 계산하고 갱신한다.
                if (new_time := prev_time + self.graph[u][v]) < self.cost[v]:
                    self.cost[v] = new_time
                    self.node_from[v] = u
                    heapq.heappush(heap, (self.cost[v], v))
        return res

    def get_path(self, end):
        path = ""
        node = end
        while self.node_from[node]:
            path = " → " + str(node) + path
            node = self.node_from[node]

        #기존 코드에서 수정한 부분
        #한 노드에서 다른 노드로 가는 경로가 없을 때도 처리
        if path:
            path = str(node) + path
            return f"{path} (cost = {str(self.cost[end])})"
        else:
            return f"There is no path."

class Digraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edges(self, *edges):
        for edge in edges:
            u, v = edge[0], edge[1]
            w = edge[2] if len(edge) == 3 else 0
            self.add_nodes(u, v)
            #노드 u에서 v로 가는 간선만 추가한다.
            self.graph[u][v] = w

    def delete_nodes(self, *nodes):
        for u in nodes:
            if u not in self.graph:
                continue
            for v in self.graph: #기존의 self.graph[u]를 수정
                self.graph[v].pop(u, None)
            del self.graph[u]


g = Digraph()
g.add_edges(("A", "C", 4), ("B", "C", 2))
g.add_edges(("C", "E", 3), ("C", "F", 5), ("D", "B", 3))
g.add_edges(("E", "F", 1), ("F", "D", 2))

