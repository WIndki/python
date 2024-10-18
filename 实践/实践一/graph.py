class Graph:
    # 初始化一个空的字典来存储图的结构，邻接表实现
    def __init__(self):
        self.graph = {}  # 初始化一个空的字典来存储图的结构

    def add_vertex(self, vertex):
        if vertex not in self.graph:  # 如果顶点不在图中
            self.graph[vertex] = []  # 将顶点添加到图中，并初始化一个空列表

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:  # 如果两个顶点都在图中
            self.graph[vertex1].append(vertex2)  # 在vertex1的邻接列表中添加vertex2
            self.graph[vertex2].append(vertex1)  # 在vertex2的邻接列表中添加vertex1

    def display(self):
        for vertex in self.graph:  # 遍历图中的每个顶点
            print(f"{vertex}: {self.graph[vertex]}")  # 打印顶点及其邻接列表

# 示例用法
if __name__ == "__main__":
    g = Graph()  # 创建一个图的实例
    g.add_vertex("A")  # 添加顶点A
    g.add_vertex("B")  # 添加顶点B
    g.add_vertex("C")  # 添加顶点C
    g.add_edge("A", "B")  # 添加边A-B
    g.add_edge("A", "C")  # 添加边A-C
    g.display()  # 显示图的结构