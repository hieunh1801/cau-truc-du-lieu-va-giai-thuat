# Tài liệu tham khảo: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

""" *** Bài toán ***
    Cho N node và M cạnh. 
    Yêu cầu: Tìm kiếm theo chiều sâu của đồ thị khi cho vào 1 node ban đầu

    *** Ý tưởng ***
    https://vi.wikipedia.org/wiki/T%C3%ACm_ki%E1%BA%BFm_theo_chi%E1%BB%81u_s%C3%A2u

    *** Cách giải *** 
    https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
    Step 1: Tạo cây
"""

from collections import defaultdict


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph. if no argument is given, it will created an new empty list
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True
        print("visited", v)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False]*(len(self.graph))

        # Call the recursive helper function to print
        # DFS traversal
        self.DFSUtil(v, visited)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
print(g.graph)
# This code is contributed by Neelam Yadav
