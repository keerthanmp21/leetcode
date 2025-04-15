class DSU2:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * (n)

    def find(self, p):
        p = self.parent[p]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
        
    def check(self):
        res = set()
        for i in self.parent:
            res.add(self.find(i))
        return len(res) == 1

class Solution:
    def earliestAcq2(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        dsu = DSU(n)
        
        for timestamp, a, b in logs:
            dsu.union(a,b)
            if dsu.check():
                return timestamp

        return -1

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()  # sort by timestamp
        uf = UnionFind(n)

        for t, a, b in logs:
            uf.union(a, b)
            if uf.components == 1:
                return t
        return -1

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x]
        return x

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        self.components -= 1
        return True


