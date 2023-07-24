from collections import defaultdict, deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # bfs
        adj_dict = defaultdict(list)
        bank.append(startGene)
        for gene in bank:
            for i in range(8):
                pattern = gene[:i] + '*' + gene[i+1:]
                adj_dict[pattern].append(gene)

        q = deque()
        visitSet = set()
        q.append(startGene)
        steps = 0

        while q:
            for _ in range(len(q)):
                gene = q.popleft()
                if gene == endGene:
                    return steps
                for i in range(8):
                    pattern = gene[:i] + '*' + gene[i+1:]
                    for adj_gene in adj_dict[pattern]:
                        if adj_gene not in visitSet:
                            q.append(adj_gene)
                            visitSet.add(adj_gene)
            steps += 1

        return -1


