from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c = Counter(nums)
        return [x[0] for x in c.most_common(k)]


class ImprovedSolution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count: dict[int, int] = {}
        freq: list[list[int]] = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for c, v in count.items():
            freq[v].append(c)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return []
