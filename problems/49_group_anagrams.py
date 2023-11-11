from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        store = defaultdict(list)
        for string in strs:
            store["".join(sorted(string))].append(string)
        return list(store.values())


class ImprovedSolution:
    # Note: We know the input is only lowercase english, so we can make the counting
    # checks O(n) across the strings rather than sorting them
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        store = defaultdict(list)
        for s in strs:
            seq = [0] * 26  # lowercase english
            for char in s:
                seq[ord(char) - ord("a")] += 1
            store[tuple(seq)].append(s)
        return list(store.values())
