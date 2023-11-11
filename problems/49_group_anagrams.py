from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        store = defaultdict(list)
        for string in strs:
            store["".join(sorted(string))].append(string)
        return list(store.values())
