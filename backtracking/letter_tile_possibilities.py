class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        def dfs(prefix, tiles):
            if prefix in res:
                return
            res.add(prefix)
            for i, t in enumerate(tiles):
                dfs(prefix + t, tiles[:i] + tiles[i + 1 :])

        dfs("", tiles)
        return len(res) - 1
