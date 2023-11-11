class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        store: dict[int, int] = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in store:
                return [store[diff], idx]
            store[n] = idx
        return []
