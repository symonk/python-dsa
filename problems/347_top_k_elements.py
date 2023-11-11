from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c = Counter(nums)
        return [x[0] for x in c.most_common(k)]
