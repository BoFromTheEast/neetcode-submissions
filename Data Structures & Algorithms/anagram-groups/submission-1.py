class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)

        for idx in strs:
            sortedChars = "".join(sorted(idx))
            mapper[sortedChars].append(idx)

        return list(mapper.values())