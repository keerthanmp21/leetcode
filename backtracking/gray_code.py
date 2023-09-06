from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res_list = []
        res_set = set()

        def inner(root):
            if root in res_set:
                return
            else:
                res_list.append(int(root, 2))
                res_set.add(root)
            if len(res_list) == (2**n):
                return
            for i in range(len(root)):
                temp_val = root[len(root) - i - 1]
                temp_val = "0" if temp_val == "1" else "1"
                temp_root = (
                    root[0 : len(root) - i - 1] + temp_val + root[len(root) - i :]
                )
                inner(temp_root)

        inner("0" * n)

        return res_list
